# Bike Trip Data Analysis Project

This project provides tools for analyzing and visualizing Helsinki and Espoo city bike trip data. The project includes scripts to analyze daily bike trips and identify the peak day for each month, with clear visualizations.

# Table of Contents
1. Requirements
2. Installation
3. Usage
4. Output
5. License

# 1. Requirements

* Python 3.7 or higher
* Required Python packages (see requirements.txt)

# 2. Installation

1. Clone or download this repository to your local machine.
2. Install the required packages by running the following command:

```bash
pip install -r requirements.txt
```

# 3. Usage

This project includes the following scripts:

- Analyze daily bike trip data:

  ```bash
  python analyze_bike_data.py
  ```
  
  This script loads, processes, and visualizes daily bike trips in Helsinki and Espoo, displaying trends over time.

- Detect monthly peak bike trip days:

  ```bash
  python detect_monthly_peaks.py
  ```

  This script identifies the peak bike trip day for each month and saves the results in `monthly_peak_trips.csv`.

# 4. Output

### Daily Bike Trips in Helsinki and Espoo (2021)
   - This line chart illustrates the number of daily bike trips in Helsinki and Espoo throughout 2021. A clear seasonal trend is evident, with peak activity during the summer months.

### Monthly Peak Bike Trips in Helsinki and Espoo (2021)
   - This bar chart shows the peak day of bike trips for each month in 2021, along with the corresponding number of trips. Each bar represents the day with the highest bike usage in its respective month.

### Bike Usage by Hour and Weekday
   - This heatmap visualizes bike usage by hour and day of the week. Darker shades indicate higher usage levels. The chart reveals that bike usage tends to peak in the afternoon on weekdays, particularly after work hours.
   - 
# 5. Data Source and License

The data used in this project is sourced from Helsinki Region Transport's (HSL) open data portal.

- *Data source* `https://www.avoindata.fi/data/fi/dataset/helsingin-ja-espoon-kaupunkipyorilla-ajatut-matkat`

# License

This work is licensed under the MIT License, but the data used in this project is provided by Helsinki Region Transport (HSL) and published under the Creative Commons Attribution 4.0 International License: `https://creativecommons.org/licenses/by/4.0/`.
