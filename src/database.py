import sqlite3
import pandas as pd


con = sqlite3.connect('database.db')
cur = con.cursor()




df = pd.read_csv(r'C:\Users\MARCUS VINICIUS\Documents\analisador-sentimento\data\IMDB Dataset.csv')


df.drop(columns=["sentiment"], inplace=True)


df["id"] = range(1, len(df) + 1)
df["date"] = pd.Timestamp.now().normalize()
df["origin"] = "IMDB Dataset"
print(df.head())



df.to_sql('reviews', con, if_exists='replace', index=False)