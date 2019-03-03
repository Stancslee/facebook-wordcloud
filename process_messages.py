#!/usr/bin/env python3
"""
Justin Ly
"""
import json
import pandas as pd

def main():
    """
    1. Read in the .json file containing messages
    2. Use pandas tables to save data
    3. Write the most frequently used words to top_words.txt
    """

    all_data = dict()
    file_path = 'data/message.json'

    with open(file_path, 'r') as f:
        all_data = json.loads(f.read())

    flip_tards = all_data['participants']
    flip_tards = [x['name'] for x in flip_tards]
    table = pd.DataFrame(all_data['messages'])
    print(table)

if __name__ == "__main__":
    main()

