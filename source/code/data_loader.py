import pandas as pd


def load_data(data_path):
    with open(data_path, 'r') as source:
        lines = source.readlines()
    return lines