# Jupyter compare_view

![bannerFINAL](https://user-images.githubusercontent.com/44469195/179508322-ea10e22a-6dfb-47f4-8fbb-d5ce724f0127.png)

[![JupyterLight](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://octoframes.github.io/jupyter_compare_view)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Octoframes/jupyter_compare_view/HEAD?labpath=example_notebook.ipynb)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Octoframes/jupyter_compare_view/blob/main/example_notebook.ipynb)
[![PyPI version](https://badge.fury.io/py/jupyter_compare_view.svg)](https://badge.fury.io/py/jupyter_compare_view)
[![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/Octoframes/jupyter_compare_view/blob/main/LICENSE)


Blend between multiple images using a cell magic in JupyterLab using [compare_view](https://github.com/Octoframes/compare_view).   
*This project was called jupyter-splitview before.*  


## Installation
```py
pip install jupyter_compare_view
```
## Example
```py
import jupyter_compare_view
```

```py
%%compare  
from skimage import data
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

img = data.chelsea()
grayscale_img = rgb2gray(img)

plt.imshow(img)
plt.axis("off")
plt.show()

plt.imshow(grayscale_img, cmap="gray")
plt.axis("off")
plt.show()
```

<img src="https://user-images.githubusercontent.com/44469195/179499138-65160434-11e1-4358-8e25-5b26ba9ebf4a.png" style="width: 400px;"/>

Another example:
```py
%%compare  --config '{"start_mode": "horizontal","start_slider_pos": 0.73}'

plt.imshow(img)
plt.axis("off")
plt.show()

plt.imshow(grayscale_img, cmap="gray")
plt.axis("off")
plt.show()
```
<img src="https://user-images.githubusercontent.com/44469195/179499350-94244408-cabf-4945-affc-fd0444d53555.png" style="width: 400px;"/>


The split view widget is still responsive after closing and reopening the notebook without running the cell again.

## Notebook arguments
(Might still change in future)
* `--config '{"start_mode": "horizontal"}'` will init the compare-view in horizontal slider mode.
* `--config '{"circle_size": 30}'`  the circle size is now 30 pixel in circle mode.
* `--config '{"show_slider": false}'` will hide the slider bar.
* `--config '{"start_slider_pos": 0.73}'` will set the slider start position to 73%. 

    * *Removed in 0.1.1: `--position 73%` will no longer the slider start position to 73%.*
* `--config '{"start_mode": "horizontal","start_slider_pos": 0.73}'` will both set the start mode to horizontal and set the slider position
* `--height 220` will set the height to 220 pixel. 
* When `--height`is not provided, the default height of the widget is 300 pixel.
* `--height auto` will set the height by the value of the first image's resolution in vertical direction.
* The widget's width will always be adjusted automatically. 

## Notebook formatting
Formatting with black can be done this way: 
1. `pip install 'black[jupyter]'`
2. `black --python-cell-magics compare compare_view_magic.ipynb`


## Developer Installation

1. `git clone --recurse https://github.com/Octoframes/jupyter_compare_view`
(Note: In case that the repo was already cloned e.g. with the GitHub Desktop client, the  GitHub submodule has to be loaded via `git submodule update --init --recursive`)
2. `poetry install`

*Note*: The IPython extension `autoreload` reloads modules before every cell execution. Very useful when debugging the `%%capture` cell magic!
Just add these lines into the first jupyter cell.
```py
%load_ext autoreload
%autoreload 2
import jupyter_compare_view
```

## Changelog


## 0.1.5

* BugFix: Remove black import that was added by accident. 

## 0.1.4

* `%%compare`  is now `%%splity`. `%%splity` is deprecated.
* Update examples

## 0.1.3

* octoframes github actions setup

## 0.1.2

* Move the repo from kolibril13/jupyter-spitview to octoframes/jupyter_compare_view 
* Rename all references
## 0.1.1

* Drop the [github.com/NUKnightLab/juxtapose](https://github.com/NUKnightLab/juxtapose) backend and replace it with [github.com/Octoframes/compare_view](https://github.com/Octoframes/compare_view).  
* Implement horizontal slider
* Implement Round Mask
## 0.1.0

* Update dependencies
* Update JupyterLite version
* Fix: in JupyterLite, a figure has to be explicitly called by plt.show()
* Better installation workflow

## 0.0.8

* Fixing problem with cell id and notebook reloading
* Experimentally lowering the dependencies to
`ipython = ">=6.0.0"` and `ipykernel = ">=5.0.0"` so that  jupyterlite will work hopefully.

## 0.0.7

* Rewrite of the import of JavaScript and CSS to make it more robust when closing and opening the notebook
* First attempt to add a JupyterLite example.
## 0.0.6 

Fix poetry workflow

## 0.0.5 

* Ship the javascript directly with the package, so no internet connection is required
* use jinja2 to save HTML in separate file
* load stylesheet and javascript only once in the beginning, and not in every cell that contains the splitview widget.

## 0.0.4 

* New `--height` parameter

## 0.0.3

* default slider position
* updated minimal example
* internal code restructuring and formatting
* Handle import in non jupyter context

## 0.0.2 
* save images in base64 strings and don't load images to disk (increases package security).
## 0.0.1

* First release
