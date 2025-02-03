import os
import time
import pandas as pd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class SierraDataHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith(".scid"):
            try:
                df = pd.read_csv(event.src_path)
                print(f"📊 Loaded {len(df)} rows from {os.path.basename(event.src_path)}")
                return df
            except Exception as e:
                print(f"❌ Error reading {os.path.basename(event.src_path)}: {str(e)}")

class DenaliDataFeed:
    def __init__(self):
        self.data_dir = os.path.expanduser("~/sierra_data")
        os.makedirs(self.data_dir, exist_ok=True)
        self.event_handler = SierraDataHandler()
        self.observer = Observer()
        self.observer.schedule(self.event_handler, path=self.data_dir, recursive=False)
        self.observer.start()
        print(f"🔍 Watching directory: {self.data_dir}")
        print(f"📂 Directory contents: {os.listdir(self.data_dir)}")

    def stream_order_book(self):
        while True:
            test_file = os.path.join(self.data_dir, "ES_test.scid")
            pd.DataFrame({
                'timestamp': [pd.Timestamp.now().floor('1s')],
                'price': [4500 + (time.time() % 10)],
                'volume': [100]
            }).to_csv(test_file, index=False)
            
            time.sleep(5)
