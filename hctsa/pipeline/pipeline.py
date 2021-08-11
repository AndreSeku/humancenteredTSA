#!/usr/bin/env python3

'''
Pipeline Class, for building a user defined pipeline for timeseries manipulation and analysis.
'''

import pandas as pd
import yaml
import hctsa.pipeline.methods as methods

class Pipeline():
  # Main Pipeline Array
  main_pipeline = []

  # Main Data Variable
  core_data = []

  # DICTIONARIE for specific pipeline rules, loaded from method_rules.yml file.
  method_rules = []
  
  def __init__(self, series: pd.Series) -> None:
    '''
      Initialization of a new Pipeline Object.
      @param series: pd.Series
    '''
    self.core_data = series
    # TODO add try/catch block
    with open('hctsa/pipeline/method_rules.yml', 'r') as file:
      self.method_rules = yaml.safe_load(file)
    return

  def load_data_csv(self, filename: str) -> None:
    '''
      Loads pd.Series data as core_data from filename.
      @param filename: str
    '''
    self.core_data = pd.read_csv(path=filename, squeeze=True)
    return

  def add_method(self, add_function: str, position: int = -1) -> bool:
    '''
      Adds a new method into the pipeline
      1) Check actual pipeline
      2) Check if method can be added at defined position or at the end (-1), regarding to the pipeline-rules (e.g. visualisation is the last layer/method)
        -> check if method is in method_rules.yml for specific "nachfolger function"
      3) if possible, add method to method-pipeline-array
      Return boolean - success or error msg
      @param add_function: str
      @param position: int
    '''
    if(len(self.main_pipeline)) > 0:
      last_func = self.main_pipeline[-1]
      if(add_function in self.method_rules['methods'][last_func]):
        self.main_pipeline.append(add_function)
      else:
        print('error: function cannot be added: ', add_function)
        return False
    else:
      if(add_function in self.method_rules['start']):
        self.main_pipeline.append(add_function)
      else:
        print('error: function cannot be added: ', add_function)
        return False
    return True

  def del_method():
    ...

  def add_series(self, series: pd.Series) -> bool:
    ...
    return True

  def run(self) -> pd.Series:
    '''
      Returns the result of the Pipeline.
      Method for running the pipeline. Every method that was added into the pipeline will get executed in a sequential way.
    '''
    _data = self.core_data
    print('PIPELINE: ', self.main_pipeline)
    for method in self.main_pipeline:
      print('DOING: ', method)
      _data = getattr(methods, method)(_data)
      print(_data)
    return _data