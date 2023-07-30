"""
    ---Task 1 ---
    Задание №5
    Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде
одноимённых pickle файлов.
"""
import os
import json
import pickle


def convert_json_to_pickle(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if filepath.lower().endswith('.json') and os.path.isfile(filepath):
            name_without_extension = os.path.splitext(filename)[0]
            pickle_file = name_without_extension + '.pickle'
            pickle_filepath = os.path.join(directory, pickle_file)

            with open(filepath, 'r', encoding='utf-8') as json_file:
                try:
                    json_data = json.load(json_file)
                    with open(pickle_filepath, 'wb') as pickle_out:
                        pickle.dump(json_data, pickle_out)

                    print(f'Converting "{filename}" to "{pickle_file}" is complete.')
                except json.JSONDecodeError as e:
                    print(f'Error decoding JSON file "{filename}": {e}')
                except Exception as e:
                    print(f'Error converting "{filename}" to pickle: {e}')