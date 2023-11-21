import csv
class DataIterator:
    def __init__(self, csv_filename):
        self.csv_filename = csv_filename
        self.data_iter = self.data_generator()

    def data_generator(self):
        with open(self.csv_filename, newline='') as f:
            fieldnames = ['data', 'temp_morning', 'presure_morning', 'wind_morning', 'temp_evening', 'presure_evening', 'wind_evening']
            reader = csv.DictReader(f, fieldnames=fieldnames)
            for row in reader:
                date = row['data']
                data = {
                    "data": date,
                    "temp_morning": row['temp_morning'],
                    "presure_morning": row['presure_morning'],
                    "wind_morning": row['wind_morning'],
                    "temp_evening": row['temp_evening'],
                    "presure_evening": row['presure_evening'],
                    "wind_evening": row['wind_evening']
                }
                yield data

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.data_iter)
        except StopIteration:
            raise StopIteration


csv_filename = 'dataset.csv'
data_iter = DataIterator(csv_filename)


try:
    next_data = next(data_iter)
    if next_data:
        print(next_data)
    else:
        print("don't database.")
except StopIteration:
    print("don't database.")
try:
    next_data = next(data_iter)
    if next_data:
        print(next_data)
    else:
        print("don't database.")
except StopIteration:
    print("don't database.")