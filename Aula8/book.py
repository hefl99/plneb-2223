import spacy
from collections import Counter


with open("/Users/florianhetzel/Desktop/PLNEB/Aula8/harry_potter_pedra_filosofal.txt") as file:
    book = file.read()

nlp = spacy.load('pt_core_news_md')

av = nlp(book)

names = []
locations = []
organisations = []
for s in av.sents:
    for ent in s.ents:
        if ent[0].ent_type_ == "PER":
            names.append(ent.text)
        if ent[0].ent_type_ == "LOC":
            locations.append(ent.text)
        if ent[0].ent_type_ == "ORG":
            organisations.append(ent.text)

most_common_names = Counter(names).most_common(10)
most_common_locations = Counter(locations).most_common(10)
most_common_organisations = Counter(organisations).most_common(10)

print(most_common_names)
print(most_common_locations)
print(most_common_organisations)