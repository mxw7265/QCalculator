#!/usr/bin/env python3

# Filename: pycalc.py

"""PyCalc is a simple calculator built using Python and PyQt5."""

import sys

# Import QApplication and the required widgets from PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

class PyCalcUi(QMainWindow):
    """PyCalc's View (GUI)"""
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyCalc')
        self.setFixedSize(235, 235)

        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)

# Client code
def main():
    pycalc = QApplication(sys.argv);

    view = PyCalcUi()
    view.show()

    sys.exit(pycalc.exec_())

if __name__ == "__main__":
    main()
