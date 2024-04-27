from langdetect import detect
import re
from collections import defaultdict
import nltk
from nltk.corpus import stopwords
import string
import math
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class AdvancedTextAnalyzer():
    def __init__(self,text):
        self.__text=re.sub(r'\s+', ' ', text)
        #Extraction des phrases cette méthode de split en donnant le pattern je l'ai testé ça marche
        self.__sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', self.text)
        self.__Idf = self.calculateIdf(self.__sentences)

    #Getters
    @property
    def text(self):
        return self.__text
    @property
    def sentences(self):
        return self.__sentences
    @property
    def Idf(self):
        return self.__Idf

    #Check if wor is stopWord
    def isStop(self, word):
        nltk.download("stopwords")
        stp_word = set(stopwords.words("english"))

        if word.lower() in stp_word:
            return True
        else:
            return False
        
    def tf(self, terme, sentence):
        lowr_sntce = sentence.lower()
        lwr_terme = terme.lower()
        return lowr_sntce.count(lwr_terme)

    def calculateIdf(self, sentences):
        total = len(sentences)

        # Nembre de phrases contenant un mot
        freq = {}

        Idf = {}

        # calcule des frequences de chaque mot
        for i in range(len(sentences)):
            words = sentences[i].split(" ")
            for word in words:

                #Enlever la ponctuation
                if word[-1] in string.punctuation:
                    word = word[:-1]

                # Rendre tous les lettres en minuscule
                word = word.lower()
                
                if not self.isStop(word):
                    if word not in freq:
                        freq[word] = 1

                        # Calculer le nembre de phrases contenant word
                        for j in range(len(sentences)):
                            if j!=i:
                                lowr_sntnce = sentences[j].lower()
                                if word in lowr_sntnce:
                                    freq[word] +=1
        #Calcule de IDF
        for word in freq:
            word = word.lower()
            Idf[word] = math.log(total/freq[word])

        return Idf

    def prodScalaire(self, phrase1, phrase2):
        score=0

        words1 = phrase1.lower().split(" ")
        words2 = phrase2.lower().split(" ")

        passed = set()

        for word in words1+words2:
            if not self.isStop(word):
                #Enlever la ponctuation
                if word[-1] in string.punctuation:
                    word = word[:-1]

                if not word in passed:
                    score += self.tf(word, phrase1)*self.tf(word, phrase2)*(self.Idf[word])**2
                    passed.add(word)
        return score

    def norme(self, phrase):
        score = 0
        words = phrase.lower().split(" ")

        for word in words:
            if not self.isStop(word):
                #Enlever la ponctuation
                if word[-1] in string.punctuation:
                    word = word[:-1]

                score += (self.tf(word, phrase)*self.Idf[word])**2

        return math.sqrt(score)


    def calculate_sentence_similarity(self, phrase1,phrase2):
        top = self.prodScalaire(phrase1, phrase2)
        bottom = self.norme(phrase1)*self.norme(phrase2)

        return (top/bottom)





    def Analyse_text(self):
            # initialisation du graphe
        graph = defaultdict(list)
        print("I'm theeere")

        for i, sentence_i in enumerate(self.sentences):
            for j, sentence_j in enumerate(self.sentences):
                if i != j:
                # Il faut qu'on implemente cette fonction nommée calculate..... pour calculer similarity entre deux phrases en se basant sur l'une des méthodes
                    similarity = self.calculate_sentence_similarity(sentence_i, sentence_j)
                    #pour implementer cette fonction il nous faut tf et idf des mots dans cette phrase donc il faut qu'on fait un pre processing a la phrase pour supprimer stop wordq les mots neutres....
                
    
                    if similarity > 0.001:  # comment va t-on determiner les phraes adjoints dans le graph ,par excemple on met un seuil pour le score si le score depasse ce seuil alors on va connecter les deux nodesc a d les deux phrases
                        graph[i].append((similarity ,j))
        
        #Affichage du graph
       
        G = nx.DiGraph()

        for node in range(len(self.sentences)):
            G.add_node(node)

           
        print(graph.items())
        for i, edges in graph.items():
            for similarity, j in edges:
                G.add_edge(i, j, weight=similarity)

        # Afficher le graphique
        pos = nx.spring_layout(G) 
        nx.draw_networkx_nodes(G, pos, node_size=300)  # Dessiner les nœuds
        nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5) 
        nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')  # Dessiner les étiquettes des nœuds
        labels = nx.get_edge_attributes(G, 'weight')  
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)  
        plt.show()

        return graph

    