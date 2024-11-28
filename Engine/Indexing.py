from collections import defaultdict
from .load_data import DATA, DATA_ID
from .Preprocess import preprocess_text
from sklearn.feature_extraction.text import TfidfVectorizer
import os
import json

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def index():
    convert_id = dict()
    cnt = 0
    documents = []
    for id in DATA_ID:
        convert_id[cnt] = id
        cnt += 1
        doc = DATA[id]
        text = f"{doc['title']}. {doc['content']}"
        text = preprocess_text(text)
        new_text = ""
        for item in text:
            new_text += item + ' '
        new_text.strip()
        documents.append(new_text)

    tf_vectorizer = TfidfVectorizer(use_idf=False)
    tf_matrix = tf_vectorizer.fit_transform(documents)

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    terms = vectorizer.get_feature_names_out()
    idf_values = vectorizer.idf_
        
    with open(os.path.join(ROOT_DIR, 'index.json'), 'w', encoding = 'utf-8') as f:
        all_docs = []
        for doc_id, (tf_row, tfidf_row) in enumerate(zip(tf_matrix.toarray(), tfidf_matrix.toarray())):
            all_terms = []
            for term_index, tf in enumerate(tf_row):
                if tf > 0:  # Only print terms that appear in the document
                    term = terms[term_index]
                    idf = idf_values[term_index]
                    tfidf = tfidf_row[term_index]
                    # print(f"  Term: {term}, TF: {tf:.4f}, IDF: {idf:.4f}, TF-IDF: {tfidf:.4f}")
                    piece = {
                        'term': term,
                        'index': {
                            'TF': f'{tf:.4f}',
                            'IDF': f'{idf:.4f}',
                            'TF-IDF': f'{tfidf:.4f}',
                        },
                    }
                    all_terms.append(piece)
            newdata = {
                'Document ID': convert_id[doc_id],
                'Title': DATA[convert_id[doc_id]]['title'],
                'Content': DATA[convert_id[doc_id]]['content'],
                'Date': DATA[convert_id[doc_id]]['date'],
                'terms': all_terms,
            }
            all_docs.append(newdata)
        
        json.dump(all_docs, f, indent=4, ensure_ascii=False)
    
    return vectorizer, convert_id, tfidf_matrix
                
