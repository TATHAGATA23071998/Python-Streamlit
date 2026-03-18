# ENVIRONMENT_GRASSLAND.py
# Requirements (put in requirements.txt):
# streamlit
# pandas
# plotly
# openpyxl
# numpy
# requests

import os
import io
import requests
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

# -------------------------
# 1. App config + title
# -------------------------
st.set_page_config(page_title="Bird Biodiversity Dashboard", layout="wide", page_icon="🐦")
st.title("Avian Biodiversity & Conservation Dashboard")
st.markdown(
    "An interactive EDA covering species distribution, temporal activity, and conservation priorities "
    "across Forest and Grassland ecosystems."
)

# -------------------------
# 2. Data loader (deployment safe)
# -------------------------
@st.cache_data(show_spinner=True)
def load_data():
    """
    Tries, in order:
      1) local repo data/Final_Master_Dashboard_Data.xlsx or .xls
      2) top-level Final_Master_Dashboard_Data.xlsx or .xls
      3) a remote URL from st.secrets['DATA_URL']
      4) interactive upload via st.file_uploader (when run locally / manually)
    Returns a preprocessed DataFrame or stops the app with an error message.
    """
    candidates = [
        "data/Final_Master_Dashboard_Data.xlsx",
        "data/Final_Master_Dashboard_Data.xls",
        "Final_Master_Dashboard_Data.xlsx",
        "Final_Master_Dashboard_Data.xls",
    ]

    # 1) try local repo files
    for path in candidates:
        if os.path.exists(path):
            try:
                if path.lower().endswith(".xlsx"):
                    df = pd.read_excel(path, engine="openpyxl")
                else:
                    df = pd.read_excel(path)
                st.write(f"Loaded dataset from `{path}`")
                return _postprocess(df)
            except Exception as e:
                st.error(f"Found file at `{path}` but failed to read it. Error: {e}")
                st.stop()

    # 2) try remote URL from secrets (useful on Streamlit Cloud / other host)
    data_url = None
    try:
        # st.secrets behaves like a dict; if not set, .get returns None
        data_url = st.secrets.get("DATA_URL") if hasattr(st, "secrets") else None
    except Exception:
        data_url = None

    if data_url:
        try:
            r = requests.get(data_url, timeout=30)
            r.raise_for_status()
            content = io.BytesIO(r.content)
            if data_url.lower().endswith(".xlsx"):
                df = pd.read_excel(content, engine="openpyxl")
            else:
                df = pd.read_excel(content)
            st.write("Loaded dataset from remote DATA_URL")
            return _postprocess(df)
        except Exception as e:
            st.error(f"Could not download/parse file from DATA_URL: {e}")
            st.stop()

    # 3) interactive upload fallback (useful for local testing)
    uploaded = st.file_uploader(
        "Upload `Final_Master_Dashboard_Data` (xlsx or xls). If you are deploying, prefer placing the file in `data/` or set DATA_URL in secrets.",
        type=["xlsx", "xls"],
    )
    if uploaded is not None:
        try:
            if uploaded.name.lower().endswith(".xlsx"):
                df = pd.read_excel(uploaded, engine="openpyxl")
            else:
                df = pd.read_excel(uploaded)
            st.write(f"Loaded dataset from uploaded file: {uploaded.name}")
            return _postprocess(df)
        except Exception as e:
            st.error(f"Failed to read uploaded file: {e}")
            st.stop()

    # If nothing found:
    st.error(
        "Dataset not found. Put `Final_Master_Dashboard_Data.xlsx` in the repo `data/` folder,\n"
        "or set a public file URL in Streamlit secrets as `DATA_URL`, or upload the file via the widget."
    )
    st.stop()


