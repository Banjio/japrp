from japrp.dict_viewer_pyqt5 import DictViewTree
from PyQt5.QtWidgets import QApplication

def test_dict_view_tree():
    value = { 'key1': 'value1', 'key3': [1,2,3, { 1: 3, 7 : 9}]}
    app = QApplication([])
    window = DictViewTree(value)
    window.show()
    app.exec()