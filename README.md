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

Another example:
```py
%%splity
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


Tested in JupyterLab.
Does not work in VSCode Notebooks.


## Notebook formatting
Formatting with black can be done this way: 
1. `pip install 'black[jupyter]'`
2. `black --python-cell-magics splity splitview_magic.ipynb`

## TODOS

* Don't save the images, but maybe chash them somehow?
    * Can they be phrased as bitestrings to javascript ?
* Handle cases where n ≠ 2 images.
* Ship the javascript directly with the package, so no internet connection is required
* automatically adjust the height parameter with f-strings
* implement tests, find out how to test a magic class
* parameter for default position in percent
* test the custom path flag.

Idea: Second option without using cell magic:
```python
from splitview import Splity # (does not yet exist)
my_splity = Splity(left_layer=img1, right_layer=img2)
display(my_splity)
```

## Changelog
### 0.0.2 (Work in Progress)
* handeling height
* dont save images to disk
*
### 0.0.1

* First release
