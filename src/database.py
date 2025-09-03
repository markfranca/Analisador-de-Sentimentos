import sqlite3
import pandas as pd


con = sqlite3.connect('database.db')
cur = con.cursor()


df = pd.read_csv('IMDB Dataset.csv')
df.to_sql('reviews', con, if_exists='replace', index=False)