"""
:mod:`horn_schunck`
===================

A simple implementation of the Horn-Schunck model for determining the optical
flow. The optical flow is obtained as the minimizer of the energy functional:

.. code-block:: math

    \min_{u}
        \frac{1}{2} \lVert f_0(x) + \nabla f_0(x) u(x) - f_1(x) \rVert_F^2
        + \frac{\lambda^2}{2} \lVert \nabla u \rVert_F^2

.. note::

    The model has been specifically implemented for 2 dimensional images,
    although it can be easily generalized to higher dimensions.
"""

import functools

import numpy as np
import scipy as sp
import skimage
import skimage.io
import skimage.registration
import matplotlib.pyplot as plt

import visualize


__all__ = [
    "HS_KERNEL_2D_4",
    "HS_KERNEL_2D_8",
    "warp",
    "solve_hs",
    "coarse_to_fine"
]


#: Anisotropic kernel in the Horn Schunck method for 2D images. Corresponds to
#: a 4 neighbourhood.
HS_KERNEL_2D_4 = np.array([
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
])/4.0


#: Isostropic kernel in the Horn Schunck method for 2D images. Corresponds to
#: an 8 neighbourhood.
HS_KERNEL_2D_8 = np.array([
    [1, 2, 1],
    [2, 0, 2],
    [1, 2, 1]
])/12.0


def warp(im, flow):
    """Warp the image given the new coordinates. The result is of the same shape
    as im0.
    """
    grid = np.indices(im.shape)
    pos = grid + flow

    out = sp.ndimage.map_coordinates(
        im, pos, mode="nearest", order=1, prefilter=False
    )
    out = out.reshape(im.shape)
    return out


def solve_hs(
    im0, im1, flow=None,
    *, clambda=0.065, nwarps=5, ninner=20, filter_median=True,
    hs_kernel=HS_KERNEL_2D_8
    ):
    """Computes the optical flow based on the Horn-Schunck-method.

    :arg ndarray im0:
        The template image.
    :arg ndarray im1:
        The reference image.
    :arg ndarray flow:
        Initial value for the optical flow.
    :arg float clambda:
        Regularization factor for the flow gradient. The larger, the smoother
        the flow (and the less the influence of the data term).
    :arg int nwarps:
        Number of warps.
    :arg int ninner:
        Number of Gauss-Seidel iterations to perform per warp, in order to
        approximate the solution.
    :arg bool filter_median:
        If true, the optical flow is filtered with a 3x3 median filter before
        each warping step to remove outliers.
    :arg ndarray hs_kernel:
        The kernel used to compute the (modified) laplacian of the optical flow.
    """
    # sanity checks
    if im0.shape != im1.shape:
        raise ValueError("im0 and im1 must have the same shape.")
    if im0.ndim != 2:
        raise ValueError("im0 and im1 must have both dimension 2.")

    # init the optical flow
    grid = np.indices(im0.shape)
    if flow is None:
        flow = np.zeros((im0.ndim, *im0.shape))

    # compute the gradient of im0 using central differences
    im0x, im0y = np.gradient(im0)

    # minimize the Horn-Schunck energy
    for iwarp in range(nwarps):

        # median filter to remove outliers
        if filter_median:
            flow[0] = sp.ndimage.filters.median_filter(flow[0], size=3)
            flow[1] = sp.ndimage.filters.median_filter(flow[1], size=3)

        # warp the image and the gradients
        im0w = warp(im0, flow)
        im0wx = warp(im0x, flow)
        im0wy = warp(im0y, flow)

        # compute constants

        # TODO: Implement the Horn-Schunck iteration here using
        #
        #       It          = im0w - im0wx*flow[0] - im0wy*flow[1] - im1
        #       Ix          = im0wx
        #       Iy          = im0wy
        #       u_quer      = convolve(flow[0], hs_kernel)
        #       v_quer      = convolve(flow[1], hs_kernel)
        #       4*alpha**2  = clambda**2
        #
        #       where the left side represents the names on the wikipedia page.

        c0 = clambda**2 + im0wx**2 + im0wy**2
        c1 = im0w - im0wx*flow[0] - im0wy*flow[1] - im1

        # Gauss-Seidel iterations
        for iinner in range(ninner):
            c2 = sp.ndimage.convolve(flow[0], hs_kernel, mode="nearest")
            c3 = sp.ndimage.convolve(flow[1], hs_kernel, mode="nearest")

            c4 = (im0wx*c2 + im0wy*c3 + c1)/c0

            flow[0] = c2 - im0wx*c4
            flow[1] = c3 - im0wy*c4
    return flow


def coarse_to_fine(im0, im1, *args, **kargs):
    """The pyramidal scheme needed to estimate large displacement optical flow.

    This function accepts the same parameters as :func:`solve`.
    """
    # Fix the paramters in the Horn Schunck solver.
    solver = functools.partial(solve_hs, *args, **kargs)

    # For sake of convenience, this is taken from the :mod:`skimage` library.
    return skimage.registration._optical_flow_utils.coarse_to_fine(
        im1, im0, solver
    )


if __name__ == "__main__":
    # load a test image
    im0 = skimage.io.imread("data/lena.pgm")

    # create a ground truth warp field
    flow0 = np.empty((2, *im0.shape))
    flow0[0] = 2.0
    flow0[1] = -1.0

    # create a ground truth "moved" image
    im1 = warp(im0, flow0)

    # compute the optical flow
    flow = coarse_to_fine(im0, im1)

    # visualize the results
    fig, ax = plt.subplots(2, 4)
    ax[0, 0].imshow(im0, cmap="gray")
    ax[0, 1].imshow(im1, cmap="gray")
    ax[0, 2].imshow(visualize.color_code(flow[0], flow[1]))
    ax[0, 3].imshow(visualize.color_wheel())

    ax[1, 0].imshow(flow[0], cmap="gray")
    ax[1, 1].imshow(flow[1], cmap="gray")
    ax[1, 2].imshow(np.abs(flow[0] - flow0[0]), cmap="gray")
    ax[1, 3].imshow(np.abs(flow[1] - flow0[1]), cmap="gray")

    plt.show()