def _postprocess(df: pd.DataFrame) -> pd.DataFrame:
    """
    Defensive post-processing: parse dates, create Month/Year/Hour, normalize booleans,
    and simple normalization for categorical columns used in the app.
    """
    df = df.copy()

    # Parse Date safely
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df["Year"] = df["Date"].dt.year
        df["Month"] = df["Date"].dt.month_name()
        df["YearMonth"] = df["Date"].dt.to_period("M").astype(str)
    else:
        df["Date"] = pd.NaT
        df["Year"] = np.nan
        df["Month"] = np.nan
        df["YearMonth"] = np.nan

    # Parse Start_Time -> Hour safely
    if "Start_Time" in df.columns:
        # Accept common time formats
        df["Hour"] = pd.to_datetime(df["Start_Time"], errors="coerce").dt.hour
    else:
        df["Hour"] = np.nan

    # Normalize PIF_Watchlist_Status -> boolean-like
    if "PIF_Watchlist_Status" in df.columns:
        df["PIF_Watchlist_Status"] = (
            df["PIF_Watchlist_Status"]
            .astype(str)
            .str.strip()
            .str.lower()
            .map(lambda x: True if x in ["true", "1", "yes", "y", "t"] else (False if x in ["false", "0", "no", "n", "f"] else np.nan))
        )

    # Normalize Flyover_Observed to boolean-like where present
    if "Flyover_Observed" in df.columns:
        df["Flyover_Observed"] = (
            df["Flyover_Observed"]
            .astype(str)
            .str.strip()
            .str.lower()
            .map(lambda x: True if x in ["true", "1", "yes", "y", "t"] else (False if x in ["false", "0", "no", "n", "f"] else np.nan))
        )

    # Clean string columns commonly used: Habitat, Plot_Name, Admin_Unit_Code, Observer
    for c in ["Habitat", "Plot_Name", "Admin_Unit_Code", "Observer", "Common_Name", "Scientific_Name", "Disturbance"]:
        if c in df.columns:
            df[c] = df[c].astype(str).str.strip()
            # preserve NaN that were true NaN (convert 'nan' back)
            df.loc[df[c].isin(["nan", "None", "NoneType", "<NA>"]), c] = np.nan

    return df


# -------------------------
# 3. Load data
# -------------------------
df = load_data()  # stops the app with helpful message if file not found

# -------------------------
# 4. Sidebar filters & controls
# -------------------------
st.sidebar.header("Filter Data / Settings")

# Habitat filter
habitat_options = df["Habitat"].dropna().unique().tolist() if "Habitat" in df.columns else []
selected_habitats = st.sidebar.multiselect(
    "Select Ecosystem / Habitat:", options=habitat_options, default=habitat_options
)

# Admin Unit filter (dynamic)
available_sites = (
    df[df["Habitat"].isin(selected_habitats)]["Admin_Unit_Code"].dropna().unique().tolist()
    if ("Admin_Unit_Code" in df.columns and len(selected_habitats) > 0)
    else df["Admin_Unit_Code"].dropna().unique().tolist() if "Admin_Unit_Code" in df.columns else []
)
selected_sites = st.sidebar.multiselect("Select Administrative Unit:", options=available_sites, default=available_sites)

# Date range filter (optional)
if "Date" in df.columns and df["Date"].notna().any():
    min_date = df["Date"].min()
    max_date = df["Date"].max()
    date_range = st.sidebar.date_input("Date range", value=(min_date, max_date))
else:
    date_range = None

# Data subset according to filters
filtered_df = df.copy()
if selected_habitats:
    filtered_df = filtered_df[filtered_df["Habitat"].isin(selected_habitats)]
if selected_sites:
    filtered_df = filtered_df[filtered_df["Admin_Unit_Code"].isin(selected_sites)]
if date_range and len(date_range) == 2:
    start, end = date_range
    if pd.notna(start) and pd.notna(end):
        filtered_df = filtered_df[(filtered_df["Date"] >= pd.to_datetime(start)) & (filtered_df["Date"] <= pd.to_datetime(end))]

# If filtered_df is empty show info and avoid plotting errors
if filtered_df.empty:
    st.warning("No records match the selected filters. Adjust filters or upload a different dataset.")
    st.stop()

# -------------------------
# 5. Executive KPIs
# -------------------------
st.markdown("### High-Level Metrics")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Total Observations", value=f"{len(filtered_df):,}")
with col2:
    unique_species = int(filtered_df["Scientific_Name"].nunique()) if "Scientific_Name" in filtered_df.columns else 0
    st.metric(label="Unique Species", value=f"{unique_species:,}")
with col3:
    at_risk = int(filtered_df[filtered_df["PIF_Watchlist_Status"] == True].shape[0]) if "PIF_Watchlist_Status" in filtered_df.columns else 0
    st.metric(label="At-Risk Bird Sightings", value=f"{at_risk:,}")
with col4:
    active_observers = int(filtered_df["Observer"].nunique()) if "Observer" in filtered_df.columns else 0
    st.metric(label="Active Observer Count", value=f"{active_observers:,}")

st.divider()

# -------------------------
# 6. Tabs / charts
# -------------------------
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
    [
        "🗺️ Spatial & Temporal",
        "🐦 Species Analysis",
        "⛅ Environment",
        "📏 Distance & Behavior",
        "🧑‍🔬 Observer Trends",
        "🛡️ Conservation",
    ]
)

