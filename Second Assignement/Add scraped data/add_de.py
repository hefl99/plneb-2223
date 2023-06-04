from deep_translator import GoogleTranslator
import json

translator_pt_to_de = GoogleTranslator(source='pt', target='de')

with(open("Second Assignement/Website/terms_v10_original.json") as file):
    dict = json.load(file) 

for term in dict:
    print(term)
    if "de" not in dict[term]:
        dict[term]["de"] = translator_pt_to_de.translate(term)
        with(open("Second Assignement/Website/terms_v10_original_with_de.json", "w") as file):
            json.dump(dict,file,indent=6, ensure_ascii=False) 