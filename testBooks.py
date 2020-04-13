import pandas as pd

file = '/home/srujanee/projects/api/book.csv'
def csv_fn(file):
    df = pd.read_csv(file)
    pd.options.display.max_columns = len(df.columns)
    print(df)
