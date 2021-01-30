import os, re, time, traceback, sys  #, shutil
from PySide2 import QtCore
from PySide2.QtCore import Signal, QThread, QObject


class WorkerAbstract(QThread):
    def __init__(self):
        super().__init__()

        class WorkerSignals(QObject):
            '''
            step_done
                no data
            error
                `tuple` (exctype, value, traceback.format_exc() )
            '''            
            step_done = Signal()
            error = Signal(tuple)
        
        self._signals = WorkerSignals()
        self.step_done = self._signals.step_done
        self.error = self._signals.error

    def run(self):
        try:
            self.work()
        except:
            traceback.print_exc()
            extype, value = sys.exc_info()[:2]
            self.error.emit((extype, value, traceback.format_exc()))
 
    def work(self):
        raise NotImplementedError("Please Implement the method work")


class WorkerReadSensor(WorkerAbstract):
    def __init__(self, sensor):
        super().__init__()
        self.sensor = sensor

    def work(self):
        start = time.time()

        for i in range(3):
            time.sleep(0.02)
            self.step_done.emit()

        print("Dauer: %f Sekunden" % (time.time()-start))



class WorkerDispatcher(QObject):
    def __init__(self):
        super().__init__()
        self.worker = set()

    def start_sensor_read(self, sensor):
        t = WorkerReadSensor(sensor)
        t.step_done.connect(self._slot_workstep_done)
        t.error.connect(self._slot_workerror_occured)
        t.finished.connect(self._slot_worker_done)

        self.worker.add(t)
        t.start()
        print("thread für %s initialized" % (sensor))

    # #############################################################
    # slots
    # #############################################################
    def _slot_workerror_occured(self, data):
        #(extype, value, traceback_content) = data
        print("error while worker thread")

    def _slot_workstep_done(self):
        print("schaffe schaffe ...")

    def _slot_worker_done(self):
        t = self.sender()
        print("%s finished" % t.sensor)

        self.worker.discard(t)
        t.deleteLater()
        if len(self.worker) > 0:
            return
        self._slot_all_worker_finished()

    def _slot_all_worker_finished(self):
        print("Alle Sensoren gelesen")
