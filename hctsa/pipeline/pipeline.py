#!/usr/bin/env python3

'''
Pipeline Class, for building a user defined pipeline for timeseries manipulation and analysis.
'''

import pandas as pd

class Pipeline(...):
  __preparations__ = []
  
  def __init__(self, series: pd.Series) -> None:
    ...

  def add_to_pipeline(self, function: str) -> bool:
    ...
    return True

  def add_series(self, series: pd.Series) -> bool:
    ...
    return True

  def run(self) -> pd.Series:
    ...
    return ...