import json
import pandas as pd

df = pd.DataFrame(columns=['id', 'text', 'label'])

with open('ai_gen_essays.json', 'r') as f:
    data = json.load(f)
    full_texts = [record['full_text'][record['full_text'].index('\n')+1:] if '\n' in record['full_text'] else record['full_text'] for record in data]
    print(full_texts[0])