from enter_to_python_8 import *

if __name__ == '__main__':
    # task 1
    directory_path = 'data'
    convert_json2pickle(directory_path)

    # task 2
    pickle_filepath = 'data/new_users.pickle'
    view_pickle_data(pickle_filepath)
    pickle2csv(pickle_filepath)

    # task 3
    csv_filepath = 'data/new_users.csv'
    pickle_string = read_csv2pickle_str(csv_filepath)
    print(pickle_string)

    # task 4 // Результат - Создается папка "export" с json, csv, pickle файлами
    directory_path = 'data'  # путь к директории, которую нужно обойти
    explore_directory_to_json(directory_path)
    # Используем свою функцию конвертации из json в pickle
    directory_path = 'export'
    convert_json2pickle(directory_path)

    # Используем свою функцию конвертации из pickle в csv
    pickle_filepath = 'export/results.pickle'
    view_pickle_data(pickle_filepath)
    pickle2csv(pickle_filepath)
