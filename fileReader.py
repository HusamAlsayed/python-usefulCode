import json
import pandas as pd


def read_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def write_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


def write_csv(data, file_path):
    data.to_csv(file_path)


def read_txt(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def read_csv(file_path):
    return pd.read_csv(file_path)


def read_excel(file_path):
    return pd.read_excel(file_path)


def read(file_path):
    extension = file_path.split('.')[-1]

    return read_dct[extension](file_path)


def write(data, file_path):
    extension = file_path.split('.')[-1]

    return write_dct[extension](data, file_path)


read_dct = {
    'csv': read_csv,
    'xlsx': read_excel,
    'txt': read_txt,
    'json': read_json
}

write_dct = {
    'csv': write_csv,
    'json': write_json
}
