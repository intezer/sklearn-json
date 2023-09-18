import joblib

import sklearn_json

path_to_old_joblib = ''
path_to_json = ''
path_to_new_joblib = ''


def to_json():
    model = joblib.load(path_to_old_joblib)

    sklearn_json.to_json(model, path_to_json)


def to_joblib():
    model = sklearn_json.from_json(path_to_json)
    joblib.dump(model,
                path_to_new_joblib,
                compress=3)


if __name__ == '__main__':
    # Run on old environment
    to_json()

    # Run on new environment
    #to_joblib()
