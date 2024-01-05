import os
import sys
import json
import time
import pprint

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from Finvasia.connect import NorenApi

prices = {}
positions = []
subscribed_instruments = []

def event_handler_quote_update(message):
    # e   Exchange
    # tk  Token
    # lp  LTP
    # pc  Percentage change
    # v   volume
    # o   Open price
    # h   High price
    # l   Low price
    # c   Close price
    # ap  Average trade price
    global prices

    if 'lp' in message:
        prices[message['tk']] = float(message['lp'])

def event_order_update(message):

    global positions
    global finvasia_obj

    if 'status' in message and message['status'] == 'COMPLETE':
        print("refreshing positions")
        positions = finvasia_obj.get_positions()

def subscribe_util():
    global positions
    global subscribed_instruments
    global finvasia_obj

    for pos in positions:
        token = pos['token']
        exchange = pos['exch']
        if token not in subscribed_instruments:
            subscribed_instruments.append(token)
            finvasia_obj.subscribe(f'{exchange}|{token}')



# Position sample:
# {'actid': '#',
#  'bep': '199.55',
#  'cfbuyqty': '0',
#  'cfsellqty': '0',
#  'dayavgprc': '199.55',
#  'daybuyamt': '0.00',
#  'daybuyavgprc': '0.00',
#  'daybuyqty': '0',
#  'daysellamt': '2993.25',
#  'daysellavgprc': '199.55',
#  'daysellqty': '15',
#  'dname': 'BANKNIFTY 10JAN24 47500 PE ',
#  'exch': 'NFO',
#  'frzqty': '901',
#  'instname': 'OPTIDX',
#  'lp': '159.45',
#  'ls': '15',
#  'mult': '1',
#  'netavgprc': '199.55',
#  'netqty': '-15',
#  'netupldprc': '199.55',
#  'openbuyamt': '3945.00',
#  'openbuyavgprc': '263.00',
#  'openbuyqty': '15',
#  'opensellamt': '0.00',
#  'opensellavgprc': '0.00',
#  'opensellqty': '0',
#  'pp': '2',
#  'prcftr': '1.000000',
#  'prd': 'I',
#  'rpnl': '0.00',
#  's_prdt_ali': 'MIS',
#  'stat': 'Ok',
#  'ti': '0.05',
#  'token': '50393',
#  'totbuyamt': '0.00',
#  'totsellamt': '2993.25',
#  'totsellavgprc': '199.55',
#  'tsym': 'BANKNIFTY10JAN24P47500',
#  'uid': '#',
#  'upldprc': '0.00',
#  'urmtom': '601.50'}

def calculate_pnl(positions):
    global prices

    total_pnl = 0
    for pos in positions:
        r_pnl, u_pnl = float(pos.get('rpnl')), 0
        try:
            ltp = float(prices[pos['token']])
            netqty = int(pos.get('netqty'))
            u_pnl = netqty * (ltp - float(pos.get('netavgprc'))) * float(pos.get('prcftr'))
            total_pnl += (u_pnl + r_pnl)
            
        except Exception as E:
            print(E)
    print("total pnl: ", total_pnl)

creds = json.load(open("creds.json", "r"))['finvasia']

user_id = creds['user']
password = creds['password']
totp_secret = creds['totp_secret']
api_key = creds['api_key']

finvasia_obj = NorenApi(host='https://api.shoonya.com/NorenWClientTP/',
                        websocket='wss://api.shoonya.com/NorenWSTP/', userid=user_id, password=password, twoFA=totp_secret, apikey=api_key)

finvasia_obj.set_session()
finvasia_obj.start_websocket(subscribe_callback=event_handler_quote_update, order_update_callback=event_order_update)

# =====================================================

positions = finvasia_obj.get_positions()
subscribe_util()

time.sleep(2)  # let the subscription complete

while True:
    calculate_pnl(positions)
    subscribe_util()
    time.sleep(2)

