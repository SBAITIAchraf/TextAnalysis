from langdetect import detect

#La detection de la langue
class Language_detector():

    languages = {"ar": "arabic",
                "en": "english",
                "fr": "french"}
    def __init__(self,text):
        self.__lang = Language_detector.languages[detect(text)]

    # getters
    @property
    def lang(self):
        return self.__lang
    
det = Language_detector("Hello there")
