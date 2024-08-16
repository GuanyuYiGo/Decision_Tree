from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
from math import log
import operator
import pickle


def create_dataset():
    dataset = [[0, 0, 0, 0, "no"],
               [0, 0, 0, 1, "no"],
               [0, 1, 0, 1, "yes"],
               [0, 1, 1, 0, "yes"],
               [0, 0, 0, 0, "no"],
               [1, 0, 0, 0, "no"],
               [1, 0, 0, 1, "no"],
               [1, 1, 1, 1, "yes"],
               [1, 0, 1, 2, "yes"],
               [1, 0, 1, 2, "yes"],
               [2, 0, 1, 2, "yes"],
               [2, 0, 1, 1, "yes"],
               [2, 1, 0, 1, "yes"],
               [2, 1, 0, 2, "yes"],
               [2, 0, 0, 0, "no"]]
    labels = ['F1-AGE', 'F2-WORK', 'F3-HOME', 'F4-LOAN']
    return dataset, labels


def create_tree(dataset, labels, feat_labels):
    class_list = [example[-1] for example in dataset]
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]
    if len(dataset[0]) == 1:
        return majority_count(class_list)
    best_feat = choose_best_feature(dataset, labels)
    best_feat_labels = feat_labels[best_feat]
    mytree = {best_featlabel: {}}
    del (labels[best_feat])
    feat_values = [example[best_feat] for example in dataset]
    uniquevals = set(feat_values)
    for value in uniquevals:
        mytree[best_featlabel][value] = create_tree(split_data(dataset, best_feat, value), labels, featlabels)