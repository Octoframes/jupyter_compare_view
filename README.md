# Jupyter compare_view

<p align="center">
    <br />
    <br />
    <a href="https://mybinder.org/v2/gh/kolibril13/jupyter-splitview/HEAD?labpath=example_notebook.ipynb">
        <img src="https://mybinder.org/badge_logo.svg" alt="Binder">
    </a>
    <a href="https://kolibril13.github.io/jupyter-splitview/">
        <img src="https://jupyterlite.rtfd.io/en/latest/_static/badge.svg" alt="JupyterLight">
    </a>
    <a href="https://github.com/Octoframes/jupyter_compare_view/blob/main/LICENSE">
        <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT license" />
    </a>
    <br />
    <br />
    <i>Blend Between Multiple Images using a cell magic in JupyterLab.</i>
</p>
<hr />

## Installation
```py
pip install jupyter_compare_view
```
## Example
```py
import jupyter_compare_view
```

```py
%%splity
from skimage import data
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

img = data.chelsea()
grayscale_img = rgb2gray(img)

fig, ax1 = plt.subplots()
ax1.axis("off")
ax1.imshow(img)

fig, ax2 = plt.subplots()
ax2.axis("off")
ax2.imshow(grayscale_img, cmap="gray")
```

<img src="https://user-images.githubusercontent.com/44469195/175052654-c6c06908-746b-4bcb-819f-c81c0e8dd521.png" style="width: 300px;"/>

Note: The split view widget is still responsive after closing and reopening the notebook without running the cell again.

Another example:
```py
%%splity --position 73% --height auto

import matplotlib.pyplot as plt
import numpy as np

array1 = np.full((15, 30), 10)
array2 = np.random.randint(0, 10, size=(15, 30))
fig, ax1 = plt.subplots(figsize=(5, 10))
ax1.imshow(array1)
fig, ax2 = plt.subplots(figsize=(5, 10))
ax2.imshow(array2)
```
<img src="https://user-images.githubusercontent.com/44469195/173763087-e76be74b-57e4-4861-ae0a-6c307021b785.png" style="width: 300px;"/>


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
2. `black --python-cell-magics splity compare_view_magic.ipynb`


## Developer Installation

1. `git clone --recurse https://github.com/Octoframes/jupyter_compare_view`
(Note: In case that the repo was already cloned e.g. with the GitHub Desktop client, the  GitHub submodule has to be loaded via `git submodule update --init --recursive`)
2. `poetry install`

## Changelog

## Milestones / Wishlist

* implement tests, find out how to test a magic class

* Idea: Second option without using cell magic:
```python
from jupyter_compare_view import Splity # (does not yet exist)
my_splity = Splity(left_layer=img1, right_layer=img2)
display(my_splity)
```

* Make this work also in VSCode notebooks, [see this issue](https://github.com/NUKnightLab/juxtapose/issues/178).

* Some other nice views, like these:

Round Mask:  
<img src="https://user-images.githubusercontent.com/44469195/175031002-0f94c143-0145-4254-88ec-a8e450faa6af.png" style="width: 300px;"/>

Double Round Mask, Second one with 50% opacity:  
<img src="https://user-images.githubusercontent.com/44469195/175031014-81e78b3a-9e74-4d21-b516-2c5a0cc7f869.png" style="width: 300px;"/>

Gaussian Mask (no priority):  
<img src="https://user-images.githubusercontent.com/44469195/175031027-ef5da1f8-9c32-454f-aa1a-40d10eb086d6.png" style="width: 300px;"/>

# 0.1.1

* Drop the [github.com/NUKnightLab/juxtapose](https://github.com/NUKnightLab/juxtapose) backend and replace it with [github.com/Octoframes/compare_view](https://github.com/Octoframes/compare_view).  

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

### 0.0.2 
* save images in base64 strings and don't load images to disk (increases package security).
### 0.0.1

* First release


