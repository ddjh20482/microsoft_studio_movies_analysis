
# visualization packages
import matplotlib.pyplot as plt
from matplotlib.axes._axes import _log as matplotlib_axes_logger
from matplotlib.ticker import FuncFormatter
import seaborn as sns

# Standard data manipulation packages
import pandas as pd
import numpy as np



def profit(df):

    fig, ax = plt.subplots(figsize=(8,6), facecolor=('#d5d9d7'))

    x = df.profit

    ax.set_facecolor('#f0ffff')

    ax.hist(x, bins=10)
    ax.set_title('Profit Distribution', fontsize=30)
    ax.set_xlabel('Profit in Million Dollar', fontsize=20)
    ax.set_ylabel('Count', fontsize=20)
    ax.tick_params(labelcolor='#0000ff')
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    
    plt.show() 
    
    pass

def budget(budget):

    fig, ax = plt.subplots(figsize=(10,6), facecolor=('#d5d9d7'))

    x = budget.Median
    y = budget.Q25
    z = budget.Q75
    index = budget.index.values

    ax.set_facecolor('#f0ffff')

    ax.bar(index, x, color = '#0000ff')
    ax.plot(index, y, color = '#00ff00', linewidth=4.00)
    ax.plot(index, z, color = '#f97306', linewidth=4.00)
    ax.legend(['Q25', 'Q75', 'median'])
    ax.yaxis.set_major_formatter('${x:1.0f}M')
    ax.set_title('Budget by Profit Range', fontsize=30)
    ax.set_xlabel('Profit Range', fontsize=20)
    ax.set_ylabel('Budget', fontsize=20)
    ax.tick_params(labelcolor='#0000ff')
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    ax.tick_params(axis='x', labelrotation = 15)
    
    plt.show() 
    
    pass

def genre(Genre):

    fig, ax = plt.subplots(figsize=(10,8), facecolor=('#d5d9d7'))

    x = Genre.Median
    y = Genre.Q25
    z = Genre.Q75
    label = Genre.Genre_name

    ax.set_facecolor('#f0ffff')
    
    ax.barh(label, x, height=0.7, color = '#0000ff')
    ax.plot(y, label, color = '#00ff00', linewidth=4.00)
    ax.plot(z, label, color = '#f97306', linewidth=4.00)
    ax.legend(['Q25', 'Q75', 'median'])
    ax.xaxis.set_major_formatter('${x:1.0f}M')
    
    ax.set_title('Profit by Genre', fontsize=30)
    ax.set_xlabel('Profit', fontsize=20)
    ax.set_ylabel('Genre Name', fontsize=20)
    ax.tick_params(labelcolor='#0000ff')
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    
    plt.show() 

    pass

def runtime(runtime):

    fig, ax = plt.subplots(figsize=(8,6), facecolor=('#d5d9d7'))

    x = runtime.Median
    y = runtime.Q25
    z = runtime.Q75
    index = runtime.index.values

    ax.set_facecolor('#f0ffff')

    ax.bar(index, x, color = '#0000ff')
    ax.plot(index, y, color = '#00ff00', linewidth=4.00)
    ax.plot(index, z, color = '#f97306', linewidth=4.00)
    ax.legend(['Q25', 'Q75', 'median'])
    ax.yaxis.set_major_formatter('${x:1.0f}M')
    ax.set_title('Profit by Runtime', fontsize=30)
    ax.set_xlabel('Runtime Ranges in Minutes', fontsize=20)
    ax.set_ylabel('Profit', fontsize=20)
    ax.tick_params(labelcolor='#0000ff')
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    
    plt.show() 

    pass
