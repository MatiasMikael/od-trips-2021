import pandas as pd
import matplotlib.pyplot as plt
import glob

# Load all CSV files in the current directory
data_files = glob.glob("*.csv")
df = pd.concat((pd.read_csv(file) for file in data_files), ignore_index=True)

# Convert 'Departure' to datetime format
df['Departure'] = pd.to_datetime(df['Departure'], errors='coerce')

# Calculate total trips per day
daily_counts = df.groupby(df['Departure'].dt.date).size()
daily_counts = daily_counts.reset_index()
daily_counts.columns = ['date', 'trip_count']

# Ensure 'date' column is in datetime format
daily_counts['date'] = pd.to_datetime(daily_counts['date'])

# Extract month and year for each day
daily_counts['year_month'] = daily_counts['date'].dt.to_period('M')

# Find the peak day for each month
monthly_peaks = daily_counts.loc[daily_counts.groupby('year_month')['trip_count'].idxmax()]
monthly_peaks = monthly_peaks[['date', 'trip_count', 'year_month']]

# Save the monthly peaks to a CSV file
monthly_peaks.to_csv('monthly_peak_trips.csv', index=False)

# Display the monthly peaks
print("Monthly peaks detected:")
print(monthly_peaks)

# Plot monthly peaks as a bar chart
plt.figure(figsize=(10, 6))
plt.bar(monthly_peaks['year_month'].astype(str), monthly_peaks['trip_count'], color='skyblue')
plt.title('Monthly Peak Bike Trips in Helsinki and Espoo (2021)')
plt.xlabel('Month')
plt.ylabel('Number of Trips')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()