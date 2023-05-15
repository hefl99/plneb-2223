import spacy
import re

nlp = spacy.load('pt_core_news_md')

document = """"A minha família é constituída por mim, pelo meu pai, a minha mãe, a minha irmã, os meus avós maternos e o meu avô paterno.
O meu pai chama-se Miguel. Tem 58 anos, é alto e moreno, com olhos castanhos. Conheceu a minha mãe, Maria, na faculdade, quando estavam a estudar psicologia. A minha mãe tem 55 anos e é ruiva, com olhos azuis.
A minha irmã chama-se Joana e tem 25 anos. Tem o cabelo ruivo, como a minha mãe, e os olhos castanhos como o meu pai. Estudou jornalismo, mas agora trabalha numa empresa de publicidade.
Os meus avós maternos, Manuel e Irene, têm ambos 80 anos. Conheceram-se numa festa na sua aldeia há 60 anos e estão juntos desde então.
O meu avô paterno, Francisco, é agricultor. Ronaldo nao joga no VfB Stuttgart."""

av = nlp(document)

dic = {}

for s in av.sents:
    print(f'# {s}')
    for ent in s.ents:
        print(f'@ {ent}')
    for w in s:
        print(f'word {(w.text)} | lemma {w.lemma_} | POS {w.pos_} | tag: {w.tag_} | ent_type: {w.ent_type_} | dep: {w.dep_}')
        if w.pos_ == 'VERB':
            print(w)
            print(w.pos_)
            if w not in dic:
                dic[w] = 1
            elif w in dic:
                dic[w] += 1
print(dic)
