import pandas as pd
import sqlite3
import pandasql
import string
import statistics
import numpy as np
from pandas.api.types import CategoricalDtype

# https://www.codegrepper.com/code-examples/python/how+to+remove+periods+in+a+datafrane+pandas
def remove_punctuations(text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
    return text

def profit(df, set_year):
    
    df = df.drop(columns=['domestic_gross'])
    
    # last 4 position of release date is saved as year
    df['year'] = [int(i[-4:]) for i in df.release_date]
    df.sort_values(by = 'year', inplace=True)
    df = df.loc[df.year >= set_year]
    
    # cleaning object value to have int value
    df['budget'] = df.production_budget.str.strip("$")
    df['budget'].replace(',','', regex=True, inplace=True)
    df['budget'] = df.budget.astype(int)
    df['budget'] = round(df['budget'] / 1000000, 2)
    
    # cleaning object value to have int value
    df['w_gross'] = df.worldwide_gross.str.strip("$")
    df['w_gross'].replace(',','', regex=True, inplace=True)
    df['w_gross'] = df.w_gross.astype(float)
    
    # calculate profit and divide by 1 million to have clearer view in the visualization
    # zero world gross is removed
    # select rows with higher profit than the set profit
    df['profit'] = round((df['w_gross'] - df['budget']*1000000) / 1000000, 2)
    df.drop(df[df.w_gross == 0].index, inplace=True)
    df.sort_values(by = 'profit', inplace=True, ascending=False)
    #df = df.loc[df.profit > set_profit]
    df = df.drop(columns=['id', 'release_date'])
    
    return df

def budget(df):
    
    df.loc[ df['profit'] <=  0,                             'profit_range'] = 'Less than Zero'
    df.loc[(df['profit'] >   0  )  & (df['profit'] <= 100), 'profit_range'] = 'Zero to $100M'
    df.loc[(df['profit'] >   100)  & (df['profit'] <= 200), 'profit_range'] = '$100M to \$200M'
    df.loc[(df['profit'] >   200)  & (df['profit'] <= 300), 'profit_range'] = '$200M to \$300M'
    df.loc[ df['profit'] >   300,                           'profit_range'] = 'More than $300M'
    
    df.sort_values(by = 'profit', inplace=True, ascending=False)
    
    budget = pd.DataFrame(
        {
            'Median': df.groupby('profit_range').median().budget,
            'Q25': df.groupby('profit_range').quantile(.25).budget,
            'Q75': df.groupby('profit_range').quantile(.75).budget
        }, index = df.groupby('profit_range').median().budget.index.values.tolist()
        )
    budget.reset_index(inplace=True)
    order = CategoricalDtype(['Less than Zero', 
                              'Zero to $100M', 
                              '$100M to \$200M', 
                              '$200M to \$300M', 
                              'More than $300M'], ordered = True)
    budget['index'] = budget['index'].astype(order)
    budget.sort_values('index', inplace=True)
    budget.set_index('index', inplace=True)
    
    return budget

def genre(df):

    # remove unnecessary columns
    df = df.drop(columns=[
        'Unnamed: 0', 
        'id', 
        'original_title', 
        'original_language', 
        'popularity', 
        'vote_average', 
        'vote_count'])
    
    # remove duplicate
    df = df.drop_duplicates()

    return df

def runtime(con):

    # select title and runtime
    df = pd.read_sql("""
        SELECT movie_id, primary_title, start_year, runtime_minutes 
        FROM movie_basics
        WHERE runtime_minutes IS NOT NULL
        ;
        """, con)

    return df


# clean element in genre id column from genre data
# then count genre ids
def get_count(number, df):
    genre = 0
    for i in df.genre_ids:
        for jn in i[1:-1].split():
            if jn == number:
                genre += 1
            else:
                pass
    return genre

def get_median(number, df):
    med = []
    x = 0
    for i in df.genre_ids:
        for jn in i[1:-1].split():
            if jn == number:
                med.append(df.profit.iloc[x])
            else:
                pass
        x += 1
    return np.percentile(med, 50)

def get_q25(number, df):
    q25 = []
    x = 0
    for i in df.genre_ids:
        for jn in i[1:-1].split():
            if jn == number:
                q25.append(df.profit.iloc[x])
            else:
                pass
        x += 1
    return np.percentile(q25, 25)

def get_q75(number, df):
    q75 = []
    x = 0
    for i in df.genre_ids:
        for jn in i[1:-1].split():
            if jn == number:
                q75.append(df.profit.iloc[x])
            else:
                pass
        x += 1
    return np.percentile(q75, 75)


def genre_count(df):
    
    # list of genres with designated genre ids
    Genre = {
    '28': 'Action',
    '12': 'Adventure',
    '16': 'Animation',
    '35': 'Comedy',
    '80': 'Crime',
    '99': 'Documentary',
    '18': 'Drama',
    '10751': 'Family',
    '14': 'Fantasy',
    '36': 'History',
    '27': 'Horror',
    '10402': 'Music',
    '9648': 'Mystery',
    '10749': 'Romance',
    '878': 'SciFi',
    '10770': 'TV_Movie',
    '53': 'Thriller',
    '10752': 'War',
    '37': 'Western'
    }
    # another step of cleaning genre column elements
    df.genre_ids.replace(",",'', regex=True, inplace=True)
    
    # start with blank
    Genre_name = []
    Genre_count = []
    Genre_median = []
    Genre_q25 = []
    Genre_q75 = []
    
    # save names in Genre_name in the order
    # save count in Genre_count in the order
    for key, value in Genre.items():
        Genre_name.append(value)
        Genre_count.append(get_count(key, df))
        Genre_median.append(get_median(key, df))
        Genre_q25.append(get_q25(key, df))
        Genre_q75.append(get_q75(key, df))
    
    # combine two lists and set as dataframe
    Genre = pd.DataFrame(
        {
            'Genre_name': Genre_name,
            'Genre_count': Genre_count,
            'Median': Genre_median,
            'Q25': Genre_q25,
            'Q75': Genre_q75
        }
        )
    
    # sort the dataframe for the readable visualization
    Genre.sort_values(by = 'Median', inplace=True)
    
    return Genre

def runtime_range(df_runtime):

    df_runtime.loc[ df_runtime['runtime_minutes'] <=60, 'rt_range'] = 'Less than 60'
    df_runtime.loc[(df_runtime['runtime_minutes'] > 60) 
                   & (df_runtime['runtime_minutes'] <= 80), 'rt_range'] = '60 to 80'
    df_runtime.loc[(df_runtime['runtime_minutes'] > 80) 
                   & (df_runtime['runtime_minutes'] <= 100), 'rt_range'] = '80 to 100'
    df_runtime.loc[(df_runtime['runtime_minutes'] > 100) 
                   & (df_runtime['runtime_minutes'] <= 120), 'rt_range'] = '100 to 120'
    df_runtime.loc[ df_runtime['runtime_minutes'] > 120, 'rt_range'] = 'over 120'

    df_runtime.sort_values(by = 'profit', inplace=True, ascending=False)

    runtime = pd.DataFrame(
        {
            'Median': df_runtime.groupby('rt_range').median().profit,
            'Q25': df_runtime.groupby('rt_range').quantile(.25).profit,
            'Q75': df_runtime.groupby('rt_range').quantile(.75).profit
        }, index = df_runtime.groupby('rt_range').median().profit.index.values.tolist()
        )

    runtime.reset_index(inplace=True)

    order = CategoricalDtype(['Less than 60', 
                              '60 to 80', 
                              '80 to 100', 
                              '100 to 120', 
                              'over 120'], ordered = True)
    runtime['index'] = runtime['index'].astype(order)
    runtime.sort_values('index', inplace=True)
    runtime.set_index('index', inplace=True)

    return runtime

# cleaning each movie titles
def movie_name_clean(series):

    series = series.apply(lambda x: x.lower())
    series = series.apply(remove_punctuations)
    series.replace(' ','', regex=True, inplace=True)
    
    return series