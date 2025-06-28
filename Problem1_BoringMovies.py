import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    df=cinema[(cinema['id']%2 != 0) & (~cinema['description'].str.contains('boring'))]
    return pd.DataFrame(df).sort_values(by=['rating'],ascending=False)