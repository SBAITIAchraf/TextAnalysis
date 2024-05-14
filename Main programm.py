import string
from Classes.AdvancedTextAnalyzer import AdvancedTextAnalyzer as advanced
from nltk.corpus import stopwords
from langdetect import detect


text = """L’´electromagn´etisme est un domaine captivant de la physique, englobant l’ensemble des ph´enom`enes ´electriques et magn´etiques. Ce champ d’´etude ´etend et g´en´eralise les lois de l’´electro-statique et de la magn´etostatique, qui d´ecrivent les champs ´electrique (E) et magn´etique (B) dans des contextes o`u ces champs sont statiques, c’est-`a-dire ind´ependants du temps. Lorsque ces champs varient dans le temps, de nouveaux ph´enom`enes physiques ´emergent, notamment l’induction ´electromagn´etique, o`u un champ magn´etique changeant cr´ee un champ ´electrique, et vice-versa.
Au cœur de l’´electromagn´etisme se trouvent les ´equations de Maxwell, un ensemble de quatre ´equations qui d´efinissent avec pr´ecision les champs ´electrique et magn´etique. Bien que ces ´equations impliquent des op´erateurs vectoriels, qui peuvent paraˆıtre intimidants de prime abord, ils sont essentiels et ne doivent ˆetre vus que comme des outils math´ematiques parmi d’autres. Le premier chapitre de ce cours est d´edi´e `a la description de ces op´erateurs vectoriels et `a un rappel de certaines de leurs propri´et´es fondamentales."""

hj = advanced(text)
print(hj.lang)
