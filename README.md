# jpjwidgets
Jupyter Python+Javascript Widgets: link javascript variables with Kernel Python variables

## If you want

* to copy browser's javascript variables to IPython kernel variable
* to set some browser's variable based upon IPython kernal variable

## Examples

* get the current calling url in a python variable
* get the browser Geo Position (if the user accepts) in a Python variable

## Architecture

* Javascript is simply generated thanks to the _repr_javascript_ capability of IPython Notebook
   * this allows to set whatever javascript variable from a notebook programmatically
* Writing back javascript values to the notebook via the HTTP server
   * this allows to set whatever python IPython kernel variable with javascript Browser values

## Install

* **Base Framework**: Jupyter Lab + Jupyter ipywidgets + Jupyter Server proxy
* **Copy**: notebook and python file in a Jupyter Lab directory
* **Run**: The notebook

## Documentation

* Read the notebook notes
* read the python file comments if you want to dig the HTTP server operations
