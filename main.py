
import csv
import re

def read_file(filename:str):
    with open(filename,'r') as file_it:
        data = csv.reader(file_it, delimiter=';')
    return data

def check():
    valid={
        'mail': re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'),
        "http_status_message": re.compile(r'(([1-9])|([1-9][0-9])|([1-9][0-9][0-9]))\s[A-Z]([a-z]+)'),
        'snils':re.compile(r'[0-9]{11}'),
        'passport': re.compile(r'([0-9]{2}\s){2}[0-9]{6}'),
        'ip_v4':re.compile(r'((25[0-6]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[1-9])\.){3}(25[0-6]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[1-9])'),



    }
