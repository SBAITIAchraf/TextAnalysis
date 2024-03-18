import re
text = """Although there are most encouraging results presented in the graph-based
approaches, they do not take into consideration the aspects like feature association
score, coreference resolution and semantic association score.
The Web data is represented using graph, and meaningful patterns are extracted
from it. The importance of graph properties, advanced graph types and suitable
representation are essential to provide analysis of Web information, which is used
for applications like recommendation system, sentiment analysis and many more.
Graph is a natural way of representing association between the entities."""

new_txt = re.sub(r'\s+', ' ', text)
sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', new_txt)
print(sentences)