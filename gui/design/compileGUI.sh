#!/bin/bash

cd ~/Workspace/python_qt/gui/design
pyrcc5 Images.qrc -o ../Images_rc.py
pyuic5 -x MainWindow.ui -o ../Ui_MainWindow.py

#Replace alertsystemimages_rc by the package gui.alertsystemimages_rc
gsed -i '/import Images_rc/c\import gui.Images_rc' ~/Workspace/python_qt/gui/Ui_MainWindow.py
