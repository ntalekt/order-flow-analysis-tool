import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class SierraDataHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith(".scid"):
            print(f"Detected changes in: {event.src_path}")


class DenaliDataFeed:
    def __init__(self, product="ES"):
        # Create directory if needed
        self.data_dir = os.path.expanduser("~/sierra_data")
        os.makedirs(self.data_dir, exist_ok=True)

        self.event_handler = SierraDataHandler()
        self.observer = Observer()
        self.observer.schedule(self.event_handler, path=self.data_dir, recursive=False)
        self.observer.start()

    def stream_order_book(self):
        while True:
            yield {"bids": [], "asks": []}  # Dummy data
            time.sleep(1)
