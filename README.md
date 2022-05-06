Jupyter Splitview
=================

A cell magic that displays images in splitview using https://github.com/NUKnightLab/juxtapose.  
*NOTE: Still work in progress, there will be breaking changes.*
## Installation
```py
pip install jupyter-splitview
```
## Example
```py
import jupyter_splitview
```

```py
%%splity

from skimage import data
from skimage.util import random_noise
import matplotlib.pyplot as plt

img = data.chelsea()
noisy_img = random_noise(img, var=0.02)

fig, ax1 = plt.subplots()
ax1.axis('off')
ax1.imshow(img)

fig, ax2 = plt.subplots()
ax2.axis('off')
ax2.imshow(noisy_img)
```

<img src="concept_image.jpg" style="width: 300px;"/>

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
<img src="concept_image2.jpg" style="width: 300px;"/>


## Notebook arguments

* `--position 73%` will set the slider start position to 73%.
*  The height of the widget. 
* `--height 220` will set the height to 220 pixel. 
* When `--height`is not provided, the default height of the widget is 300 pixel.
* `--height auto` will set the height by the value of the first image's resolution in vertical direction.
* The widget's width will always be adjusted automatically. 

## Notebook formatting
Formatting with black can be done this way: 
1. `pip install 'black[jupyter]'`
2. `black --python-cell-magics splity splitview_magic.ipynb`

## TODOS

* Make this work also in VSCode notebooks
* Ship the javascript directly with the package, so no internet connection is required.
* Handle cases where n ≠ 2 images. Currenty: All further img are ignored.
* implement tests, find out how to test a magic class

Idea: Second option without using cell magic:
```python
from splitview import Splity # (does not yet exist)
my_splity = Splity(left_layer=img1, right_layer=img2)
display(my_splity)
```

## Changelog


## 0.0.4 (Work in Progress)

* New `--height` parameter with three modes:
    A) 200px fixed height
    B) custom fixed height
    C) auto height from first images

## 0.0.3

* default sider position
* updated minimal example
* internalt code restructuring and formatting
* Handle import in non jupyter context

### 0.0.2 
* save images in base64 strings and don't load images to disk (increases package security).
### 0.0.1

* First release
