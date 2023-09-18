import numpy as np
from sklearn.metrics import pairwise_distances
from utils import validate_params


@validate_params
def connectivity(X, labels, neighbors=10, metric="euclidean"):
    distances = pairwise_distances(X, metric=metric)
    nearest = distances.argsort(axis=0)[1 : (neighbors + 1), :]
    nrow, ncol = nearest.shape
    replicated_indexes = np.tile(labels, (nrow, 1))
    sorted_labels = labels[nearest]
    arr = replicated_indexes != sorted_labels
    return (arr * np.tile(np.array(1 / np.arange(1, neighbors + 1)), (ncol, 1)).T).sum()
