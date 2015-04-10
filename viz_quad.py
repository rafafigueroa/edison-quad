#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Rafael Figueroa
Visualization object for quadrotor
to be called from main GUI program
"""
# PyQtGraph imports
import pyqtgraph.opengl as gl
import numpy as np


def create_viz_quad():
    """Creates a simple quadrotor representation, 
    with RGB axis"""
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
    m1 = gl.GLMeshItem(vertexes=verts, faces=faces, 
                       faceColors=colors, smooth=False)
    m1.setGLOptions('opaque')
    return m1

