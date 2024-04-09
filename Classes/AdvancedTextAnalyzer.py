from langdetect import detect
import re
from collections import defaultdict
import nltk
from nltk.corpus import stopwords
import string
import math
import numpy as np

class AdvancedTextAnalyzer():
    def __init__(self,text):
        self.__text=re.sub(r'\s+', ' ', text)
        #Extraction des phrases cette méthode de split en donnant le pattern je l'ai testé ça marche
        self.__sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', self.text) 

    #Getters
    @property
    def text(self):
        return self.__text
    @property
    def sentences(self):
        return self.__sentences

    def calculate_tf_idf(sentences):
        total = len(sentences)

        # Nembre de phrases contenant un mot
        freq = {}

        Idf = {}

        tf = {}

        nltk.download("stopwords")
        stp_word = set(stopwords.words("english"))

        # calcule des frequences de chaque mot
        for i in range(len(sentences)):
            words = sentences[i].split(" ")
            for word in words:

                #Enlever la ponctuation
                if word[-1] in string.punctuation:
                    word = word[:-1]

                # Rendre tous les lettres en minuscule
                word = word.lower()
                
                if word not in stp_word:
                    if word not in freq:
                        freq[word] = 1

                        # Calculer le nembre de phrases contenant word
                        for j in range(len(sentences)):
                            if j!=i:
                                lowr_sntnce = sentences[j].lower()
                                if word in lowr_sntnce:
                                    freq[word] +=1

                    # Calculer la frequence du termes dans chaque phrase
                    if word not in tf:
                        tf[word] = np.zeros(len(sentences))
                        lowr_sntnce = sentences[i].lower()
                        tf[word][i] = lowr_sntnce.count(word)

                        for j in range(len(sentences)):
                            if j!=i:
                                if word in sentences[j]:
                                    lowr_sntnce = sentences[j].lower()
                                    tf[word][j] = lowr_sntnce.count(word)
        #Calcule de IDF
        for word in freq:
            Idf[word] = math.log(total/freq[word])

        return Idf, tf
        


    def calculate_sentence_similarity(phrase1,phrase2):
        score=0
        #on va l'implementer en se basant sur la methode qui prend tf et idf des mots de chaque phrase
        return score





    def Analyse_text(self):
            # initialisation du graphe
        graph = defaultdict(list)
        for i, sentence_i in enumerate(self.sentences):
            for j, sentence_j in enumerate(self.sentences):
                if i != j:
                # Il faut qu'on implemente cette fonction nommée calculate..... pour calculer similarity entre deux phrases en se basant sur l'une des méthodes
                    similarity = self.calculate_sentence_similarity(sentence_i, sentence_j)
                    #pour implementer cette fonction il nous faut tf et idf des mots dans cette phrase donc il faut qu'on fait un pre processing a la phrase pour supprimer stop wordq les mots neutres....
                
    
                    if similarity > 0.2:  # comment va t-on determiner les phraes adjoints dans le graph ,par excemple on met un seuil pour le score si le score depasse ce seuil alors on va connecter les deux nodesc a d les deux phrases
                        graph[i].append((similarity ,j))
    
        return graph

    