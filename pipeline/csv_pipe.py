import csv, pathlib

class CSVPipe:
    def __init__(self, filename: str):
        self.f = open(pathlib.Path(filename), 'w', encoding='utf-8-sig', newline='')
        self.writer = None

    def write_one(self, item: dict):
        if self.writer is None:
            self.writer = csv.DictWriter(self.f, fieldnames=item.keys())
            self.writer.writeheader()
        self.writer.writerow(item)

    def close(self):
        self.f.close()