import os
import json
from typing import Dict
from collections import defaultdict
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, 'dataset')

def load_data():
    """
    Read dataset and compress into a dictionary
    
    Returns: defaultdict(dict)
    """
    data = defaultdict(dict)
    data_id = []

    for filename in os.listdir(DATA_DIR):
        if filename.endswith('.json'):
            filepath = os.path.join(DATA_DIR, filename)
            with open(filepath, 'r', encoding = 'utf-8') as f:
                doc = json.load(f)

                first_newline_index = doc['post_details']['title'].find('\n')

                # If a newline exists, slice the string before the newline
                if first_newline_index != -1:
                    cleaned_title = doc['post_details']['title'][:first_newline_index]
                else:
                    cleaned_title = doc['post_details']['title']
                piece = {
                    'title': cleaned_title,
                    'content': doc['post_details']['content'].strip(),
                    'date': doc['post_details']['date'].split('GMT')[0].strip()
                }

                data[doc['post_details']['postId']] = piece
                data_id.append(doc['post_details']['postId'])
    
    return data, data_id

DATA, DATA_ID = load_data()