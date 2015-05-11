#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Rafael Figueroa
GUI object for quadrotor base station
"""

# Python imports
from __future__ import division
import numpy as np

# PyQtGraph imports
import pyqtgraph as pg
import pyqtgraph.opengl as gl
from pyqtgraph.Qt import QtGui, QtCore

# Visualization of Quatrotor
from viz_quad import create_viz_quad

class GUI_quad(object):

    def __init__(self):
        
        self.x = 0
        self.y = 0
        self.z = 0
        self.hx = 0
        self.hy = 0
        self.hz = 0

        # Qt Initialization (once per application)
        self.app = QtGui.QApplication([])

        # Top level of Qt Widget, Main Window
        self.mw = QtGui.QWidget()
        self.mw.resize(800, 1200)
        
        # Main Widget
        self.main_widget = pg.PlotWidget(name = 'Main')
        
        # Widget showing the current quadrotor rotation
        self.viz_quad = create_viz_quad()  # returns a glMeshItem

        self.viz_quad_widget = gl.GLViewWidget()
        self.viz_quad_widget.setWindowTitle('Quadrotor Rotation')
        self.viz_quad_widget.setCameraPosition(distance=40)
        self.viz_quad_widget.addItem(self.viz_quad)
        
        # Grid
        self.gl_grid = gl.GLGridItem()
        self.gl_grid.scale(2, 2, 1)
        self.viz_quad_widget.addItem(self.gl_grid)

        # Layout
        layout = QtGui.QGridLayout(self.mw)
        layout.addWidget(self.main_widget, 0, 0)
        layout.addWidget(self.viz_quad_widget, 1, 0)
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
    
    def set_state(self, X):
        self.x = X[0]
        self.y = X[1]
        self.z = X[2]
        self.hx = X[3]
        self.hy = X[4]
        self.hz = X[5]
        print self.hx, self.hy, self.hz

    def update_gui(self):
        """Updates all moving parts of the GUI.
        Called from the QtCore Timer at regular intervals"""
        # self.viz_quad.rotate(3 + self.counter, 1, 0, 0)
        roll = self.hx
        pitch = self.hy
        yaw = self.hz 

        print roll, pitch, yaw

        tr = pg.Transform3D()
        # TODO: Check rotation with model
        # Now using Ry(pitch)*Rx(roll)*Rz(yaw)*coordinate
        tr.rotate(np.degrees(yaw), 0, 0, 1)
        tr.rotate(np.degrees(roll), 1, 0, 0)
        tr.rotate(np.degrees(pitch), 0, 1, 0)
        
        self.viz_quad.setTransform(tr)
        self.app.processEvents()

    def run(self):
        self.app.exec_()
        
        
