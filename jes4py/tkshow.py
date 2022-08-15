import sys, pickle, atexit
import tkinter as tk
from PIL import ImageTk
from types import SimpleNamespace
from queue import Queue
from threading import Thread, Event
from jes4py import Picture
from time import sleep
import ctypes

class App():
    ExitCode = 'exit'
    def __init__(self):
        self.logfile = open('/tmp/show.log', 'w')
        self.root = tk.Tk()
        self.imageQueue = Queue()
        stopEvent = Event()
        showThread = Thread(target=self.showImages, args=(stopEvent,), daemon=True)
        showThread.start()
        self.listenThread = Thread(target=self.listener, args=(stopEvent,), daemon=True)
        self.listenThread.start()
        atexit.register(self.stopBackground, stopEvent, showThread)
        atexit.register(self.stopBackground, stopEvent, self.listenThread)
        self.root.protocol("WM_DELETE_WINDOW", self.windowClosed)
        self.root.mainloop()

    def showImages(self, event):
        self.logfile.write('Show thread has started\n')
        self.logfile.flush()
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack()
        imageID = None
        while not event.is_set():
            picture = self.imageQueue.get()
            self.logfile.write('Possible image found on queue...\n')
            self.logfile.write(f'  Type: {type(picture)}\n')
            self.logfile.write(f'  Value: {picture}\n')
            self.logfile.flush()
            if isinstance(picture, str) and picture == self.ExitCode:
                self.logfile.write('not an image - exit code\n')
                self.logfile.flush()
                #self.root.destroy()
                return
            try:
                self.logfile.write('must be an image\n')
                self.logfile.flush()
                self.root.title(picture.getTitle())
                image = ImageTk.PhotoImage(picture.getImage())
                self.canvas.config(width=picture.getWidth(),
                                   height=picture.getHeight())        
                if imageID is None:
                    self.logfile.write('showing a new image\n')
                    self.logfile.flush()
                    imageID = self.canvas.create_image(0, 0, anchor=tk.NW,
                                                       image=image)
                else:
                    self.logfile.write('repainting exisiting image\n')
                    self.logfile.flush()
                    self.canvas.itemconfig(imageID, image=image)
            except AttributeError:
                pass

    def raiseException(self, threadID):
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(threadID, ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(threadID, 0)

    def listener(self, event):
        """Run Listener thread"""
        self.logfile.write('About to enter main while loop\n')
        self.logfile.flush()
        while not event.is_set():
            # wait for control code
            self.logfile.write('Waiting for control code\n')
            self.logfile.flush()
            data = sys.stdin.buffer.read(1)
            self.logfile.write(f'Got control code {data}\n')
            self.logfile.flush()
            if not event.is_set() and data == Picture.show_control_exit:
                for i in range(10):
                    self.logfile.write('Quitting\n')
                    self.logfile.flush()
                self.imageQueue.put('quit')
                return
            elif data == Picture.show_control_data:
                self.logfile.write('About to try and read picture data\n')
                self.logfile.flush()
                # read picture size and pickled picture data
                try:
                    data = sys.stdin.buffer.read(8)
                    dataLen = int.from_bytes(data, byteorder='big')
                    self.logfile.write(f'Picture size: {dataLen}\n')
                    self.logfile.flush()
                    pkg = sys.stdin.buffer.read(dataLen)
                    self.logfile.write(f'Read {dataLen} bytes from picture obj\n')
                    self.logfile.flush()
                    picture = pickle.loads(pkg)
                    self.imageQueue.put(picture)
                except RuntimeError:
                    self.logfile.write('Runtime error - closing\n')
                    self.logfile.flush()
                    return
            else:
                self.logfile.write('Unrecognized control - closing\n')
                self.logfile.flush()
                # unrecognised control code
                return
            self.logfile.write('End of main While loop\n')
            self.logfile.flush()
            #sleep(5)
        self.logfile.write('Closing log and leaving function\n')
        self.logfile.flush()

    def stopBackground(self, event, thread):
        event.set()
        self.imageQueue.put(self.ExitCode)
        #self.windowClosed()
        thread.join()
        self.logfile.write('stopBackground: Exit\n')
        self.logfile.flush()
        self.logfile.close()
        exit()
    
    def windowClosed(self):
        self.logfile.write('windowClosed\n')
        self.logfile.flush()
        self.imageQueue.put(self.ExitCode)
        self.listenThread.join()
        self.listenThread._stop()
        #self.raiseException(self.listenThread)
        try:
            self.root.destroy()
            del self.root
        except AttributeError:
            pass
        exit()

if __name__ == '__main__':
    app = App()
