'''
Methods for normalization of timeseries data.
'''

def standard(df):
  '''
    Normalization of the TimeSeries data.
    Input: pd.DataFrame
    Output: Normalized pd.DataFrame
    _x = (x - min) / (max - min)
  '''
  for col in list(df.columns):
    df[col] = (df[col] - df[col].min()) / (df[col].max - df[col].min)
  return df
  

def zscore(df):
  '''
    Z-score normalization of the TimeSeries data.
    Input: pd.DataFramee
    Output: Z-Score normalized pd.DataFrame
    _x = (x - mean) / std
  '''
  for col in list(df.columns):
    df[col] = (df[col] - df[col].mean())/df[col].std(ddof=0)
  return df
  