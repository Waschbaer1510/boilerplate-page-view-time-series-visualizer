import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',parse_dates=['date'])
df = df.set_index('date')
df["value"]=df["value"].astype("int32")
#df.info()
#print(df.describe())

# Clean data
df = df[(df.value<=df.value.quantile(0.975))&(df.value>=df.value.quantile(0.025))]
#df2 = df[(df.value>df.value.quantile(0.975))|(df.value<df.value.quantile(0.025))]
#rint(df.head())
#print(df2.head())

df.info()

def draw_line_plot():
    
    # Draw line plot
    fig, ax =plt.subplots(figsize=(20,5))

    #Create figure and axis
    #ax.plot(df.index,df["value"], marker='o', linestyle='-', color='b', label="Test Trend")
    ax.plot(df.index,df["value"], linestyle='-', color='r', label="Test Trend")

    # labels and title
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar =  df.groupby(df.index.to_period('M')).sum()
    #print(df_bar)
    # Draw bar plot
    fig, ax =plt.subplots(figsize=(20,5))

    #ax.plot(df.index,df["value"], marker='o', linestyle='-', color='b', label="Test Trend")
    ax.bar(df_bar.index,df_bar["value"])

    # labels and title
    #ax.set_xlabel("Date")
    #ax.set_ylabel("Page Views")
    #ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")



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





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

#draw_line_plot()
draw_bar_plot()