# --- TAB 1: Spatial & Temporal ---
with tab1:
    st.markdown("#### Spatial & Temporal Trends")
    c1, c2 = st.columns(2)

    with c1:
        if "Admin_Unit_Code" in filtered_df.columns:
            fig_admin = px.histogram(
                filtered_df,
                x="Admin_Unit_Code",
                color="Habitat" if "Habitat" in filtered_df.columns else None,
                barmode="group",
                title="Observation Frequency by Admin Unit & Habitat",
                color_discrete_sequence=px.colors.qualitative.Vivid,
            )
            st.plotly_chart(fig_admin, use_container_width=True)
        else:
            st.info("No `Admin_Unit_Code` column to show spatial histogram.")

    with c2:
        # Seasonal Trends
        if "Month" in filtered_df.columns:
            # If you want to order month, you can provide category_orders. For dynamic months, just show counts.
            fig_month = px.histogram(
                filtered_df, x="Month", color="Habitat" if "Habitat" in filtered_df.columns else None, barmode="group", title="Seasonal Trends: Observations by Month"
            )
            st.plotly_chart(fig_month, use_container_width=True)
        else:
            st.info("No `Month` column to show seasonal trends.")

    # Time of Day Correlation
    if "Hour" in filtered_df.columns:
        fig_hour = px.histogram(
            filtered_df,
            x="Hour",
            color="Habitat" if "Habitat" in filtered_df.columns else None,
            barmode="group",
            title="Observation Time: Bird Activity by Hour of Day (24H)",
            labels={"Hour": "Hour of Day"},
        )
        fig_hour.update_layout(xaxis=dict(tickmode="linear", dtick=1))
        st.plotly_chart(fig_hour, use_container_width=True)

# --- TAB 2: Species Analysis ---
with tab2:
    st.markdown("#### Species Diversity & Activity Patterns")
    c1, c2 = st.columns(2)

    with c1:
        if {"Plot_Name", "Scientific_Name"}.issubset(filtered_df.columns):
            plot_div = filtered_df.groupby("Plot_Name")["Scientific_Name"].nunique().reset_index()
            plot_div = plot_div.sort_values(by="Scientific_Name", ascending=False).head(10)
            fig_div = px.bar(
                plot_div,
                x="Scientific_Name",
                y="Plot_Name",
                orientation="h",
                title="Hotspots: Top 10 Plots by Unique Species",
                labels={"Scientific_Name": "Unique Species Count"},
            )
            fig_div.update_layout(yaxis={"categoryorder": "total ascending"})
            st.plotly_chart(fig_div, use_container_width=True)
        else:
            st.info("Need `Plot_Name` and `Scientific_Name` to compute plot diversity.")

    with c2:
        if "ID_Method" in filtered_df.columns:
            fig_id = px.histogram(
                filtered_df, x="ID_Method", color="Habitat" if "Habitat" in filtered_df.columns else None, barmode="group", title="Activity Patterns: Identification Method"
            )
            st.plotly_chart(fig_id, use_container_width=True)
        else:
            st.info("No `ID_Method` column present.")

    # Sex Ratio
    if "Sex" in filtered_df.columns:
        sex_df = filtered_df[filtered_df["Sex"].isin(["Male", "Female"])]
        if not sex_df.empty:
            fig_sex = px.histogram(
                sex_df, x="Habitat" if "Habitat" in sex_df.columns else None, color="Sex", barmode="group", title="Sex Ratio by Habitat (Confirmed Identifications Only)"
            )
            st.plotly_chart(fig_sex, use_container_width=True)
        else:
            st.info("No confirmed Male/Female sex records found.")

# --- TAB 3: Environment ---
with tab3:
    st.markdown("#### Environmental Conditions & Correlations")
    c1, c2 = st.columns(2)

    with c1:
        if "Disturbance" in filtered_df.columns:
            fig_dist = px.histogram(filtered_df, y="Disturbance", color="Habitat" if "Habitat" in filtered_df.columns else None, barmode="group", title="Impact of Environmental Disturbance")
            st.plotly_chart(fig_dist, use_container_width=True)
        else:
            st.info("No `Disturbance` column present.")

    with c2:
        if {"Temperature", "Humidity"}.issubset(filtered_df.columns):
            fig_weather = px.density_contour(
                filtered_df,
                x="Temperature",
                y="Humidity",
                color="Habitat" if "Habitat" in filtered_df.columns else None,
                title="Weather Correlation: Temp vs Humidity",
                marginal_x="histogram",
                marginal_y="histogram",
            )
            st.plotly_chart(fig_weather, use_container_width=True)
        else:
            st.info("Need `Temperature` and `Humidity` to show weather correlation.")

