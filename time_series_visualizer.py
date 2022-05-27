import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col =['date']) #

#df.set_index(['date'],inplace=True)

# Clean data
df = df[(df['value'] >= (df['value'].quantile(0.025))) & (df['value'] <= (df['value'].quantile(0.975))) ]


def draw_line_plot():
    
    #Create a draw_line_plot function that uses Matplotlib to draw a line chart similar to "examples/Figure_1.png". 
    # The title should be "Daily freeCodeCamp Forum Page Views 5/2016-12/2019". 
    # The label on the x axis should be "Date" and the label on the y axis should be "Page Views".    
    
    fig = df.plot(figsize=(15, 6))

    plt.title( 'Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    fig = fig.figure

    #plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
    df_bar['month'] = pd.Categorical(df_bar.index.strftime('%B'), categories=month, ordered=True)
    df_bar = pd.pivot_table(data=df_bar, index=df_bar.index.year, columns='month', values='value')

    #Create a draw_bar_plot function that draws a bar chart similar to "examples/Figure_2.png". 
    # It should show average daily page views for each month grouped by year. 
    # The legend should show month labels and have a title of "Months". 
    # On the chart, the label on the x axis should be "Years" and the label on the y axis should be "Average Page Views".

    fig = df_bar.plot.bar(figsize=(10, 6))

    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title = 'Months')

    fig = fig.figure

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    

    # Draw box plots (using Seaborn)
    #Create a draw_box_plot function that uses Seaborn to draw two adjacent box plots similar to "examples/Figure_3.png". 
    # These box plots should show how the values are distributed within a given year or month and how it compares over time. 
    # The title of the first chart should be "Year-wise Box Plot (Trend)" and the title of the second chart should be "Month-wise Box Plot (Seasonality)". 
    # Make sure the month labels on bottom start at "Jan" and the x and y axis are labeled correctly. 
    # The boilerplate includes commands to prepare the data.
    
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    fig,axes =  plt.subplots(1,2, figsize=(18,6))

    sns.boxplot(ax=axes[0], data = df_box,  x = df_box['year'], y = df_box['value'])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    sns.boxplot(ax=axes[1], data = df_box,  x = df_box['month'], y = df_box['value'], order = months)
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_ylabel('Page Views')
    axes[1].set_xlabel('Month')





    fig = fig.figure

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
