---
sidebar_position: 3
---

# Pipeline

The core of the `hctsa`-package is the **pipeline**.

## Initialize

(1) At first, you need to import the **Pipeline**-Class, and additionally pandas:
```python
from hctsa.pipeline.pipeline import Pipeline
import pandas as pd
```

(2a) Then you can initialize your specific pipeline with your own data or csv-file:

```python
data = pd.read_csv('./test_data/testdata.csv', squeeze=True)
pline = Pipeline(series=data)
```

(2b) You can also initialize the pipeline without any data and add the data later:

```python
pline = Pipeline()
pline.load_data_csv(filename='./test_data/testdata.csv')
```

In both ways, the data is set as the core data, all further methods are based on.

## Build

To build up the pipeline, the pipeline-method `add_method` can be used, to add another method into the sequence of methods of the pipeline:

```python
pline.add_method(METHOD_NAME)
```
Where `METHOD_NAME` is the String of the specfic method to be added. There is a number of different methods with individual rules. Hence, just those methods get added into the pipeline, which are allowed dependent on the parent method.

So, sequentially adding a number of methods into the pipeline:

```python
# Example of adding a number of preparation methods:
pline.add_method('point_slope_transformation')
pline.add_method('zscore')
pline.add_method('rolling_mean')
# Adding an output method for visualization:
pline.add_method('sns_line_plot_series')
```

## Run

For running the pipeline and generating an output or result, just use the `run`-method of the pipeline-class:

```python
pline.run()
```