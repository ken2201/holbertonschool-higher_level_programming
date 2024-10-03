#!/usr/bin/python3
"""Module task_02_csv : Define Converting CSV date to JSON format"""


import csv
import json


def convert_csv_to_json(csv_filename):
    """Reading data from one format and converting it into another format"""
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:

            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: The file '{csv_filename}' was not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
