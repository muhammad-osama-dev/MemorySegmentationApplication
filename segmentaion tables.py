from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,  QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
import sys


class Window(QWidget):
    def __init__(self, num_of_seg, process_number, seg_names, limit, base):
        super().__init__()
        self._num_of_seg = num_of_seg
        self._process_number = process_number
        self._seg_names = seg_names
        self._limit = limit
        self._base = base
        self.title = self._process_number
        self.top = 100
        self.left = 100
        self.width = 500
        self.height = 400

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.creatingTables()

        self.show()

    def creatingTables(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(self._num_of_seg)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(('SegNumber', 'limit', 'Base'))
        seg_list = self._seg_names
        limit_list = self._limit
        base_list = self._base
        for row in range(self._num_of_seg):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(seg_list[row]))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(limit_list[row])))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(base_list[row])))

        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.addWidget(self.tableWidget)
        self.setLayout(self.vBoxLayout)

App = QApplication(sys.argv)
window = Window(3, 'p2', ['seg1', 'seg2', 'seg3'], [5, 6, 7] ,[7 , 6 , 8])
sys.exit(App.exec())