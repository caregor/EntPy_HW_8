"""
    ---Task 2---
    Задание №6
Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
 * Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
 * Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
"""
import os
import csv
import pickle


def pickle2csv(pickle_filepath):
    csv_filepath = os.path.splitext(pickle_filepath)[0] + '.csv'
    with open(pickle_filepath, 'rb') as pickle_file:
        try:
            data = pickle.load(pickle_file)
            if not isinstance(data, list):
                raise TypeError("Invalid data format in pickle file. Expected a list of dictionaries.")

            # Получаем заголовки столбцов из ключей словаря
            fieldnames = list(data[0].keys())

            with open(csv_filepath, 'w', newline='') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                # Записываем заголовки в CSV файл
                writer.writeheader()

                # Записываем данные из списка словарей в CSV файл
                writer.writerows(data)

            print(f"Converting {pickle_filepath} to {csv_filepath} is complete.")
        except pickle.UnpicklingError as e:
            print(f"Error unpickling {pickle_filepath}: {e}")
        except Exception as e:
            print(f"Error converting {pickle_filepath} to CSV: {e}")