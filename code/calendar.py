from PyQt5 import QtWidgets, uic, QtGui, QtCore
import sys, importlib
from libabr import core,app,res, file
from libnam import files, control
import app, importlib

class MainApp (QtWidgets.QCalendarWidget):

    def __init__(self,args):
        super(MainApp, self).__init__()

        self.Backend = args[0]
        self.Env = args[1]
        self.Desktop = args[2]
        self.Widget = args[3]

        self.Widget.setWindowTitle ("Calendar")
        self.Widget.setWindowIcon (QtGui.QIcon(res.get('@logo/calendar')))

        ## Data base ##
        sweek = files.readall("/proc/info/sweek")

        self.Widget.resize(720,500)

        ## Calender widget ##

        ## Start week ##
        if sweek=="Sat":
            self.setFirstDayOfWeek(QtCore.Qt.Saturday)
        elif sweek=="Sun":
            self.setFirstDayOfWeek(QtCore.Qt.Sunday)
        elif sweek=="Mon":
            self.setFirstDayOfWeek(QtCore.Qt.Monday)
        elif sweek=="Tue":
            self.setFirstDayOfWeek(QtCore.Qt.Tuesday)
        elif sweek=="Wed":
            self.setFirstDayOfWeek(QtCore.Qt.Wednesday)
        elif sweek=="Thu":
            self.setFirstDayOfWeek(QtCore.Qt.Thursday)
        elif sweek=="Fri":
            self.setFirstDayOfWeek(QtCore.Qt.Friday)

        self.setGridVisible(True) # https://www.tutorialspoint.com/pyqt/pyqt_qcalender_widget.htm
