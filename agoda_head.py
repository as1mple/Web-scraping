import csv

from pprint import pprint

import asyncio
from aiohttp import ClientSession

from setting import save_data, setl

CHECKIN, LOS, ID, WAY, Flag = setl()
url = "https://www.agoda.com/api/en-us/pageparams/property?"
async def fetch(CHECKIN, LOS, ID, session):
    async with session.get(url, params={
             "checkin": CHECKIN,
             "los": LOS,             "hotel_id": ID,
             'adults': 2},
                                timeout=10) as response:
        response =await response.json()

        return response

async def run():

    tasks = []



    # Fetch all responses within one Client session,
    # keep connection alive for all requests.
    async with ClientSession() as session:
        for i in condition():
            task = asyncio.ensure_future(add_dict(*i, session))
            tasks.append(task)

        responses = asyncio.gather(*tasks)
        await responses
        # you now have all response bodies in this variable
        pprint(responses)

def print_responses(result):
    print(result)


def read_csv():
    with open(WAY, 'r') as myFile:
        dataFromFile = csv.reader(myFile)
        data = (list(dataFromFile))
    return data
def condition() -> None:
    global CHECKIN, LOS, ID
    if (WAY == 'not'):
        return [[CHECKIN, LOS, ID]]
    else:
        return read_csv()


async def add_dict(CHECKIN, LOS, ID, session):

    res = {}
    hotel = await fetch(CHECKIN, LOS, ID, session)
    HOTEL_NAME =  hotel['hotelInfo']['name']
    try:
     room =  hotel['roomGridData']['masterRooms'][0]
    except KeyError as io:
        print(io)
        return 0
    except IndexError as io:
        print(io)
        return 0

    res.update(
        {'id': room['id'], 'name': room['name'], 'price': room['rooms'][0]['price'],
         'CHECKIN': CHECKIN, 'LOS': LOS, 'ID': ID, 'HOTEL': HOTEL_NAME})
    save_data(res) if Flag else 0
    print(res)
    return res



