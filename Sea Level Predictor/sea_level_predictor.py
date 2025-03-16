import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    data = pd.read_csv("epa-sea-level.csv")
    print(data)

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], label="Data Points", color='blue', alpha=0.7)


    # Create first line of best fit
    slope, intercept, _, _, _ = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    sea_levels = slope * years_extended + intercept
    plt.plot(years_extended, sea_levels, label="Best Fit Line (All Data)", color='red')


    # Create second line of best fit
    recent_data = data[data['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    sea_levels_recent = slope_recent * years_recent + intercept_recent
    plt.plot(years_recent, sea_levels_recent, label="Best Fit Line (2000 Onward)", color='green')


    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()