import spacy
from collections import Counter
from itertools import combinations

file = open('harry_potter_pedra_filosofal.txt', 'r')
book = file.read()

nlp = spacy.load('pt_core_news_md')
av = nlp(book)

name_combos = []
for s in av.sents:
    persons_set = set()
    for ents in s.ents:
        for ent in ents:
            if ent.ent_type_ == "PER" or ent.text == "Harry":
                persons_set.add(ent.text)
    name_combos.extend(combinations(persons_set, 2))

sorted_name_combos = []
for (first, sec) in name_combos:
    if first < sec:
        sorted_name_combos.append(tuple([first, sec]))
    elif first > sec:
        sorted_name_combos.append(tuple([sec, first]))

combo_count = Counter(sorted_name_combos)

best_friends = combo_count.most_common(10)

print('Best friends:')
for i, (combo, count) in enumerate(best_friends):
    print(f'Rank {i+1}: ', combo, f' ({count} counts)')

