#!/usr/bin/env python
#coding: utf-8

from PyQt4 import QtCore, QtGui
from paste import paste2cloud

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        icon = QtGui.QIcon("./tape.ico")
        self.trayIcon = QtGui.QSystemTrayIcon(self)
        self.trayIcon.setIcon(icon)
        self.trayIcon.show()
        self.Menu()

    def Menu(self):
        self.pasteAction = QtGui.QAction("Paste", self, triggered=paste2cloud)
        self.quitAction = QtGui.QAction("Quite", self, triggered=QtGui.qApp.quit)

        self.trayIconMenu = QtGui.QMenu(self)
        self.trayIconMenu.addAction(self.pasteAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.quitAction)
        self.trayIcon.setContextMenu(self.trayIconMenu)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)

    frm = Window()

    sys.exit(app.exec_())
