import os
from pyvi import ViTokenizer as VT
from typing import Dict, List, Set

FILE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_filter() -> Set[str]:
    """Load Vietnamese stopwords"""
    Files = ['vietnamese-stopwords-dash.txt', 'vietnamese-stopwords.txt']
    words = set()

    for item in Files:
        try:
            filepath = os.path.join(FILE_DIR, item)
            tmp = None
            with open(filepath, 'r', encoding='utf-8') as f:
                tmp = {line.strip() for line in f if line.strip()}
            words.union(tmp)
        except FileNotFoundError:
            print(f"Warning: Stopwords file not found at {item}")
    return words

stopwords = load_filter()

def preprocess_text(seq: str, query = False) -> List[str]:
    """Tokenize and filter words"""
    text = VT.tokenize(seq.lower())
    tokens = text.split()
    if not query:
        tokens = [token.strip() for token in tokens
                if token.strip() and token not in stopwords]
    return tokens