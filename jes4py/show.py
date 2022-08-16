#!/usr/bin/env python3

import sys, pickle, atexit
import socket
import tkinter as tk
from PIL import ImageTk
from queue import Queue
from threading import Thread, Event

def logger(message, logging=False):
    if logging:
        f = open('SOCKETTEST.log', 'a')
        f.write(message + '\n')
        f.close()

class App():
    EXIT_CODE = b'\x00'
    PICTURE_CODE = b'\x01'
    ExitCode = 'exit'

    def __init__(self):
        self.root = tk.Tk()
        self.imageQueue = Queue()
        stopEvent = Event()
        self.showThread = Thread(target=self.showImages, args=(stopEvent,), daemon=True)
        self.showThread.start()
        self.listenThread = Thread(target=self.listener, args=(stopEvent,), daemon=True)
        self.listenThread.start()
        atexit.register(self.stopBackground, stopEvent, self.showThread)
        atexit.register(self.stopBackground, stopEvent, self.listenThread)
        self.root.protocol("WM_DELETE_WINDOW", self.windowClosed)
        self.root.mainloop()

    def listener(self, event):
        # Open socket on unused port 
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(('', 0))
        port = self.sock.getsockname()[1]
        logger(f'Port will be {port}')

        # Write port on stdout - should be read via pipes by parent process
        logger('About to write port to stdout')
        print(port)
        sys.stdout.flush()
        logger('finished writing port')

        # Ready start work...  Listen for connections
        backlog = 5
        self.sock.listen()#backlog)

        logger('About to accept on socket')
        self.client, address = self.sock.accept()
        logger('About to start main loop')
        while not event.is_set():
            logger('Waiting to receive message...')
            opCode = self.client.recv(1)
            logger(f'Just read something: {opCode}')
            if len(opCode) == 0 or opCode == self.EXIT_CODE:
                logger('Exiting')
                self.imageQueue.put('exit')
                self.client.close()
                return
                #exit()
            elif opCode == self.PICTURE_CODE:
                logger('Getting a picture')
                data = sys.stdin.buffer.read(8)
                dataLen = int.from_bytes(data, byteorder='big')
                logger(f'I need to read {dataLen} bytes')
                pkg = sys.stdin.buffer.read(dataLen)
                logger(f'I just read {len(pkg)} bytes')
                picture = pickle.loads(pkg)
                self.imageQueue.put(picture)
                logger('Image was put into queue')
            else:
                logger('Unknown opCode')

    def showImages(self, event):
        logger('Show thread has started')
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack()
        imageID = None
        while not event.is_set():
            picture = self.imageQueue.get()
            logger('Possible image found on queue...')
            logger(f'  Type: {type(picture)}')
            logger(f'  Value: {picture}')
            if isinstance(picture, str) and picture == self.ExitCode:
                logger('not an image - exit code')
                #self.root.destroy()
                return
            try:
                logger('must be an image')
                self.root.title(picture.getTitle())
                image = ImageTk.PhotoImage(picture.getImage())
                self.canvas.config(width=picture.getWidth(),
                                   height=picture.getHeight())        
                if imageID is None:
                    logger('showing a new image')
                    imageID = self.canvas.create_image(0, 0, anchor=tk.NW,
                                                       image=image)
                else:
                    logger('repainting exisiting image')
                    self.canvas.itemconfig(imageID, image=image)
            except AttributeError:
                logger('Attribute Error encountered')
                #pass

    def stopBackground(self, event, thread):
        """Handle Python exiting"""
        event.set()
        self.imageQueue.put(self.ExitCode)
        try:
            self.client.close()
        except:
            pass
        try:
            self.sock.close()
        except:
            pass
        #thread.join()
        logger('stopBackground: Exit')
        exit()
    
    def windowClosed(self):
        """Handle GUI window close event"""
        logger('windowClosed')
        self.imageQueue.put(self.ExitCode)  # Signal stop to showImage thread
        #self.listenThread.join()
        #self.listenThread._stop()
        try:
            self.client.close()
        except:
            pass
        try:
            self.sock.close()
        except:
            pass
        try:
            self.root.destroy()
            del self.root
        except AttributeError:
            pass
        exit()

if __name__ == '__main__':
    app = App()
