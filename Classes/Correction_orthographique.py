from textblob import TextBlob


class Correction_orthographique():

    def __init__(self,text):
        self.text=text
    
    def Correction(self,text):
        b = TextBlob(text)
        print("texte corrigé:\n", str(b.correct()))
