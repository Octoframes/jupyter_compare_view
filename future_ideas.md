
Example of the concept without cell magic:
```python
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

#new part (does not exist yet):
from splitview import SplitMapControl
control = SplitMapControl(left_layer=fig1, right_layer=fig2)
m.add_control(control)
m
```