#!/usr/bin/env python3

'''
Method mapping file, needed for the string to method mapping functionality.
'''

# Imports
from ..preparation.normalization import *
from ..descriptive.univariate import *

# Preparations.Normalizations
def prep_norm_zscore(df: DataFrame) -> DataFrame:
  return zscore(df)

def prep_norm_standard(df: DataFrame) -> DataFrame:
  return standard(df)

# Descriptive.Univariate
def descr_uni_rolling_mean(series: Series) -> Series:
  return rolling_mean(series)

def descr_uni_rolling_std(series: Series) -> Series:
  return rolling_std(series)

def descr_uni_confidence_interval(series: Series) -> DataFrame:
  return confidence_interval(series)

def descr_uni_value_distribution(series: Series) -> Series:
  return value_distribution(series)

def descr_uni_simple_descriptive_analysis(series: Series) -> dict:
  return simple_descriptive_analysis(series)