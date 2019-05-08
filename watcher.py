import time
import distutils.dir_util
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Watcher:
    def __init__(self):
        self.observer = Observer()
        self.directory_to_watch = "C:\\_D\\copy\\src"
        self.directory_to_destination = "C:\\_D\\copy\\destination"

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.directory_to_watch)
        self.observer.start()
        print("Watching...")
        self.observer.join()


class Handler(FileSystemEventHandler):
    w = Watcher()
    @staticmethod
    def on_any_event(event):

        if event.is_directory:
            return None
        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print("Created event - %s." % event.src_path)
            try:
                distutils.dir_util.copy_tree(w.directory_to_watch, w.directory_to_destination)
            except WindowsError as ex:
                print("Error:", ex)

        elif event.event_type == 'modified':
            # If the file is modified, this will be executed
            print("Received modified event - %s." % event.src_path)


if __name__ == '__main__':
    w = Watcher()
    w.run()
