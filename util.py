# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 17:21:32 2025

@author: Masou
"""
import os
import json
import re
from datetime import datetime, timezone

def save_json(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f)

def read_json(adr):
    with open(adr) as f:
        data = json.load(f)
    return data

def list_json_files(directory):
    return [f for f in os.listdir(directory) if f.endswith('.json') and os.path.isfile(os.path.join(directory, f))]

def read_json_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [json.loads(line) for line in f.readlines() if line.strip()] 

def checking_time (t):

    # Parsing the date string to a datetime object
    parsed_date = datetime.strptime(t, '%a %b %d %H:%M:%S %z %Y')
    
    # Defining the range as aware datetime (using UTC timezone)
    start_date = datetime(2020, 1, 1, tzinfo=timezone.utc)
    end_date = datetime(2022, 7, 31, tzinfo=timezone.utc)
    
    # Checking if the date falls within the range
    is_within_range = start_date <= parsed_date <= end_date
    
    return is_within_range

def clean_text(text):
    text = text.lower()
    text = re.sub(r'@[^\s]+', '', text)
    text = re.sub(r"http\S+", " ", text)
    text = re.sub(r'#[^\s]+', '', text)
    text = re.sub(r"\s+", " ", text)
    text = text.strip()
    return text

def categorize_nsi(value):
    if value < 0.45:
        return 'weak'
    elif 0.45 <= value < 0.55:
        return 'moderate'
    else:
        return 'strong'