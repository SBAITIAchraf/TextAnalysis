from langdetect import detect
import re
from collections import defaultdict

#La detection de la langue
class Language_detector():
    def __init__(self,text):
        self.text=text

    def detection_de_la_langue(self):
        langue=detect(self.text)
        return langue
        