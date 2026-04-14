# Convert full country names into 2 letter abbreviations using case match
country = str(input("Name your country:"))
match country:
    case "United States of America":
        print("US")
    case "India":
        print("IN")
    case "Germany":
        print("DE")
    case _:
        print("Unknown")