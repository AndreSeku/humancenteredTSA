#!/usr/bin/env python3

TESTCASE = 0

from hctsa.pipeline.pipeline import Pipeline
import pandas as pd

# Load Data:
data = pd.read_csv('./test_data/testdata.csv', squeeze=True)

'''
  Example Case 0
  Test of an easy example pipeline:
  1. load data
  2. normalize data (zscore)
  3. confidence interval
  4. visualization (line_ci_plot)
'''

if TESTCASE == 0:
  pline = Pipeline(series=data)
  pline.add_method('point_slope_transformation')
  pline.add_method('zscore')
  pline.add_method('rolling_mean')
  # pline.add_method('sns_line_plot_series')
  pline.add_method('confidence_interval')
  pline.add_method('sns_line_plot_ci')
  pline.add_method('simple_descriptive_analysis')
  pline.run()

'''
  Example Case 1
  Test of an easy example pipeline:
  1. load data
  2. add data
  3. visualization (line_ci_plot)
'''

if TESTCASE == 1:
  pline = Pipeline(series=data)
  pline.add_series(series=data, merge_method='merge_sum')
  pline.add_series(series=data, merge_method='merge_subtract')
  pline.add_series(series=data, merge_method='merge_multiply')
  pline.add_series(series=data, merge_method='merge_divide')
  pline.add_series(series=data, merge_method='merge_mean')
  pline.add_method('sns_line_plot_series')
  # pline.add_series(series=data, merge_method='corr')
  pline.run()

