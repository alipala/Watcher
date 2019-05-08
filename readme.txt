https://www.michaelcho.me/article/using-pythons-watchdog-to-monitor-changes-to-a-directory

previous code

class Watcher:

    def __init__(self):
        self.observer = Observer()
        # self.directory_to_watch = str(input("Enter watch directory like(C:\copy\src): "))
        # self.directory_to_destination = str(input("Enter destination directory like(C:\copy\dest): "))
        self.directory_to_watch = "C:\\_D\\copy\\src"
        self.directory_to_destination = "C:\\_D\\copy\\destination"

    def run(self):
        event_handler = FileSystemEventHandler()
        self.observer.schedule(event_handler, self.directory_to_watch)
        self.observer.start()
        print("Watching...")
        try:
            while True:
                time.sleep(2)
        except WindowsError as e:
            print("Error: ", e)
            self.observer.stop()
        self.observer.join()




class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print("Created event - %s." % event.src_path)

            try:
                distutils.dir_util.copy_tree(self.directory_to_watch, self.directory_to_destination)
            except WindowsError as ex:
                print("Error:", ex)
            except OSError as f:
                print("Error:", f)
        elif event.event_type == 'modified':
            # If the file is modified, this will be executed
            print("Received modified event - %s." % event.src_path)


if __name__ == '__main__':
    w = Watcher()
    w.run()
