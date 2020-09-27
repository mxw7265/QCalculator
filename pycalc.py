#!/usr/bin/env python3

# Filename: pycalc.py

"""PyCalc is a simple calculator built using Python and PyQt5."""

import sys

from PyQt5.QtCore import Qt

# Import QApplication and the required widgets from PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLineEdit, QPushButton, QVBoxLayout

class PyCalcUi(QMainWindow):
    """PyCalc's View (GUI)"""
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyCalc')
        self.setFixedSize(235, 235)

        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        self.display = QLineEdit()

        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)

        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        self.buttons = dict()

        buttonsLayout = QGridLayout()

        buttons = {
            '7': (0, 0),
            '8': (0, 1),
            '9': (0, 2),
            '/': (0, 3),
            'C': (0, 4),
            '4': (1, 0),
            '5': (1, 1),
            '6': (1, 2),
            '*': (1, 3),
            '(': (1, 4),
            '1': (2, 0),
            '2': (2, 1),
            '3': (2, 2),
            '-': (2, 3),
            ')': (2, 4),
            '0': (3, 0),
           '00': (3, 1),
            '.': (3, 2),
            '+': (3, 3),
            '=': (3, 4)
        }

        for btnText, (px, py) in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btnText], px, py)

        self.generalLayout.addLayout(buttonsLayout)

# Client code
def main():
    pycalc = QApplication(sys.argv);

    view = PyCalcUi()
    view.show()

    sys.exit(pycalc.exec_())

if __name__ == "__main__":
    main()
