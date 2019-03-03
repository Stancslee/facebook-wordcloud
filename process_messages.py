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
    keep_columns = ['content', 'sender_name']

    with open(file_path, 'r') as f:
        all_data = json.loads(f.read())

    flip_tards = all_data['participants']
    flip_tards = [x['name'] for x in flip_tards]
    df = pd.DataFrame(all_data['messages'])

    all_cols = list(df.columns.values)
    drop_cols = [x for x in all_cols if x not in keep_columns]
    df = df.drop(drop_cols, axis=1)
    print(df)

if __name__ == "__main__":
    main()

