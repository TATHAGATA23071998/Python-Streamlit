import streamlit as st
import pandas as pd
import plotly.express as px

# ==============================================================================
# 1. Dashboard Configuration & Setup
# ==============================================================================
st.set_page_config(page_title="Bird Biodiversity Dashboard", layout="wide", page_icon="🐦")
st.title("Avian Biodiversity & Conservation Dashboard")
st.markdown("An interactive EDA covering species distribution, temporal activity, and conservation priorities across Forest and Grassland ecosystems.")

# ==============================================================================
# 2. Data Loading & Preprocessing
# ==============================================================================
@st.cache_data
def load_data():
    #file_path = r"C:\Users\tatha\Downloads\NEW_PROJECT\Final_Master_Dashboard_Data.xls"
    file_path = r"file_path = r"C:\Users\tatha\Downloads\NEW_PROJECT\Final_Master_Dashboard_Data.xls""
    df = pd.read_excel(file_path)
    
    # Temporal Preprocessing
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Month'] = df['Date'].dt.month_name()
    df['Year'] = df['Date'].dt.year
    df['Hour'] = pd.to_datetime(df['Start_Time'], format='%H:%M:%S', errors='coerce').dt.hour
    
    return df

# Load the data
df = load_data()

# ==============================================================================
# 3. Interactive Sidebar Filters
# ==============================================================================
st.sidebar.header("Filter Data")

# Filter 1: Habitat
selected_habitats = st.sidebar.multiselect(
    "Select Ecosystem / Habitat:", 
    options=df['Habitat'].dropna().unique(), 
    default=df['Habitat'].dropna().unique()
)

# Dynamically filter sites based on selected habitat
available_sites = df[df['Habitat'].isin(selected_habitats)]['Admin_Unit_Code'].dropna().unique()

# Filter 2: Admin Unit
selected_sites = st.sidebar.multiselect(
    "Select Administrative Unit:", 
    options=available_sites, 
    default=available_sites
)

# Apply Filters to create the working dataframe
filtered_df = df[
    (df['Habitat'].isin(selected_habitats)) & 
    (df['Admin_Unit_Code'].isin(selected_sites))
]

# ==============================================================================
# 4. Executive KPIs (Top Row)
# ==============================================================================
st.markdown("### High-Level Metrics")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Total Observations", value=f"{len(filtered_df):,}")
with col2:
    st.metric(label="Unique Species", value=f"{filtered_df['Scientific_Name'].nunique():,}")
with col3:
    at_risk = filtered_df[filtered_df['PIF_Watchlist_Status'] == True].shape[0]
    st.metric(label="At-Risk Bird Sightings", value=f"{at_risk:,}")
with col4:
    st.metric(label="Active Observer Count", value=f"{filtered_df['Observer'].nunique():,}")

st.divider()

# ==============================================================================
# 5. EDA Navigation Tabs
# ==============================================================================
# Using tabs to keep the dashboard clean and organized
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🗺️ Spatial & Temporal", 
    "🐦 Species Analysis", 
    "⛅ Environment", 
    "📏 Distance & Behavior", 
    "🧑‍🔬 Observer Trends", 
    "🛡️ Conservation"
])

# --- TAB 1: Spatial & Temporal ---
with tab1:
    st.markdown("#### Spatial & Temporal Trends")
    c1, c2 = st.columns(2)
    
    with c1:
        # Admin Units & Habitat
        fig_admin = px.histogram(filtered_df, x='Admin_Unit_Code', color='Habitat', barmode='group',
                                 title='Observation Frequency by Admin Unit & Habitat',
                                 color_discrete_sequence=px.colors.qualitative.Vivid)
        st.plotly_chart(fig_admin, use_container_width=True)
        
    with c2:
        # Seasonal Trends
        month_order = ['May', 'June', 'July']
        fig_month = px.histogram(filtered_df, x='Month', color='Habitat', barmode='group',
                                 category_orders={"Month": month_order},
                                 title='Seasonal Trends: Observations by Month')
        st.plotly_chart(fig_month, use_container_width=True)

    # Time of Day Correlation
    fig_hour = px.histogram(filtered_df, x='Hour', color='Habitat', barmode='group',
                            title='Observation Time: Bird Activity by Hour of Day (24H)',
                            labels={'Hour': 'Hour of Day'})
    fig_hour.update_layout(xaxis=dict(tickmode='linear', dtick=1))
    st.plotly_chart(fig_hour, use_container_width=True)

