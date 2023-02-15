import pandas as pd
from data_processing import parse_data, rescale


if __name__ == '__main__':

    # Reading data
    raw_data = pd.read_csv('Prostate_Cancer.csv')

    # Data processing
    clean_data = parse_data(raw_data)

    # Data standardization
    rescaled_data = rescale(clean_data)
