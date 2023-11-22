import csv

def create_x_and_y():
    with open('dataset.csv', newline='') as f:
        fieldnames = ['data', 'temp_morning', 'presure_morning','wind_morning', 'temp_evening', 'presure_evening', 'wind_evening']
        reader = csv.DictReader(f, fieldnames=fieldnames)
        for row in reader:
            file_writer = csv.writer(open('dataset-number.csv', 'a', newline=''), lineterminator="\r")
            file_writer.writerow([row['data']])
            file_writer = csv.writer(open('dataset-data.csv', 'a', newline=''), lineterminator="\r")
            file_writer.writerow([row["temp_morning"],row["presure_morning"],row["wind_morning"],row["temp_evening"],row["presure_evening"],row["wind_evening"]])
if __name__ == '__main__':
    create_x_and_y()