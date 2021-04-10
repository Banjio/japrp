### Build a py file from an ui file

> pyuic5 gui.ui -o gui.py

## General structure

* Application consist of one main windows and one or several dialog windows.
* Dialogs have buttons, whereas main windows has a menu bar, toolbar, satus bar or a central widget
* Dialog can be __Modal__ &Rightarrow; Until closed blocks all other user input or __Modeless__ &Rightarrow; can be open but user is free to interact with rest of program

### Qt Design(er) basics

New template can be of type:

* __Dialog with Buttons Bottom or Buttons Right__: This template creates a form with the OK and
Cancel buttons in the bottom-right corner or top right corner.
*  __Dialog without Button__: Empty form, superclass of Dialogs is _QDialog_
* __Main Window__: Main window with menu bar and toolbar 
* __Widget__: Template which supercalss is _QWidget_

Everything is a widget. Every GUI has a top-level widget and the rest are called its children. The top-level widget can be 
_QDialog, QWidget or QMainWindows_, thus a guid has to inherit 
from one of these classes

# Best Practices

* Although not neccessary consider wrapping function that connect a widget to a function (i.e. assigining a slot) for 
example ```Qpushbutton.clicked.connect(on_click_func)```  with the decorator ```from PyQt5.Core import pyqtSlot``` as it
  reduces the memory footprint.
```
from pyqt5.QtCore import pyqtSlot
...
@pyQtSlot(int)
def func(self, var: int):
  do_something()
```
* Use ```from functools import partial``` to dynamically create buttons and connect them to a function with varying inputs

## Desiging apps
Best practice in desiging copied from [here](https://stackoverflow.com/questions/58247357/qt5-pyqt5-best-practices):

"Generally, to minimise the complexity of UI elements (e.g. Main Window) and make applications more decoupled (thus, more maintainable), you can use the Model-View-Controller (MVC) pattern.

In a typical use-case, each UI element (the 'view') is backed by a controller class and a model class. When a signal is triggered, the appropriate method on the controller is called. The controller method, in turn, calls a method on the model and/or changes another UI element.

The above example presents a one-to-one association between view, controller, and model, but you can vary this according to your requirements.
There are other modern derivatives of MVC (e.g. MVVM and MVP), but I prefer it because of its simplicity and also because the other patterns are more effective when the framework in use supports them."

### Model View Controller
[Guide](https://www.learnpyqt.com/tutorials/modelview-architecture/):


# Link References (I.e. Cool Projects)

* __Winamp Clone with Qt5__: https://www.learnpyqt.com/examples/failamp-multimedia-player/


# Widget References

## QLabel

* Display Messages
* Take no input 

#### Methods

* setText() : This method assigns text to the Label widget 
* setPixmap() : This method assigns pixmap , an instance of the QPixmap class, to
the Label widget
* setNum() : This method assigns an integer or double value to the Label widget
* clear() : This method clears text from the Label widget

## QLineEdit

* Entering, undo, redo, cut and paste single line data

### Methods

* setEchoMode() : It sets the echo mode of the Line Edit widget. That is, it
determines how the contents of the Line Edit widget are to be displayed. The available options are as follows:
    
    * Normal : This is the default mode and it displays characters the way they are
entered
    * NoEcho : It switches off the Line Edit echo, that is, it doesn't display
anything
    * Password : This option is used for password fields, no text will be displayed;
instead, asterisks appear for the text entered by the user
    * PasswordEchoOnEdit : It displays the actual text while editing the
password fields, otherwise it will display the asterisks for the text
      
* maxLength() : This method is used to specify the maximum length of text that
can be entered in the Line Edit widget.
* setText() : This method is used for assigning text to the Line Edit widget.
* text() : This method accesses the text entered in the Line Edit widget.
* clear() : This method clears or deletes the complete content of the Line Edit
widget.
* setReadOnly() : When the Boolean value true is passed to this method, it will
make the Line Edit widget read-only, that is, non-editable. The user cannot make
any changes to the contents displayed through the Line Edit widget, but can only
copy.
* isReadOnly() : This method returns the Boolean value true if the Line Edit
widget is in read-only mode, otherwise it returns false.
* setEnabled() : By default, the Line Edit widget is enabled, that is, the user can
make changes to it. But if the Boolean value false is passed to this method, it will
disable the Line Edit widget so the user cannot edit its content, but can only
assign text via the setText() method.
* setFocus() : This method positions the cursor on the specified Line Edit widget.

## QPushbutton

* If you precede a character with "&" (Ampersand) when setting text of button then the button will have this key as a shortcut
and can be activated with Alt + Key
  
### Methods

* setText(): Assign text 
* setIcon(): Assign icon


# Useful links and bocks

* The ultimate PyQt webiste: https://www.learnpyqt.com/