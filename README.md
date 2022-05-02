jupyter-splitview 
=================

A cell magic that displays images in splitview using https://github.com/NUKnightLab/juxtapose.

Here is an example:

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

Implementation can be found in `splitview_magic.ipynb`.
Package on pypi will come soon.

Tested in JupyterLab.
Does not work in VSCode Notebooks.


## Notebook formatting
Formatting with black can be done this way: 
1. `pip install 'black[jupyter]'`
2. `black --python-cell-magics splity splitview_magic.ipynb`

