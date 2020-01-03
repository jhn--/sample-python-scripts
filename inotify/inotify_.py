#!/usr/bin/env python

import os, sys, logging, time
from operator import itemgetter
from threading import Thread, Lock
from watchdog.observers import Observer
from watchdog.observers.inotify import InotifyEmitter
from watchdog.events import FileSystemEventHandler, LoggingEventHandler

logging.basicConfig(format = '%(asctime)s %(levelname)s %(lineno)03d: %(message)s',
                    datefmt = '%s', 
                    level = getattr(logging, os.environ.get('LOGGING_LEVEL', 'DEBUG'), 'INFO'))
# me = os.path.basename(sys.argv[0]).replace('.py', '')
# L = logging.getLogger(me)

path = sys.argv[1] if len(sys.argv) > 1 else '/tmp'

'''
logging_event_handler = LoggingEventHandler()
observer = Observer()
observer.schedule(logging_event_handler, path, recursive = True)
'''
'''
class newfiles(FileSystemEventHandler):
    def on_any_event(self, event):
        if isinstance(event, (FileCreatedEvent, DirCreatedEvent)):
            path = os.path.abspath(event.src_path)
            answer = os.system("file '%s") % path
            return answer
        else:
            pass
'''

class myHandler(FileSystemEventHandler):
    def on_created(self, event):
        print("event is {0}").format(event)
        path = os.path.abspath(event.src_path)
        answer = os.system("file '%s'" % path)
        return answer

event_handler = myHandler()
observer = Observer()
ANSWER = observer.schedule(event_handler, path, recursive = True)
print(ANSWER)
observer.start()
try:
    while True:
        time.sleep(1)
        print('a')
except KeyboardInterrupt:
    observer.stop()
observer.join()