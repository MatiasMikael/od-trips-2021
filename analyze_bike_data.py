import pandas as pd
import matplotlib.pyplot as plt
import glob

# Find all CSV files in the current directory
data_files = glob.glob("*.csv")

# Load and concatenate all CSV files into a single DataFrame
df = pd.concat((pd.read_csv(file) for file in data_files), ignore_index=True)

# Convert 'Departure' and 'Return' columns to datetime format, automatically inferring format
df['Departure'] = pd.to_datetime(df['Departure'], errors='coerce')
df['Return'] = pd.to_datetime(df['Return'], errors='coerce')

# Add 'weekday' and 'start_hour' columns for analysis
df['weekday'] = df['Departure'].dt.day_name()
df['start_hour'] = df['Departure'].dt.hour

# Calculate total trips per day
daily_counts = df.groupby(df['Departure'].dt.date).size()

# Plot daily trip counts
plt.figure(figsize=(12, 6))
daily_counts.plot(kind='line', color='blue', linewidth=1)
plt.title('Daily Bike Trips in Helsinki and Espoo (2021)')
plt.xlabel('Date')
plt.ylabel('Number of Trips')
plt.grid(True)
plt.show()

# Calculate trips by weekday and hour
hourly_counts = df.groupby(['weekday', 'start_hour']).size().unstack().fillna(0)

# Plot heatmap of hourly usage by weekday
plt.figure(figsize=(10, 6))
plt.imshow(hourly_counts, aspect='auto', cmap='Blues')
plt.colorbar(label='Number of Trips')
plt.xticks(range(0, 24), labels=range(0, 24))
plt.yticks(range(7), labels=hourly_counts.index)
plt.xlabel('Hour of the Day')
plt.ylabel('Day of the Week')
plt.title('Bike Usage by Hour and Weekday')
plt.show()