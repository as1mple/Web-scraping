import json
import logging
import os
import sys
from logging.handlers import TimedRotatingFileHandler

import argparse

FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
LOG_FILE = "n.log"
def setl():
    parser = argparse.ArgumentParser(description='Test')
    parser.add_argument('-ch', '--CHECKIN', type=str, help='input', default='2020-09-13')
    parser.add_argument('-l', '--LOS', type=str, help='count', default='1')
    parser.add_argument('-id', '--ID', type=str, help='id', default='550')
    parser.add_argument('-csEVEv', '--File', type=str, help='with file', default='arg.csv')
    parser.add_argument('-flag', '--Flag', type=bool, default=True)

    args = parser.parse_args()

    checkin = args.CHECKIN
    los = args.LOS
    id = args.ID
    way = args.File
    flag = args.Flag

    return [checkin, los, id, way, flag]

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

