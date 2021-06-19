from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import os
import SpearDatabase

SpearDatabase.InitData()

class SpearManager(QWidget):
    def __init__(self, parent=None):
        super(SpearManager, self).__init__(parent)

        self.initUI()

        self.loadModuleNames()

        

    def initUI(self):
        self.mainLayout = QVBoxLayout()

        self.selecting = QHBoxLayout()
        
        self.notselected = QListWidget()
        self.selected = QListWidget()
        self.using = QListWidget()

        self.modulesTool = QVBoxLayout()

        self.use = QPushButton('>')
        self.use.clicked.connect(lambda: self.useModule(self.notselected.selectedItems()))
        self.unuse = QPushButton('<')
        self.unuse.clicked.connect(lambda: self.unuseModule(self.selected.selectedItems()))

        self.modulesTool.addWidget(self.use)
        self.modulesTool.addWidget(self.unuse)

        self.selecting.addWidget(self.notselected)
        self.selecting.addLayout(self.modulesTool)
        self.selecting.addWidget(self.selected)

        self.mainLayout.addLayout(self.selecting)
        self.mainLayout.addWidget(self.using)

        self.setLayout(self.mainLayout)

    def loadModuleNames(self):
        myPath = os.path.abspath('./Modules')
        modules = os.listdir(myPath)

        used = SpearDatabase.ReadData('used')
        print(used)

        self.notselected.clear()
        self.selected.clear()

        for module in modules:
            if module not in used:
                self.notselected.addItem(module)
            else:
                self.selected.addItem(module)

    def useModule(self, moduleName):
        try:
            value = moduleName[0].text()
        except:
            return
        SpearDatabase.AppendData('used', value)
        
        self.loadModuleNames()

    def unuseModule(self, moduleName):
        try:
            value = moduleName[0].text()
        except:
            return
        SpearDatabase.DeleteData('used', value)

        self.loadModuleNames()
        

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = SpearManager()
    window.show()
    sys.exit(app.exec())