#!/usr/bin/env python3

'''
  Test of an easy example pipeline:
  1. load data
  2. normalize data (zscore)
  3. confidence interval
  4. visualization (line_ci_plot)
'''

from hctsa.pipeline.pipeline import Pipeline
import pandas as pd

d = pd.read_csv('./tests/testdata.csv', squeeze=True)
print(d)

data = d
pline = Pipeline(series=data)

pline.add_method('point_slope_transformation')

pline.add_method('zscore')
pline.add_method('rolling_mean')
pline.add_method('sns_line_plot_series')
# pline.add_method('confidence_interval')
# pline.add_method('sns_line_plot_ci')
# pline.add_method('simple_descriptive_analysis')

pline.run()

