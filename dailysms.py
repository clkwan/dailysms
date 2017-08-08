import time
from datetime import datetime, timedelta

from googlemaps import Client as gmapClient
from googlemaps.distance_matrix import distance_matrix
from twilio.rest import Client as twilClient

from credentials import account_sid, auth_token, my_cell, twilio_number, gm_key

home_address = '41601 S Bellridge Dr, Belleville, MI'
work_address = 'ITBIC'
arrival_time = '9:30AM'

client = twilClient(account_sid, auth_token)


def convert_time(arrival_time):
    arrival_time = [int(x) for x in arrival_time.split(':')]
    hr = int(arrival_time[0])
    min = int(arrival_time[1])
    now = datetime.now()
    total_seconds = int((timedelta(hours=24)
                         - (now - now.replace(hour=hr, minute=min, second=0, microsecond=0))).total_seconds()
                        % (24 * 3600))
    return total_seconds


def get_traffic():
    gmaps = gmapClient(gm_key)
    distance = distance_matrix(gmaps,
                               home_address,
                               work_address,
                               arrival_time=time.strptime(arrival_time, '%I:%M%p')
                               )

    return distance['rows'][0]['elements'][0]['duration']['text']


def sendsms():
    my_msg = 'Your commute today is {}'.format(get_traffic())
    client.messages.create(
        to=my_cell,
        from_=twilio_number,
        body=my_msg
    )


if __name__ == '__main__':
    while True:
        if datetime.now() == time.strptime(arrival_time, '%I:%M%p'):
            sendsms()
