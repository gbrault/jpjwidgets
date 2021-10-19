# Communication between the front-end and back-end in a Jupyter Notebook

ipybus is an ipywidgets [see](https://github.com/gbrault/ipybus) enabling communication between frontend and backend

  * when creating an ipybus.Base() object, you can set a variable name which will be accessible in the window spacename
  * this frontend variable can be used in javascript to set a new value and send it to the backend
  * The notebook developper can then create scripts in the frontend which send values to the backend

See the [wired-elements-ipybus](wired-elements-ipybus.ipynb) Notebook for more insights
