from decimal import Decimal as Dcml, ROUND_CEILING, ROUND_FLOOR
from binance.client import Client
from binance.enums import *
from datetime import datetime
import configparser
import os


listFile = os.listdir()

# Will create a config file with your API key
if 'config.cfg' in listFile:
    config = configparser.ConfigParser()
    config.read('config.cfg')
    api = config['BINANCE']
    client = Client(api['KEY'], api['SECRET'])
else:
    key = input('Enter Binance Futures api key:\n')
    secret = input('\nEnter Binance Futures api secret key:\n')
    client = Client(key, secret)
    if input(f'\nThe config.cfg file will be saved to {os.getcwd()}\nSave keys?  YES/NO:\n').upper() == 'YES':
        with open('config.cfg', 'a') as file:
            print('[BINANCE]', file=file)
            print(f'KEY = {key}', file=file)
            print(f'SECRET = {secret}', file=file)
        print(f'\nThe config.cfg file is saved in { os.getcwd()} directory.')
    else:
        print('\nKeys not saved')


class newTrade():
    """Create new trade
    # Create an object; Binance Futures Symbol: CHZUSDT; leverage: 5;
    exemple: chz = newTrade('chz', 5)
    
    Methods:
    chz.timeNow()  # Print datetime.now
    chz.cancelOrders()  # CANCEL_ALL_OPEN_ORDERS
    chz.checkOpenOrders()  # GET_ALL_OPEN_ORDERS
    chz.cancelOneOrder(int)  # CANCEL_ONE_ORDER
    chz.leverage(int)  # CHANGE_LEVERAGE
    chz.checkBalnc()  # CHECK_BALANCE
    chz.checkPos()  # CHECK_POSITION_INFORMATION
    chz.buy_market(int or float)  # ORDER_BUY_MARKET
    chz.sell_market(int or float)  # ORDER_SELL_MARKET
    chz.sl(int or float)  # ORDER_SL
    """
    def __init__(self, symbol, leverage=20):
        self.symbol_hold = 'USDT'
        self.symbol_trade = symbol.upper()
        self.trade_pair = self.symbol_trade + self.symbol_hold
        inf = client.futures_change_leverage(symbol = self.trade_pair, leverage = leverage)
        message = f"\
        Symbol   : {inf['symbol']}\n\
        Leverage : {inf['leverage']}"
        self.timeNow()
        print(message)        

    def timeNow(self):
        """Print datetime.now
        exemple: timeNow()
        """
        message = f"----{datetime.now().strftime('%d.%m.%Y %H:%M')}"
        print(message)

    def cancelOrders(self):
        """CANCEL_ALL_OPEN_ORDERS
        exemple: cancelOrders()
        """
        inf = client.futures_cancel_all_open_orders(symbol = self.trade_pair)
        message = f"code:{inf['code']} {inf['msg']}"
        self.timeNow()
        print(message)
        self.checkOpenOrders()
        

    def checkOpenOrders(self):
        """GET_ALL_OPEN_ORDERS
        exemple: checkOpenOrders()
        """
        inf = client.futures_get_open_orders()
        for i in inf:
            message = f"\
            Symbol :   {i['symbol']}\n\
            OrderId:   {i['orderId']}\n\
            origQty:   {i['origQty']}\n\
            Side   :   {i['side']}\n\
            Price  :   {i['price']}\n\
            slPrice:   {i['stopPrice']}\n\
            Status :   {i['status']}\n\
            Type   :   {i['type']}"
            self.timeNow()
            print(message)
        print(f'All {len(inf)} open orders')

    def cancelOneOrder(self, orderId):
        """CANCEL_ONE_ORDER
        exemple: cancelOneOrder(int)
        """
        inf = client.futures_cancel_order(symbol = self.trade_pair, orderId = orderId)
        message = f"\
        Symbol :   {inf['symbol']}\n\
        OrderId:   {inf['orderId']}\n\
        origQty:   {inf['origQty']}\n\
        Side   :   {inf['side']}\n\
        Price  :   {inf['price']}\n\
        slPrice:   {inf['stopPrice']}\n\
        Status :   {inf['status']}\n\
        Type   :   {inf['type']}"
        self.timeNow()
        print(message)

    def leverage(self, num):
        """CHANGE_LEVERAGE
        exemple: leverage(int)
        """
        inf = client.futures_change_leverage(symbol = self.trade_pair, leverage = num)
        message = f"\
        Symbol   : {inf['symbol']}\n\
        Leverage : {inf['leverage']}"
        self.timeNow()
        print(message)

    def checkBalnc(self):
        """CHECK_BALANCE
        exemple: checkBalnc()
        """
        balance = client.futures_account_balance()
        balance_hold_symbol = Dcml('0')
        for i in range(len(balance)):
            if balance[i]['asset'] != self.symbol_hold:
                continue
            balance_hold_symbol = balance[i]['balance']
        balance_hold_symbol = Dcml(balance_hold_symbol)
        message = f'Balance: {balance_hold_symbol} USDT'
        self.timeNow()
        print(message)

    def checkPos(self):
        """CHECK_POSITION_INFORMATION
        exemple: checkPos()
        """
        chkPV = client.futures_position_information(symbol = self.trade_pair)[0]
        message = f"\
        Symb: {chkPV['symbol']}\n\n\
        entryPrice:  {chkPV['entryPrice']}\n\
        Liquidation: {chkPV['liquidationPrice']}\n\
        Amt:  {chkPV['positionAmt']} Coins\n\
        Amt:  {int(float(chkPV['notional']))} Dollars\n\n\
        PNL:  {chkPV['unRealizedProfit']}"
        self.timeNow()
        print(message)

    def buy_market(self, buyMarket):
        """ORDER_BUY_MARKET
        exemple: buyMarket(int or float)
        """
        ordBuyMkt = client.futures_create_order(symbol = self.trade_pair, side = 'BUY', type = 'MARKET', quantity = buyMarket)
        message = f"\
        Symbol :   {ordBuyMkt['symbol']}\n\
        OrderId:   {ordBuyMkt['orderId']}\n\
        origQty:   {ordBuyMkt['origQty']}\n\
        Side   :   {ordBuyMkt['side']}\n\
        Status :   {ordBuyMkt['status']}"
        self.timeNow()
        print(message)

    def sell_market(self, sellMarket):
        """ORDER_SELL_MARKET
        exemple: sell_market(int or float)
        """
        ordSellMkt = client.futures_create_order(symbol = self.trade_pair, side = 'SELL', type = 'MARKET', quantity = sellMarket)
        message = f"\
        Symbol :   {ordSellMkt['symbol']}\n\
        OrderId:   {ordSellMkt['orderId']}\n\
        origQty:   {ordSellMkt['origQty']}\n\
        Side   :   {ordSellMkt['side']}\n\
        Status :   {ordSellMkt['status']}"
        self.timeNow()
        print(message)

    def sl(self, price):
        """ORDER_SL
        exemple: sl(int or float)
        """
        chkPV = client.futures_position_information(symbol = self.trade_pair)[0]['positionAmt']
        if chkPV and chkPV[0] != '-':
            ordSl = client.futures_create_order(symbol=self.trade_pair, side = 'SELL', type = 'STOP_MARKET', stopPrice = price, closePosition = 'true', timeInForce='GTC')
        elif chkPV and chkPV[0] == '-':
            ordSl = client.futures_create_order(symbol=self.trade_pair, side = 'BUY', type = 'STOP_MARKET', stopPrice = price, closePosition = 'true', timeInForce='GTC')
        else:
            print(f'Not set!!! PositionAmt: {chkPV}')
        message = f"\
        Symbol    : {ordSl['symbol']}\n\
        OrderId   : {ordSl['orderId']}\n\
        Side      : {ordSl['side']}\n\
        Status    : {ordSl['status']}\n\
        stopPrice : {ordSl['stopPrice']}"
        self.timeNow()
        print(message)


