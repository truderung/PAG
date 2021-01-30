"""
:mod:`visualize`
================

Some small helper functions for visualizing the optical flow. Essential the
color coding of the flow vectors.
"""

import numpy as np
import scipy as sp
import skimage
import skimage.io
import skimage.color
import matplotlib.pyplot as plt


def color_code(x, y, max_norm=1.0):
    """Color encodes the 2D vectors given by the coordinates (x, y)."""
    alpha = np.arctan2(x, y)
    alpha = np.fliplr(alpha)
    alpha = np.flipud(alpha)

    norm = np.sqrt(x*x + y*y)

    hsv = np.zeros((*alpha.shape, 3))
    hsv[..., 0] = (alpha + np.pi)/(2.0*np.pi)
    hsv[..., 1] = np.clip(0.0, 1.0, norm/max_norm)
    hsv[..., 2] = 1.0

    rgb = skimage.color.hsv2rgb(hsv)
    return rgb


def color_wheel(r=512):
    """Visualize the color coding with a small circle."""
    x, y = np.indices((r, r), dtype=float)
    x -= x.mean()
    y -= y.mean()

    rgb = color_code(x, y, max_norm=x.max())
    rgb[np.sqrt(x*x + y*y) > 0.5*r] = 1.0
    return rgb


if __name__ == "__main__":
    wheel = color_wheel()
    plt.imshow(wheel)
    plt.show()
