import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    df=my_numbers.groupby('num').size().reset_index(name='count')
    df=df[df['count']==1].max()
    return pd.DataFrame({'num':[df['num']]})