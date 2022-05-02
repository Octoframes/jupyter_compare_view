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

![](concept_image.jpg)
