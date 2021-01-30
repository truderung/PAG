import shutil, sys, os, time, pickle
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QObject, QTimer
from PySide2.QtWidgets import QApplication
from Threading import *


class TExample(QObject):
    def __init__(self):
        super().__init__()
        self._application_name = "thread_example"
        self._application_version = "v1.0"

        self.dispatcher = WorkerDispatcher()

        self._timer = QTimer(self)
        self._timer.timeout.connect(self._slot_new_angle)
        self._timer.start(500)

    # #############################################################
    # slots
    # #############################################################

    def _slot_new_angle(self):
        print("\n\nneue Winkelstellung, mach was ...")
        self.dispatcher.start_sensor_read("sensor1")
        self.dispatcher.start_sensor_read("sensor2")
        self.dispatcher.start_sensor_read("sensor3")


# execute MainWindow
if __name__ == '__main__':
  app = QApplication(sys.argv)
  TExample()
  app.exec_()
  app.aboutToQuit.connect(app.deleteLater)
