"""
    ---Task 3---
    Задание №7
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Распечатайте его как pickle строку.
"""
import csv
import pickle


def read_csv2pickle_str(csv_filepath):
    data_list = []
    with open(csv_filepath, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        fieldnames = next(csv_reader)

        for row in csv_reader:
            data_list.append(dict(zip(fieldnames, row)))
    pickle_string = pickle.dumps(data_list)

    return pickle_string
