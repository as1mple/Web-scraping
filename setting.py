import json

import os

import argparse


def setl():
    parser = argparse.ArgumentParser(description='Test')
    parser.add_argument( '--checkin', type=str, default='2020-09-13')
    parser.add_argument('--los', type=str, default='1')
    parser.add_argument('--id', type=str, default='550')
    parser.add_argument('--file', type=str, default='arg.csv')
    parser.add_argument('--flag', type=bool, default=True)

    args = parser.parse_args()



    return [args.checkin, args.los, args.id, args.file, args.flag]

def save_data(room: dict, JSON_PATH  = 'res.json') -> None:
    if not os.path.isfile(JSON_PATH):
        with open(JSON_PATH, 'w') as json_file:
            json.dump([room], json_file, indent=4)
    else:
        with open(JSON_PATH) as feeds_json:
            feeds = json.load(feeds_json)
            feeds.append(room)

            with open(JSON_PATH, 'w') as json_file:
                json.dump(feeds, json_file, indent=4)

