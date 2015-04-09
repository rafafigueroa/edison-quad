# -*- coding: utf-8 -*-
"""
Simple examples demonstrating the use of GLMeshItem.

"""

from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import time

app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.show()
w.setWindowTitle('pyqtgraph example: GLMeshItem')
w.setCameraPosition(distance=40)

g = gl.GLGridItem()
g.scale(2,2,1)
w.addItem(g)

import numpy as np

## Example 1:
## Array of vertex positions and array of vertex indexes defining faces
## Colors are specified per-face
a = 1
b = 7
c = 0.3
trans = 1.0
verts = np.array([
    [0, 0, b/2.0],
    [0, b, 0],
    [-a, a, c],
    [-b, 0, 0],
    [-a, -a, c],
    [0, -b, 0],
    [a, -a, c],
    [b, 0, 0],
    [a, a, c],
    [-a, a, -c],
    [-a, -a, -c],
    [a, -a, -c],
    [a, a, -c]
])




faces = np.array([
    [0, 2, 8], [0, 2, 4], [0, 4, 6], [0, 6, 8], 
    [1, 2, 8],
    [2, 3, 4],
    [4, 5, 6],
    [6, 7, 8],
    [1, 9, 12],
    [9, 3, 10],
    [5, 10, 11],
    [7, 11, 12],
    [1, 2, 9],
    [3, 2, 9],
    [3, 4, 10],
    [5, 4, 10],
    [5, 6, 11],
    [7, 6, 11],
    [7, 8, 12],
    [1, 8, 12]
])
colors = np.array([
    [0, 0, 1, trans], [0, 0, 1, trans], 
    [0, 0, 1, trans], [0, 0, 1, trans],
    [0, 1, 0, trans],
    [1, 1, 1, trans],
    [1, 1, 1, trans],
    [1, 0, 0, trans],
    [0, 1, 0, trans],
    [1, 1, 1, trans],
    [1, 1, 1, trans],
    [1, 0, 0, trans],
    [0, 1, 0, trans],
    [1, 1, 1, trans],
    [1, 1, 1, trans],
    [1, 1, 1, trans],
    [1, 1, 1, trans],
    [1, 0, 0, trans],
    [1, 0, 0, trans],
    [0, 1, 0, trans]
])

## Mesh item will automatically compute face normals.
m1 = gl.GLMeshItem(vertexes=verts, faces=faces, faceColors=colors, smooth=False)
for ang in range(0,180):
    m1.rotate(45, 1, 0, 0)
    time.sleep(0.1)

m1.setGLOptions('opaque')
w.addItem(m1)

## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

for ang in range(0,180):
    m1.rotate(45, 1, 0, 0)
    time.sleep(0.1)