# --- TAB 4: Distance & Behavior ---
with tab4:
    st.markdown("#### Observation Distance & Bird Behavior")
    c1, c2 = st.columns(2)

    with c1:
        if "Distance" in filtered_df.columns:
            fig_dist_range = px.histogram(filtered_df, x="Distance", color="Habitat" if "Habitat" in filtered_df.columns else None, barmode="group", title="Distance Analysis: Observation Range")
            st.plotly_chart(fig_dist_range, use_container_width=True)
        else:
            st.info("No `Distance` column present.")

    with c2:
        if "Flyover_Observed" in filtered_df.columns:
            fig_fly = px.histogram(filtered_df, x="Habitat" if "Habitat" in filtered_df.columns else None, color="Flyover_Observed", barmode="group", title="Behavior: Flyover Frequency by Habitat")
            st.plotly_chart(fig_fly, use_container_width=True)
        else:
            st.info("No `Flyover_Observed` column present.")

# --- TAB 5: Observer Trends ---
with tab5:
    st.markdown("#### Field Staff & Observer Trends")
    c1, c2 = st.columns(2)

    with c1:
        if "Observer" in filtered_df.columns:
            obs_counts = filtered_df["Observer"].value_counts().reset_index().head(10)
            obs_counts.columns = ["Observer", "Count"]
            fig_obs = px.bar(obs_counts, x="Count", y="Observer", orientation="h", title="Observer Trends: Top 10 Most Active Field Staff")
            fig_obs.update_layout(yaxis={"categoryorder": "total ascending"})
            st.plotly_chart(fig_obs, use_container_width=True)
        else:
            st.info("No `Observer` column available.")

    with c2:
        if "Visit" in filtered_df.columns:
            fig_visit = px.histogram(filtered_df, x="Visit", color="Habitat" if "Habitat" in filtered_df.columns else None, barmode="group", title="Visit Patterns: Repeated Visits to Plots")
            st.plotly_chart(fig_visit, use_container_width=True)
        else:
            st.info("No `Visit` column available.")

# --- TAB 6: Conservation Insights ---
with tab6:
    st.markdown("#### Conservation Priorities & At-Risk Species")
    c1, c2 = st.columns(2)

    with c1:
        if "PIF_Watchlist_Status" in filtered_df.columns:
            # Coerce non-bools for plotting
            tmp = filtered_df.copy()
            tmp["PIF_plot"] = tmp["PIF_Watchlist_Status"].map({True: "At-risk", False: "Not at-risk", np.nan: "Unknown"})
            fig_watch = px.histogram(tmp, x="Habitat" if "Habitat" in tmp.columns else None, color="PIF_plot", barmode="group", title="Watchlist Trends: At-Risk Species Sightings", color_discrete_map={"At-risk": "red", "Not at-risk": "lightgrey", "Unknown": "silver"})
            st.plotly_chart(fig_watch, use_container_width=True)
        else:
            st.info("No `PIF_Watchlist_Status` column present.")

    with c2:
        # AOU/Species patterns among at-risk records
        watchlist_df = filtered_df[filtered_df.get("PIF_Watchlist_Status") == True] if "PIF_Watchlist_Status" in filtered_df.columns else pd.DataFrame()
        if watchlist_df.empty:
            st.info("No at-risk (PIF) records in the current filter.")
        else:
            if "AOU_Code" in watchlist_df.columns and watchlist_df["AOU_Code"].notna().any():
                aou_counts = watchlist_df["AOU_Code"].value_counts().reset_index().head(10)
                aou_counts.columns = ["AOU_Code", "Count"]
                fig_aou = px.bar(aou_counts, x="AOU_Code", y="Count", title="AOU Code Patterns: Top 10 At-Risk Species Codes", color="Count", color_continuous_scale="Reds")
            elif "Common_Name" in watchlist_df.columns:
                aou_counts = watchlist_df["Common_Name"].value_counts().reset_index().head(10)
                aou_counts.columns = ["Common_Name", "Count"]
                fig_aou = px.bar(aou_counts, x="Common_Name", y="Count", title="Top 10 At-Risk Species (by common name)", color="Count", color_continuous_scale="Reds")
            else:
                st.info("At-risk records present but neither `AOU_Code` nor `Common_Name` are available.")
                fig_aou = None

            if fig_aou is not None:
                st.plotly_chart(fig_aou, use_container_width=True)

# -------------------------
# 7. Footer / quick export
# -------------------------
st.sidebar.markdown("---")
st.sidebar.write("Quick export of filtered data")
csv = filtered_df.to_csv(index=False)
st.sidebar.download_button("Download filtered dataset (CSV)", data=csv, file_name="filtered_birds.csv", mime="text/csv")
st.sidebar.markdown("If you deploy to Streamlit Cloud, add the dataset to `/data/` in the repo or set `DATA_URL` in Secrets.")

# End of app
