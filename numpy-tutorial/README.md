# numpy-tutorial

This repository contains a small implementation of the Horn-Schunck model for
estimating the optical flow, as well as some code for visualizing the flow
and testing it on the Middlebury database.

*   https://en.wikipedia.org/wiki/Horn%E2%80%93Schunck_method
*   http://vision.middlebury.edu/flow/data/

Install the requirements in *requirements.txt*
```bash
pip3 install -r requirements.txt
```
and run the example with
```bash
python3 test.py
```

## Excerices ?

*   Play with the parameters of the Horn-Schunck solver, especially the
    number of iterations, warps and median filtering.
*   Use broadcasting to replace the *flow[0], flow[1]* indexing the code.
    Hints:
    *   Wrap the gradient in an array: ``grad = np.array(np.gradient(im0))``
    *   Use the *axis* keyword in *np.sum*: ``norm = np.sum(grad, axis=0)``
