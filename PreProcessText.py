import nltk
from nltk.corpus import stopwords

class PreProcessText():
    nltk.download("stopwords")
    def __init__(self, text):
        self.__text = text

    def 