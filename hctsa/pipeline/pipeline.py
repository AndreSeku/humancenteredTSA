#!/usr/bin/env python3

'''
Pipeline Class, for building a user defined pipeline for timeseries manipulation and analysis.
'''

import pandas as pd
import hctsa.pipeline.methods as methods

class Pipeline():
  main_pipeline = []
  # __preparations__ = []
  # __descriptive__ = []
  # __non_descriptive__ = []
  # __visualize__ = [] # "Output Layer"

  # Main Data Variable
  core_data = []

  # DICTIONARIES - TODO load from config.ini file ... (config fuer erlaubtenachfolgerfunctionen)
  start_methods = ['zscore','standard',...]
  method_rules = {'zscore': ['rolling_mean', 'rolling_std', 'confidence_interval', 'value_distribution', 'simple_descriptive_analysis'], 
                  'standard': ['rolling_mean', 'rolling_std', 'confidence_interval', 'value_distribution', 'simple_descriptive_analysis'],
                  'rolling_mean': ['confidence_interval', 'value_distribution', 'simple_descriptive_analysis'],
                  'rolling_std': ['confidence_interval', 'value_distribution', 'simple_descriptive_analysis'],                  
                  'value_distribution': [],
                  'confidence_interval': [],
                  'simple_descriptive_analysis': []
                  }
  # prep_methods = {}
  # descr_methods = {}
  # ndescr_methods = {}
  # vis_methods = {}
  
  def __init__(self, series: pd.Series) -> None:
    self.core_data = series
    return

  def load_data_csv(self, filename: str) -> None:
    '''
      Loads pd.Series data as core_data from filename.
      @param filename: str
    '''
    self.core_data =pd.read_csv(path=filename)
    return

  def add_method(self, add_function: str, position: int = -1) -> bool:
    '''
      TODO
    '''
    ## 1) Check actual pipeline
    ## 2) Check if method can be added at defined position or at the end (-1), regarding to the pipeline-rules (e.g. visualisation is the last layer/method)
    ##  -> check if method is in config.ini for specific "vorgaenger function" ...
    ## 3) if possible, add method to specific method-pipeline-array
    ## 4) return success or error msg
    if(len(self.main_pipeline)) > 0:
      last_func = self.main_pipeline[-1]
      if(add_function in self.method_rules[last_func]):
        self.main_pipeline.append(add_function)
      else:
        print('error: function cannot be added: ', add_function)
        return False
    else:
      if(add_function in self.start_methods):
        self.main_pipeline.append(add_function)
      else:
        print('error: function cannot be added: ', add_function)
        return False
    return True

  def add_series(self, series: pd.Series) -> bool:
    ...
    return True

  def run(self) -> pd.Series:
    _data = self.core_data
    print('PIPELINE: ', self.main_pipeline)
    for method in self.main_pipeline:
      print('DOING: ', method)
      _data = getattr(methods, method)(_data)
      print(_data)
    return ...