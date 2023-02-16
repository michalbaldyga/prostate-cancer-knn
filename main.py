import pandas as pd
from data_processing import parse_data, rescale, split_data
from constants import SPLIT_RATIO, K_NEAREST_NEIGHBOR
from classifier import knn
from collections import defaultdict


if __name__ == '__main__':

    # Reading data
    raw_data = pd.read_csv('Prostate_Cancer.csv')

    # Data processing
    clean_data = parse_data(raw_data)

    # Data standardization
    rescaled_data = rescale(clean_data)

    # Splitting data
    train_set, test_set = split_data(rescaled_data, SPLIT_RATIO)

    # Classification
    wrong_predicts = 0
    confusion_matrix = defaultdict(int)

    for patient in test_set:
        predicted = knn(K_NEAREST_NEIGHBOR, train_set, patient.point)
        actual = patient.label
        if actual != predicted:
            wrong_predicts += 1

        confusion_matrix[(predicted, actual)] += 1

    # Results
    print("Accuracy: " + str((len(test_set) - wrong_predicts) / len(test_set)))
    print(confusion_matrix)
