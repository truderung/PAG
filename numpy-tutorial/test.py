#!/usr/bin/env python3

"""
:mod:`numpy_tutorial.test`
==========================

Computes the optical flow using the Horn Schunck model on images of the
Middlebury test data set.

:seealso: http://vision.middlebury.edu/flow/data/
"""

import pathlib

import skimage
import skimage.io
import skimage.registration
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

import horn_schunck
import horn_schunck_full as horn_schunck
import visualize


# load a test data set
path = pathlib.Path("data/RubberWhale")
im0 = skimage.io.imread(path / "frame10.png")
im1 = skimage.io.imread(path / "frame11.png")

# normalize the images
im0 = (im0 - im0.min())/im0.ptp()
im1 = (im1 - im1.min())/im1.ptp()

# estimate the optical flow
# NOTE: Choose between our Horn Schunck based implementation or the better
#       model implemented in *skimage*.

flow = horn_schunck.coarse_to_fine(im0, im1)
#flow = skimage.registration.optical_flow_tvl1(im0, im1)

# compute some analytics
flow_norm = np.sqrt(np.sum(flow*flow, axis=0))
im1w = horn_schunck.warp(im1, flow)
residual = np.abs(im0 - im1w)

# visualize the results
fig, ax = plt.subplots(2, 4)
ax[0, 0].imshow(im0, cmap="gray")
ax[0, 0].set_title("im0")

ax[0, 1].imshow(im1, cmap="gray")
ax[0, 1].set_title("im1")

ax[0, 2].imshow(0.5*(im0 + im1), cmap="gray")
ax[0, 2].set_title("im0 + im1 (blended)")

ax[0, 3].imshow(residual, cmap="gray")
ax[0, 3].set_title("residual")

ax[1, 0].imshow(flow[0], cmap="Reds")
ax[1, 0].set_title("optical flow - x")

ax[1, 1].imshow(flow[1], cmap="Reds")
ax[1, 1].set_title("optical flow - y")

ax[1, 2].imshow(visualize.color_code(
    flow[0], flow[1], max_norm=np.quantile(flow_norm, 0.75)
))
ax[1, 2].set_title("optical flow - angle")

ax[1, 3].imshow(visualize.color_wheel(r=min(im0.shape)))
ax[1, 3].set_title("color coding")

plt.show()
