import string
import Classes.AdvancedTextAnalyzer as advanced

text = "Tomato is important for ecosystem. Ecosystem no good without tomato. Hello everybody and welcom."

hj = advanced.AdvancedTextAnalyzer(text)

print(hj.calculate_sentence_similarity(hj.sentences[0], hj.sentences[1]))