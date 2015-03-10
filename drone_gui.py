#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Rafael Figueroa
GUI object for quadrotor base station
"""

#Python imports
from __future__ import division
import numpy as np

#PyQtGraph imports
import pyqtgraph as pg
import pyqtgraph.opengl as gl
from pyqtgraph.Qt import QtGui, QtCore


class GUI_quad(object):

    def __init__(self):
        # Qt Initialization (once per application)
        self.app = QtGui.QApplication([])

        # Top level of Qt Widget, Main Window
        self.mw = QtGui.QWidget()
        self.mw.resize(800, 1200)
        
        # Main Widget
        self.main_widget = pg.PlotWidget(name = 'Main')
        
        # Widget showing the current quadrotor rotation
        self.quad_rot_widget = gl.GLViewWidget()
        self.quad_rot_widget.setWindowTitle('Quadrotor Rotation')
        self.quad_rot_widget.setCameraPosition(distance=40)

        # Rotation Axis
        self.rot_axis = create_rot_axis()
        self.quad_rot_widget.addItem(self.rot_axis)
        
        # Rotation Grid
        self.gl_grid = gl.GLGridItem()
        self.gl_grid.scale(2, 2, 1)
        self.quad_rot_widget.addItem(self.gl_grid)

        # Layout
        layout = QtGui.QGridLayout(self.mw)
        layout.addWidget(self.main_widget, 0, 0)
        layout.addWidget(self.quad_rot_widget, 1, 0)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 2)

        self.mw.setLayout(layout)

        # Show main window
        self.mw.show()

        # GUI Update loop timer with callback function
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_gui)
        self.timer.start(50.0) # in ms

        self.counter = 0
        
    def update_gui(self):
        """Updates all moving parts of the GUI.
        Called from the QtCore Timer at regular intervals"""
        self.rot_axis.rotate(3, 1, 0, 0)
        self.counter = self.counter + 1
        self.gl_grid.setRotation(45+self.counter, 1, 0, 0)
        self.app.processEvents()

    def run(self):
        self.app.exec_()
        

def create_rot_axis():
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

# Script
GUI = GUI_quad()
GUI.run()

        
