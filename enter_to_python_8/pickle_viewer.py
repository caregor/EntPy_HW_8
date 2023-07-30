import pickle


def view_pickle_data(pickle_filepath):
    with open(pickle_filepath, 'rb') as pickle_file:
        try:
            data = pickle.load(pickle_file)
            print(data)
        except pickle.UnpicklingError as e:
            print(f"Error unpickling {pickle_filepath}: {e}")
        except Exception as e:
            print(f"Error viewing data from {pickle_filepath}: {e}")