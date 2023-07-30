from enter_to_python_8 import convert_json_to_pickle, pickle2csv, view_pickle_data


if __name__ == '__main__':
#task 1
    directory_path = 'data'
    convert_json_to_pickle(directory_path)
#task 2
    pickle_filepath = 'data/new_users.pickle'
    view_pickle_data(pickle_filepath)
    pickle2csv(pickle_filepath)
