# -*- coding: utf-8 -*-

import os
import jieba
import jieba.posseg as pseg


class Word(object):
    def __init__(self, token, pos):
        self.token = token
        self.pos = pos


class Tagger:
    def __init__(self, path="vocab/"):
        # TODO vocab_name_pos.txt
        files = os.listdir(path)
        for file in files:
            if "vocab" in file:
                jieba.load_userdict(os.path.join(path, file))

        # TODO splits.txt
        with open(os.path.join(path, "splits.txt"), mode="r", encoding="utf-8") as fp:
            for line in fp.readlines():
                token1, token2 = line.split()
                jieba.suggest_freq((token1, token2), True)

    @staticmethod
    def get_word_objects(sentence):
        return [Word(word, tag) for word, tag in pseg.cut(sentence)]
