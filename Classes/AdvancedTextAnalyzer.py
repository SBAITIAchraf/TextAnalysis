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


class NodeInTheNetwork:
    def __init__(self, node_id, eigenvector_centrality,phrase):
        self.node_id = node_id
        self.phrase=phrase
        self.eigenvector_centrality = eigenvector_centrality
       




class AdvancedTextAnalyzer():

    languages = {"ar": "arabic",
                    "en": "english",
                    "fr": "french"}

    def __init__(self,text):

        
        self.__text=re.sub(r'\s+', ' ', text)
        #Extraction des phrases cette méthode de split en donnant le pattern je l'ai testé ça marche
        self.__sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', self.text)
        self.__lang = self.languages[detect(text)]
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
    @property
    def lang(self):
        return self.__lang

    #Check if wor is stopWord
    def isStop(self, word):
        stp_word = set(stopwords.words(self.__lang))

        if word.lower() in stp_word:
            return True
        else:
            return False
        
    
    def check_word(self, word):

        if len(word) != 0:

            if word[-1] in string.punctuation:
                word = word[:-1]

            if word[0] in string.punctuation:
                word = word[1:]

            # Rendre tous les lettres en minuscule
            word = word.lower()
            if not self.isStop(word):
                return word, True
        return word, False
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

                word, is_clear = self.check_word(word)
                if is_clear:
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

            word, is_clear = self.check_word(word)
            if is_clear:
                if not word in passed:
                    score += self.tf(word, phrase1)*self.tf(word, phrase2)*(self.Idf[word])**2
                    passed.add(word)
        return score

    def norme(self, phrase):
        score = 0
        words = phrase.lower().split(" ")

        for word in words:
            word, is_clear = self.check_word(word)
            if is_clear:

                score += (self.tf(word, phrase)*(self.Idf[word])**2)

        return math.sqrt(score)


    def calculate_sentence_similarity(self, phrase1,phrase2):
        top = self.prodScalaire(phrase1, phrase2)
        bottom = self.norme(phrase1)*self.norme(phrase2)

        return (top/bottom)





    def Analyse_text(self,p):
        G = nx.DiGraph()
        # Initialize the graph with nodes
        for node in range(len(self.sentences)):
            G.add_node(node)

        # Calculate the sentence similarity and construct the graph
        graph = defaultdict(list)
        for i, sentence_i in enumerate(self.sentences):
            for j, sentence_j in enumerate(self.sentences):
                if i != j:
                    similarity = self.calculate_sentence_similarity(sentence_i, sentence_j)
                    graph[i].append((similarity, j))

        # Calculate eigenvector centrality after constructing the graph
        eigenvector_centralities = nx.eigenvector_centrality_numpy(G)
        print(eigenvector_centralities)

        # Create instances of NodeInTheNetwork and sort them
        nodes_in_the_network = []
        for node in range(len(self.sentences)):
            nod = NodeInTheNetwork(node, eigenvector_centralities[node], self.__sentences[node])
            nodes_in_the_network.append(nod)
        sorted_nodes = sorted(nodes_in_the_network, key=lambda node: node.eigenvector_centrality)

        # Print the phrases sorted by eigenvector centrality
        #I have a question how much of phrases we should output I said n/2
        for n in sorted_nodes[:p]:
            print(n.node_id)
       


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

    