#!/bin/python3

import datetime 
import random

class Broker():
    market_ls = []
    spread = 0.0018
    def __init__(self):
        self.dt = datetime.datetime.now().replace(microsecond=0)
        self.date_qty = 5
        
        for i in range(self.date_qty):
            self.dt = self.dt+datetime.timedelta(seconds=10,microseconds=0)
            Broker.market_ls.append(Market(self.dt))

        self.clock()
    def clock(self):
        for i in range(self.date_qty):
            print("")
            Broker.market_ls[i].show_info()    
            while True:
                ans=input("Input command!\nNot order:0\tBID:1\tASK:2\n")
                if ans =="1" or ans=="2":
                    print("OK")
                    break
                else:
                    print("Again! Please input 0,1 or 2")
class Market():
    currency = "USD/JPY"
    id = 0
    rate = 150
    def __init__(self,dt):
        self.id=Market.id
        Market.id += 1
        self.dt = dt
        self.fixed_upward_rate()
        #self.set_fixed_rate()
        #self.set_floating_rate()
    def fixed_upward_rate(self):
        self.pip=5
        self.rate = Market.rate
        Market.rate = round(self.rate+self.pip/100,2)
    def set_fixed_rate(self):
        self.rate = Market.rate
    def set_floating_rate(self):
        self.rate = round(Market.rate + random.randint(-100,100)/100,2)
        Market.rate = self.rate
    def show_info(self):
        print("ID:",self.id,"\t",self.dt,"\nBID:",self.rate-Broker.spread/2,"\tASK:",self.rate+Broker.spread/2)

class Trade():
    pass
    # id
    # time
    # ask or bid
    # qty

class Player():
    id=0
    def __init__(self,input_money):
        self.id = Player.id
        Player.id +=1
        self.balance = input_money
    # order

def main():
    start=Broker()

main()
