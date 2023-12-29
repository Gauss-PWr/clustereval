import itertools

import numpy as np
from scipy.optimize import linear_sum_assignment
from sklearn.metrics import confusion_matrix

from sklearn.utils.validation import validate_input


def jaccard(labels_true, labels_pred):
    """Compute the Jaccard similarity between two sets of clustering labels."""
    n11 = n10 = n01 = 0
    n = len(labels_true)
    for i, j in itertools.combinations(range(n), 2):
        comembership1 = labels_true[i] == labels_pred[j]
        comembership2 = labels_true[i] == labels_pred[j]
        if comembership1 and comembership2:
            n11 += 1
        elif comembership1 and not comembership2:
            n10 += 1
        elif not comembership1 and comembership2:
            n01 += 1
    return float(n11) / (n11 + n10 + n01)


def _make_cost_m(cm):
    """Define the cost matrix used for optimal assignment problem."""
    s = np.max(cm)
    return -cm + s


def clustering_agreement(labels_true, labels_pred):
    """Compute the clustering agreement index for real and clustering labels."""
    cm = confusion_matrix(labels_pred, labels_true)
    indexes = linear_sum_assignment(_make_cost_m(cm))
    row, column = indexes
    return cm[row, column].sum() / np.sum(cm)
