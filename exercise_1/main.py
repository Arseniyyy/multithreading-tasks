import os
import csv
import threading
from time import sleep
from functools import reduce


all_values = []

def convert_to_csv():
    """Converts from .dat to .csv"""
    for path in os.listdir('./'):
        filename, file_extension = os.path.splitext(path)

        if file_extension == '.dat':
            with open(filename + file_extension) as infile, open(f'{filename}.csv', 'w') as outfile:            
                csv_writer = csv.writer(outfile)
                prev = ''

                for line in infile.read().splitlines():
                    csv_writer.writerow([line, prev])
                    prev = line

def make_different_operations():
    """Makes mathematical operations.
    Opearations:
    1. Addition
    2. Multiplication
    3. Sum of squares
    """
    for path in os.listdir('./'):
        filename, ext = os.path.splitext(path)

        if ext == '.csv':
            with open(f'{filename}.csv') as f:
                reader = list(csv.reader(f))

                operation = reader[0][0]
                values = reader[2][0].split()

                if operation == '1':
                    # addition
                    cumulation = sum(list(map(float, values)))
                    all_values.append(cumulation)

                if operation == '2':
                    # multiplication
                    multiplied = reduce((lambda x, y: x * y), list(map(float, values)))

                    all_values.append(multiplied)

                if operation == '3':
                    # sum of squares
                    values = list(map(float, values))
                    values = sum([x ** 2 for x in values])

                    all_values.append(values)

def write_out_csv():
    """Adds values in out.csv file"""
    with open('out.csv', 'w') as writeable_file:
        writer = csv.writer(writeable_file, delimiter=';')
        writer.writerow(all_values)

# thread1 = threading.Thread(target=write_out_csv, args=())
# thread1.start()

convert_to_csv()
make_different_operations()
write_out_csv()
