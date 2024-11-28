from .Indexing import index
from .load_data import DATA, DATA_ID
from .Preprocess import preprocess_text
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
import numpy

Vectorizer, convert_id, tfidf_matrix = index()

def search(query, k = 5, euclid = False):
    query = query.strip()
    query = preprocess_text(query, True)
    print(query)
    query_vector = Vectorizer.transform(query)
    similarity = None
    if not euclid:
        similarity = cosine_similarity(query_vector, tfidf_matrix)[0]
        top = numpy.argsort(similarity)[::-1][:k]
    else:
        similarity = euclidean_distances(query_vector, tfidf_matrix)[0]
        top = numpy.argsort(similarity)[:k]

    result = []

    for i in top:
        newdata = {
            'Title': DATA[convert_id[i]]['title'],
            'Content': DATA[convert_id[i]]['content'],
        }
        result.append(newdata)

    return result