# --- TAB 2: Species Analysis ---
with tab2:
    st.markdown("#### Species Diversity & Activity Patterns")
    c1, c2 = st.columns(2)
    
    with c1:
        # Diversity Metrics (Top 10 Plots)
        plot_div = filtered_df.groupby('Plot_Name')['Scientific_Name'].nunique().reset_index()
        plot_div = plot_div.sort_values(by='Scientific_Name', ascending=False).head(10)
        fig_div = px.bar(plot_div, x='Scientific_Name', y='Plot_Name', orientation='h',
                         title='Hotspots: Top 10 Plots by Unique Species',
                         labels={'Scientific_Name': 'Unique Species Count'})
        fig_div.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig_div, use_container_width=True)

    with c2:
        # Activity Patterns (ID Method)
        fig_id = px.histogram(filtered_df, x='ID_Method', color='Habitat', barmode='group',
                              title='Activity Patterns: Identification Method')
        st.plotly_chart(fig_id, use_container_width=True)

    # Sex Ratio
    sex_df = filtered_df[filtered_df['Sex'].isin(['Male', 'Female'])]
    fig_sex = px.histogram(sex_df, x='Habitat', color='Sex', barmode='group',
                           title='Sex Ratio by Habitat (Confirmed Identifications Only)',
                           color_discrete_sequence=['#636EFA', '#EF553B'])
    st.plotly_chart(fig_sex, use_container_width=True)

# --- TAB 3: Environment ---
with tab3:
    st.markdown("#### Environmental Conditions & Correlations")
    c1, c2 = st.columns(2)
    
    with c1:
        # Disturbance Effect
        fig_dist = px.histogram(filtered_df, y='Disturbance', color='Habitat', barmode='group',
                                title='Impact of Environmental Disturbance')
        st.plotly_chart(fig_dist, use_container_width=True)
        
    with c2:
        # Weather Correlation (Density Contour in Plotly)
        fig_weather = px.density_contour(filtered_df, x='Temperature', y='Humidity', color='Habitat',
                                         title='Weather Correlation: Temp vs Humidity',
                                         marginal_x="histogram", marginal_y="histogram")
        st.plotly_chart(fig_weather, use_container_width=True)

# --- TAB 4: Distance & Behavior ---
with tab4:
    st.markdown("#### Observation Distance & Bird Behavior")
    c1, c2 = st.columns(2)
    
    with c1:
        # Distance Analysis
        fig_dist_range = px.histogram(filtered_df, x='Distance', color='Habitat', barmode='group',
                                      title='Distance Analysis: Observation Range')
        st.plotly_chart(fig_dist_range, use_container_width=True)
        
    with c2:
        # Flyover Frequency
        fig_fly = px.histogram(filtered_df, x='Habitat', color='Flyover_Observed', barmode='group',
                               title='Behavior: Flyover Frequency by Habitat')
        st.plotly_chart(fig_fly, use_container_width=True)

# --- TAB 5: Observer Trends ---
with tab5:
    st.markdown("#### Field Staff & Observer Trends")
    c1, c2 = st.columns(2)
    
    with c1:
        # Observer Bias
        obs_counts = filtered_df['Observer'].value_counts().reset_index().head(10)
        obs_counts.columns = ['Observer', 'Count']
        fig_obs = px.bar(obs_counts, x='Count', y='Observer', orientation='h',
                         title='Observer Trends: Top 10 Most Active Field Staff')
        fig_obs.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig_obs, use_container_width=True)
        
    with c2:
        # Visit Patterns
        fig_visit = px.histogram(filtered_df, x='Visit', color='Habitat', barmode='group',
                                 title='Visit Patterns: Repeated Visits to Plots')
        st.plotly_chart(fig_visit, use_container_width=True)

# --- TAB 6: Conservation Insights ---
with tab6:
    st.markdown("#### Conservation Priorities & At-Risk Species")
    c1, c2 = st.columns(2)
    
    with c1:
        # Watchlist Trends
        fig_watch = px.histogram(filtered_df, x='Habitat', color='PIF_Watchlist_Status', barmode='group',
                                 title='Watchlist Trends: At-Risk Species Sightings',
                                 color_discrete_map={True: 'red', False: 'lightgrey'})
        st.plotly_chart(fig_watch, use_container_width=True)
        
    with c2:
        # AOU Code Patterns
        watchlist_df = filtered_df[filtered_df['PIF_Watchlist_Status'] == True]
        aou_counts = watchlist_df['Common_Name'].value_counts().reset_index().head(10)
        aou_counts.columns = ['AOU_Code', 'Count']
        fig_aou = px.bar(aou_counts, x='AOU_Code', y='Count',
                         title='AOU Code Patterns: Top 10 At-Risk Species Codes',
                         color='Count', color_continuous_scale='Reds')
        st.plotly_chart(fig_aou, use_container_width=True)
