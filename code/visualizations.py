
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

def budget(df):

    fig, ax = plt.subplots(figsize=(8,6), facecolor=('#d5d9d7'))

    x = df.budget.loc[df.budget > 0] / 1000000

    ax.set_facecolor('#f0ffff')

    ax.hist(x, bins=17, color = '#0343df')
    ax.set_title('Budget Distribution', fontsize=30)
    ax.set_xlabel('Budget in Million Dollar', fontsize=20)
    ax.set_ylabel('Count', fontsize=20)
    ax.tick_params(labelcolor='#0000ff')
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    
    plt.show() 
    
    pass

def genre(Genre):

    fig, ax = plt.subplots(figsize=(10,8), facecolor=('#d5d9d7'))

    y = Genre.Genre_name
    x = Genre.Genre_count

    ax.set_facecolor('#eafff5')

    ax.barh(y, x, height=0.7, color = 'g')
    ax.set_title('Genre Popularity', fontsize=30)
    ax.set_xlabel('Count', fontsize=20)
    ax.set_ylabel('Genre Name', fontsize=20)
    ax.tick_params(labelcolor='#0000ff')
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    
    plt.show() 

    pass

def runtime(df):

    fig, ax = plt.subplots(figsize=(8,6), facecolor=('#d5d9d7'))

    x = df.runtime_minutes

    ax.set_facecolor('#eafff5')

    ax.hist(x, bins=21, color = 'c')
    ax.set_title('Movie Runtime Distribution', fontsize=30)
    ax.set_xlabel('Movie Length in Minutes', fontsize=20)
    ax.set_ylabel('Count', fontsize=20)
    ax.tick_params(labelcolor='#0000ff')
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    
    plt.show() 

    pass
