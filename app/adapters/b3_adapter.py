import mmap
import os
from datetime import datetime

from app.interfaces.b3_interface import B3Interface


class B3Adapter(B3Interface):
    def read_data_from_b3(self, file_path):
        b3_data = {}
        files = [f for f in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, f))]
        for file in files:
            self.read_csv(b3_data, file, file_path)
        b3_consolidated_data = []
        for business_date in b3_data:
            for ticker in b3_data[business_date]:
                b3_consolidated_data.append({
                    'business_date': datetime.strptime(business_date, "%Y-%m-%d"),
                    'ticker': ticker,
                    'max_range_value': b3_data[business_date][ticker]['max_range_value'],
                    'max_daily_volume': b3_data[business_date][ticker]['max_daily_volume'],
                })
        return b3_consolidated_data

    def read_csv(self, b3_data, file, file_path):
        start_time = datetime.now()
        with open(os.path.join(file_path, file)) as csv_file:
            print(f'Iniciando leitura do arquivo {file} - {datetime.now() - start_time}')
            lines_read = []
            with mmap.mmap(csv_file.fileno(), 0, access=mmap.ACCESS_READ) as mm:
                mm.readline()
                for line in iter(mm.readline, b""):
                    lines_read.append(line)
                print(f'Finalizando leitura do arquivo {file} - {datetime.now() - start_time}')
        self.process_lines(b3_data, lines_read)
        print(f'Finalizando processamento do arquivo {file} - {datetime.now() - start_time}')

    def process_lines(
        self,
        b3_data,
        lines_read
    ):
        start_time = datetime.now()
        for line in lines_read:
            row = line.decode("utf-8").split(";")
            self.create_dict_structure(b3_data, row)
            row_volume = int(row[4])
            if row_volume > b3_data[row[0]][row[1]]['max_daily_volume']:
                b3_data[row[0]][row[1]]['max_daily_volume'] = row_volume
            row_qty = float(row[3].replace(',', '.'))
            if row_qty > b3_data[row[0]][row[1]]['max_range_value']:
                b3_data[row[0]][row[1]]['max_range_value'] = row_qty
        print(f'Finalizando processamento de linhas - {datetime.now() - start_time}')

    @staticmethod
    def create_dict_structure(b3_data, row):
        if row[0] not in b3_data:
            b3_data[row[0]] = {}
        if row[1] not in b3_data[row[0]]:
            b3_data[row[0]][row[1]] = {
                'max_range_value': 0,
                'max_daily_volume': 0,
            }
