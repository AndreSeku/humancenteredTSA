#!/usr/bin/env python3

'''
Methods for univariate descriptive timeseries analysis.
'''

import pandas as pd
from pandas import Series, DataFrame

def simple_descriptive_analysis(series: Series) -> dict:
  '''
    Returns dictionary with TimeSeries specific features.
    This method generates a simple descriptive analysis of the timeseris data.
    TODO ...
    @param series: pd.Series
   
  '''
  result = {
    'min': series.min(),
    'mean': series.mean(),
    'median': series.median(),
    'max': series.max(),
    'std': series.std(),
    'var': series.var(),
    'largest': series.nlargest(),
    'smallest': series.nsmallest()
  }
  return result

def rolling_mean(series: Series, window=5) -> Series:
  '''
    Returns a Series with the rolling mean.
    @param series: pd.Series
  '''
  return series.rolling(window, min_periods=1).mean()

def confidence_interval(series: Series) -> DataFrame:
  '''
    Returns a DataFrame with three columns, the upper and lower bound and the rolling mean for the confidence interval of the input timeseries.
    @param series: pd.Series
  '''
  # TODO
  ...

def value_distribution(series: Series, bins=-1) -> Series:
  '''
    Returns a DataFrame with the value distribution of the input timeseries (rounded).
    @param series: pd.Series
  '''
  if bins==-1:
    return series.round().value_counts().sort_index()
  else:
    return series.round().value_counts(bins=bins).sort_index()


####### TEST
if __name__ == '__main__':
  test_df = pd.Series(data=[0.1,1.2,2.5,3.7,4.5,5,6,3,2314,3,12,213,23,3,3,1])
  print(value_distribution(test_df))
  # print(simple_descriptive_analysis(test_df))
  # print(rolling_mean(test_df))