# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 21:42:40 2018

@author: Alan Jerry Pan, CPA, CSc student
@affiliation: Shanghai Jiaotong University
    
MAN VS MACHINE: AUTOTRADER VERSION
Genres: RPG, trading, comedy, horror, educational

Desription: MAN VS MACHINE: AUTOTRADER VERSION is usually not the role playing 
game any one would want to play. This game simulates real-life situations that 
happen every day on trading floors. You are a trader starting with $10. The
autotrader starts with $100 and never misses a good deal. The rules are simple:
BUY and SELL and you bankrupt the autotrader or the autotrader takes your innings. 
Like the real world, the more $wealth you amassed, the easier it is to bankrupt 
others. The only way to bankrupt the AUTOTRADER in this game is by taking over 
the market through amassing $wealth in the market.


Works Cited:
Pan, Alan J. (2018). Profit-Sentient Electronic Bartering Platform [Computer software]. Github repository <https://github.com/alanjpan/Profit-Sentient-Electronic-Bartering-Platform>
Pan, Alan J. (2018). Barter Market [Computer software]. Github repository <https://github.com/alanjpan/Linear-Dungeon>

    
https://www.greekshares.com/investing-education/trading-slang#inline-auto150
https://www.inc.com/peter-economy/11-winning-negotiation-tactics-from-trump-s-art-of-the-deal.html


@author: alanp
"""

import sys
import time
import random
secure_random = random.SystemRandom()
slang = ["If that trader gets slammed again, his buying power will dwindle down to nothing!",
         "Hey, watch that stock, it's crunching through the price level!", 
         "When you dare to hold the position overnight.",
         "I can't believe it! I got jigged out on a trade today!",
         "That trader hasn't figured out the learning curve yet.", 
         "I melted my account today trading A!",
         "My trades today didn't even cover my nut!",
         "Wow, that stock's running, it's printing on the \"O!\"",
         "I wish I could be a great scalper, like him!",
         "I hate the slippage in SOES orders.",
         "That trader uses a lot of squiggly lines on his chart.",
         "I bought A and it ran up three sticks!",
         "Get out of your trade, the market's tanking!",
         "I got whacked on that trade!"]
rant = ["I like thinking big. I always have. To me it's very simple: if you're going to be thinking anyway, you might as well think big.",
         "I always go into the deal anticipating the worst. If you plan for the worst--if you can live with the worst--the good will always take care of itself.",
         "I never get too attached to one deal or one approach...I keep a lot of balls in the air, because most deals fall out, no matter how promising they seem at first.",
         "I like to think that I have that instinct. That's why I don't hire a lot of number-crunchers, and I don't trust fancy marketing surveys. I do my own surveys and draw my own conclusions.",
         "The worst thing you can possibly do in a deal is seem desperate to make it. That makes the other guy smell blood, and then you're dead.",
         "Perhaps the most misunderstood concept in all of real estate is that the key to success is location, location, location...First of all, you don't necessarily need the best location. What you need is the best deal.",
         "One thing I've learned about the press is that they're always hungry for a good story, and the more sensational the better...The point is that if you are a little different, a little outrageous, or if you do things that are bold or controversial, the press is going to write about you.",
         "In most cases I'm very easy to get along with. I'm very good to people who are good to me. But when people treat me badly or unfairly or try to take advantage of me, my general attitude, all my life, has been to fight back very hard.",
         "You can't con people, at least not for long. You can create excitement, you can do wonderful promotion and get all kinds of press, and you can throw in a little hyperbole. But if you don't deliver the goods, people will eventually catch on.",
         "I believe in spending what you have to. But I also believe in not spending more than you should.",
         "Money was never a big motivation for me, except as a way to keep score. The real excitement is playing the game."]

from threading import Thread

products = ["A"]

demand = []
supply = []


def buy(item, price):
    demand.append((item, price))
def sell(item, price):
    supply.append((item, price))

def transact():
    global nomnomnom
    global supply
    global demand

    for i in supply:
        for j in demand:
            if i[0] == j[0]:
                if i[1] < j[1]:
                    collect = j[1] - i[1]
                    nomnomnom += collect
                    demand.remove(j)
                    print("nom$$$ " + str(nomnomnom))
                    break

        
def dramatype(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.10)
       
print()
dramatype("MAN VS MACHINE")
print()
dramatype("AUTOTRADER VERSION")
print("\n")
dramatype("Narrator: Enter the stock market.")
print()
dramatype("You, a man, or woman, challenge the TRADINGMONSTER")
print()
dramatype("...TRADINGMONSTER does not feel. It does not fear.")
print()
dramatype("BUY low! SELL high, brave puny trader!")
print()
time.sleep(1)
dramatype("...")
dramatype("BEGIN!")

monsteralive = True
nomnomnom = 100

def market():
    global supply
    global demand
    global monsteralive
    
    while monsteralive == True:
        time.sleep(4)
        demand.append(("A", random.randint(mind, maxd)))
        print("RESELL PRICE: " + str(demand[0]))
        dramatype(secure_random.choice(slang))

maxd = 10
mind = 5
maxs = 7
mins = 3

def heavy():
    global nomnomnom
    global maxd
    global mind
    global maxs
    global mins
    
    for i in supply:
        maxd += 1
        maxs += 1
    nomnomnom -= int(kaching/10)

def TRADINGMONSTER():
    global monsteralive
    global nomnomnom
    global supply
    
    while nomnomnom > 0:
        supply.append(("A", random.randint(mins, maxs)))
        print("PURCHASE PRICE: " + str(supply[0]))
        time.sleep(10)
        transact()
        heavy()
        if nomnomnom > 1000:
            dramatype(secure_random.choice(rant))
            
        
    monsteralive == False
    print()
    dramatype("THE TRADINGMONSTER IS SLAIN!!")
    print()
    dramatype("... or is it?")
    quit()

Thread(target = market).start()
Thread(target = TRADINGMONSTER).start()

inventory = []
kaching = 10
while kaching >= 0:
    try:
        response = input("BUY!")
        if response.lower() == "give up":
            dramatype("TRADINGMONSTER won't let you quit...")
            quit()
        if len(response) > 0:
            inventory.append(supply[0])
            supply.pop(0)
            print(str(inventory))
        response = input("SELL!")
        if len(response) > 0:
            kaching += demand[len(demand)-1][1] - inventory[0][1]
            print(str(inventory))
            inventory.pop(0)
            print("YOU HAVE $" + str(kaching))
    except Exception:
        print()
        dramatype("A pigeon lands...")
print()
dramatype("Another victim of the TRADINGMONSTER")
