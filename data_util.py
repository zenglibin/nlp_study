# _*_ coding:utf-8 _*_
import os
import numpy as np
import getConfig

gConfig = {}
gConfig = getConfig.get_config(config_file='config.ini')

UNK = "__UNK__"
START_VOCABULART = [UNK]
UNK_ID = 3


def create_vocabulary(inpud_file, vocabulary_size, output_file):
    vocabulary = {}
    k = int(vocabulary_size)
    with open(inpud_file, 'r') as f:
        counter = 0
        for line in f:
            counter += 1
            tokens = [word for word in line.split()]
            for word in tokens:
                if word in vocabulary:
                    vocabulary[word] += 1
                else:
                    vocabulary[word] = 1
        vocabulary_list = START_VOCABULART + sorted(vocabulary, key=vocabulary.get, reverse=True)

        if len(vocabulary_list) > k:
            vocabulary_list = vocabulary_list[:k]





# print(gConfig)