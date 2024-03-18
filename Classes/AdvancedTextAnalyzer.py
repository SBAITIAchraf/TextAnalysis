from langdetect import detect
import re
from collections import defaultdict




class AdvancedTextAnalyzer():
    def __init__(self,text):
        self.text=text

    def calculate_sentence_similarity(phrase1,phrase2):
        score=0
        #on va l 'implementer en se basant sur la methode qui prend tf et idf des mots de chaque phrase
        return score

    def Analyse_text(self):
        text = re.sub(r'\s+', ' ', text)
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)  #Extraction des phrases cette méthode de split en donnant le pattern je l'ai testé ça marche 
            # initialisation du graphe
        graph = defaultdict(list)
        for i, sentence_i in enumerate(sentences):
            for j, sentence_j in enumerate(sentences):
                if i != j:
                # Il faut qu'on implemente cette fonction nommée calculate..... pour calculer similarity entre deux phrases en se basant sur l'une des méthodes
                    similarity = self.calculate_sentence_similarity(sentence_i, sentence_j)
                    #pour implementer cette fonction il nous faut tf et idf des mots dans cette phrase donc il faut qu'on fait un pre processing a la phrase pour supprimer stop wordq les mots neutres....
                
    
                    if similarity > 0.2:  # comment va t-on determiner les phraes adjoints dans le graph ,par excemple on met un seuil pour le score si le score depasse ce seuil alors on va connecter les deux nodesc a d les deux phrases
                        graph[i].append(j)
    
        return graph, sentences

    