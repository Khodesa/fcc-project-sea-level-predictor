import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    line = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    a, b = line.slope, line.intercept
    x = range(1880, 2051, 1)
    y = a * x + b
    plt.plot(x, y)

    # Create second line of best fit
    df_2k = df[df['Year'] >= 2000]
    line = linregress(df_2k['Year'], df_2k['CSIRO Adjusted Sea Level'])
    a, b = line.slope, line.intercept
    x = range(2000, 2051, 1)
    y = a * x + b
    plt.plot(x, y)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()