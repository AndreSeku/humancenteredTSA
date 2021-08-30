---
sidebar_position: 1
---

# Introduction

The `hctsa`-package has several functions and modules that we will describe here: 

In general, it is a package for human-centered timeseries analysis:
- **Pipeline** Class for timeseries analysis..
- based on methods for data **Preparation**, **Analysis** and **Visualization**..
- in a **data-centered way**..
- for **human-centered**.. 
- **no-code** or **low-code** data science applications.

## Input and Core Data

The core data, the first input, should be always a time series. All following methods will be executes on this data and manipulate it.

## Pipeline

The Pipeline represents the sequence of methods that will get executed. The user can add specific methods to the pipeline. Every method has its own rules, which methods are allowed next in the sequence. There is a number of possible methods, e.g., for preparation, data analysis or visualization. All methods will get execute on base of the core data.

## Methods

The methods are clustered in different categories:
- preparations
- descriptive analysis
- visualizations
- more to be added..

### Preparation

Prepare the data, e.g., with normalization or data cleaning methods, to get a better data quality for data analysis or visualization methods.

### Descriptive Analysis

Get descriptive data insights.

### Visualization

Get your results visualized. There will be different ways and use of third-party packages for visualization. Furthermore, you can **plot** your results directly or generate an output **file** of your visualization.

## Applications

The idea of the `hctsa`-package is to provide the basis for **low-code** and **no-code** advanced applications. For specific applications, a flask-server with a REST api can get started, but the package and its methods can also be used individualy. 

<!-- 
Run the development server:

```shell
cd my-website

npx docusaurus start
```

Your site starts at `http://localhost:3000`.

Open `docs/intro.md` and edit some lines: the site **reloads automatically** and display your changes.

Generate a new Docusaurus site using the **classic template**:

```shell
npx @docusaurus/init@latest init my-website classic
``` 
-->
