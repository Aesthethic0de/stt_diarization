import csv

class TxtConversion:
    def __init__(self, txt_file_path: str, csv_file_path: str):
        self.txt_file_path = txt_file_path
        self.csv_file_path = csv_file_path

    def convert_to_csv(self):
        with open(self.txt_file_path, 'r') as in_file:
            stripped = (line.strip() for line in in_file)
            lines = (line.split(",") for line in stripped if line)
            with open(self.csv_file_path, 'w') as out_file:
                writer = csv.writer(out_file)
                writer.writerows(lines)