import json
import pickle

__locations = None
__data_columns = None
__model = None

def get_location_names():
    return __locations

def load_saved_artifacts():
    print('loading the artifacts...')
    global __data_columns
    global __locations

    with open("D:/git/banglore/server/artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[3:]

    with open("D:/git/banglore/server/artifacts/banglore_home_prices_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print('Loading the artifacts done!')

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
