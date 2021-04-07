"""
PyQt5 Widget that Implements a tree view for python dictionaries from:
https://stackoverflow.com/questions/21805047/qtreewidget-to-mirror-python-dictionary
"""

from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QDialog, QVBoxLayout

class DictViewTree(QTreeWidget):
    def __init__(self, dict_):
        super().__init__()

        def fill_item(item, value):

            def new_item(parent, text, val=None):
                child = QTreeWidgetItem([text])
                fill_item(child, val)
                parent.addChild(child)
                child.setExpanded(True)

            if value is None: return
            elif isinstance(value, dict):
                for key, val in sorted(value.items()):
                    new_item(item, str(key), val)
            elif isinstance(value, (list, tuple)):
                for val in value:
                    text = (str(val) if not isinstance(val, (dict, list, tuple))
                            else '[%s]' % type(val).__name__)
                    new_item(item, text, val) 
            else:
                new_item(item, str(value))

        fill_item(self.invisibleRootItem(), dict_)


class DictTreeViewAsDialog(QDialog):

    def __init__(self, dict_, parent=None):
        super().__init__(parent=parent)
        self.Layout = QVBoxLayout()
        tree = DictViewTree(dict_)
        self.Layout.addWidget(tree)
        self.setLayout(self.Layout)