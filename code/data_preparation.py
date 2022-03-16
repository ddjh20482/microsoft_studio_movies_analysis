import pandas as pd
import sqlite3
import pandasql
import string

# https://www.codegrepper.com/code-examples/python/how+to+remove+periods+in+a+datafrane+pandas
def remove_punctuations(text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
    return text

def profit(df, set_year, set_profit):
    
    df = df.drop(columns=['domestic_gross'])
    
    df['year'] = [int(i[-4:]) for i in df.release_date]
    df.sort_values(by = 'year', inplace=True)
    df = df.loc[df.year >= set_year]
    
    df['budget'] = df.production_budget.str.strip("$")
    df['budget'].replace(',','', regex=True, inplace=True)
    df['budget'] = df.budget.astype(int)

    df['w_gross'] = df.worldwide_gross.str.strip("$")
    df['w_gross'].replace(',','', regex=True, inplace=True)
    df['w_gross'] = df.w_gross.astype(float)
    
    df['profit'] = round((df['w_gross'] - df['budget']) / 1000000, 2)
    df.drop(df[df.worldwide_gross == 0].index, inplace=True)
    df.sort_values(by = 'profit', inplace=True, ascending=False)
    df = df.loc[df.profit > set_profit]
    df = df.drop(columns=['id', 'release_date'])    
    
    return df

def genre(df):

    df = df.drop(columns=[
        'Unnamed: 0', 
        'id', 
        'original_title', 
        'original_language', 
        'popularity', 
        'vote_average', 
        'vote_count'])
    
    df = df.drop_duplicates()

    return df

def runtime(con):

    df = pd.read_sql("""
        SELECT movie_id, primary_title, start_year, runtime_minutes 
        FROM movie_basics
        WHERE runtime_minutes IS NOT NULL
        ;
        """, con)

    return df


def get_count(number, df):
    genre = 0
    for i in df.genre_ids:
        for jn in i[1:-1].split():
            if jn == number:
                genre += 1
            else:
                pass
    return genre

def genre_count(df):
    
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
    df.genre_ids.replace(",",'', regex=True, inplace=True)
    
    Genre_name = []
    Genre_count = []
    
    for key, value in Genre.items():
        Genre_name.append(value)
        Genre_count.append(get_count(key, df))

    Genre = pd.DataFrame(
        {
            'Genre_name': Genre_name,
            'Genre_count': Genre_count
        }
        )

    Genre.sort_values(by = 'Genre_count', inplace=True)
    
    return Genre

def movie_name_clean(series):

    series = series.apply(lambda x: x.lower())
    series = series.apply(remove_punctuations)
    series.replace(' ','', regex=True, inplace=True)
    
    return series