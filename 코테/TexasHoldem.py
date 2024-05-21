from tkinter import *
from tkinter import font
from winsound import *
from card import *
from player import *
import random


class BlackJack:
    def __init__(self):
        self.window = Tk()
        self.window.title = ("BlackJack")
        self.window.geometry("800x600")
        self.window.configure(bg='green')
        self.fontstyle = font.Font(self.window, size=24, weight='bold', family='Consolas')
        self.fontstyle2 = font.Font(self.window, size=16, weight='bold', family='Consolas')
        self.setUpBotton()
        self.setUpLabel()

        self.player = Player('player')
        self.dealer = Player('dealer')
        self.betMoney = 10
        self.playerMoney = 1000
        self.nCardDealer = 0
        self.nCardPlayer = 0
        self.LCardPlayer = []
        self.LCardDealer = []
        self.deckN = 0
        self.window.mainloop()

    def setUpBotton(self):
        self.Check = Button(self.window, text='Check', width=6, height=1, font=self.fontstyle2, command=self.pressedCheck)
        self.Check.place(x=50, y=500)
        self.BetX1 = Button(self.window, text='Bet X1', width=6, height=1, font=self.fontstyle2, command=self.pressedBetX1)
        self.BetX1.place(x=150, y=500)
        self.BetX2 = Button(self.window, text='Bet X2', width=6, height=1, font=self.fontstyle2, command=self.pressedBetX2)
        self.BetX2.place(x=250, y=500)
        self.Deal = Button(self.window, text='Deal', width=6, height=1, font=self.fontstyle2, command=self.pressedDeal)
        self.Deal.place(x=600, y=500)
        self.Again = Button(self.window, text='Again', width=6, height=1, font=self.fontstyle2,command=self.pressedAgain)
        self.Again.place(x=700, y=500)

        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

    def setUpLabel(self):
        self.LbetMoney = Label(text='$10', width=4, height=1, font=self.fontstyle, bg='green', fg='cyan')
        self.LbetMoney.place(x=200, y=450)
        self.LplayerMoney = Label(text='You have $1000', width=15, height=1, font=self.fontstyle, bg='green', fg='cyan')
        self.LplayerMoney.place(x=500, y=450)
        self.Lstatus = Label(text='', width=15, height=1, font=self.fontstyle, bg='green', fg='white')
        self.Lstatus.place(x=500, y=300)

    def pressedBetX1(self):
        self.betMoney += 50
        if 50 <= self.playerMoney:
            self.LbetMoney.configure(text='$' + str(self.betMoney))
            self.playerMoney -= self.betMoney
            self.LplayerMoney.configure(text='You have $' + str(self.playerMoney))
            self.Deal['state'] = 'active'
            self.Deal['bg'] = 'white'
            PlaySound('sound/chip.wav', SND_FILENAME)
        else:
            self.betMoney -= 50

    def pressedBetX2(self):
        self.betMoney += 10
        if 10 <= self.playerMoney:
            self.LbetMoney.configure(text='$' + str(self.betMoney))
            self.playerMoney -= self.betMoney
            self.LplayerMoney.configure(text='You have $' + str(self.playerMoney))
            self.Deal['state'] = 'active'
            self.Deal['bg'] = 'white'
            PlaySound('sound/chip.wav', SND_FILENAME)
        else:
            self.betMoney -= 10

    def pressedCheck(self):
        self.betMoney += 1
        if 1 <= self.playerMoney:
            self.LbetMoney.configure(text='$' + str(self.betMoney))
            self.playerMoney -= self.betMoney
            self.LplayerMoney.configure(text='You have $' + str(self.playerMoney))
            self.Deal['state'] = 'active'
            self.Deal['bg'] = 'white'
            PlaySound('sound/chip.wav', SND_FILENAME)
        else:
            self.betMoney -= 1

    def deal(self):
        self.player.reset()
        self.dealer.reset()
        self.cardDeck = [i for i in range(52)]
        random.shuffle(self.cardDeck)
        self.deckN = 0

        self.hitPlayer(0)
        self.hitDealerDown(0)
        self.hitPlayer(1)
        self.hitDealerDown(1)

        self.nCardPlayer = 1
        self.nCardDealer = 1

        self.Check['state'] = 'active'
        self.Check['bg'] = 'white'
        self.BetX1['state'] = 'active'
        self.BetX1['bg'] = 'white'
        self.BetX2['state'] = 'active'
        self.BetX2['bg'] = 'white'
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'

    def hitPlayer(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player.addCard(newCard)
        p = PhotoImage(file='cards/' + newCard.filename())
        self.LCardPlayer.append(Label(self.window, image=p))

        self.LCardPlayer[self.player.inHand() - 1].image = p
        self.LCardPlayer[self.player.inHand() - 1].place(x=50 + n * 75, y=350)
        PlaySound('sounds/cardFlip1.wav', SND_FILENAME)

    def hitDealer(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.dealer.addCard(newCard)
        p = PhotoImage(file='cards/' + newCard.filename())
        self.LCardDealer.append(Label(self.window, image=p))

        self.LCardDealer[self.dealer.inHand() - 1].image = p
        self.LCardDealer[self.dealer.inHand() - 1].place(x=250 + n * 30, y=50)
        # self.LdealerPts.configure(text=str(self.player.value()))
        PlaySound('sounds/cardFlip1.wav', SND_FILENAME)

    def hitDealerDown(self,n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.dealer.addCard(newCard)
        p = PhotoImage(file='cards/b2fv.png')
        self.LCardDealer.append(Label(self.window, image=p))
        self.LCardDealer[self.dealer.inHand() - 1].image = p
        self.LCardDealer[self.dealer.inHand() - 1].place(x=50 + n * 75, y=50)
        # self.LdealerPts.configure(text=str(self.player.value()))
        PlaySound('sounds/cardFlip1.wav', SND_FILENAME)

    def pressedHit(self):
        self.nCardPlayer += 1
        self.hitPlayer(self.nCardPlayer)
        if self.player.value() > 21:
            self.checkWiner()

    def pressedStay(self):
        while (self.dealer.value() < 17):
            self.nCardDealer += 1
            self.hitDealer(self.nCardDealer)
        self.checkWiner()

    def pressedDeal(self):
        self.deal()

    def pressedAgain(self):
        self.player.reset()
        self.dealer.reset()
        self.nCardDealer = 0
        self.nCardPlayer = 0

        for i in self.LCardPlayer:
            i.destroy()
        for i in self.LCardDealer:
            i.destroy()
        self.Lstatus.configure(text='')
        self.LCardPlayer = []
        self.LCardDealer = []
        self.deckN = 0

        self.Check['state'] = 'active'
        self.Check['bg'] = 'white'
        self.BetX1['state'] = 'active'
        self.BetX1['bg'] = 'white'
        self.BetX2['state'] = 'active'
        self.BetX2['bg'] = 'white'

        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

    def checkWiner(self):
        p = PhotoImage(file='cards/' + self.dealer.cards[0].filename())
        self.LCardDealer[0].configure(image=p)
        self.LCardDealer[0].image = p



        if self.player.value() > 21:
            self.Lstatus.configure(text='Player Busts')
            PlaySound('sounds/wrong.wav', SND_FILENAME)
        elif self.dealer.value() > 21:
            self.Lstatus.configure(text='Dealer Busts')
            self.playerMoney += self.betMoney * 2
            PlaySound('sounds/win.wav', SND_FILENAME)
        elif self.dealer.value() == self.player.value():
            self.Lstatus.configure(text='Push')
            self.playerMoney += self.betMoney
        elif self.dealer.value() < self.player.value():
            self.Lstatus.configure(text='You Won!!')
            self.playerMoney += self.betMoney * 2
            PlaySound('sounds/win.wav', SND_FILENAME)
        else:
            self.Lstatus.configure(text='Sorry you lost!')
            PlaySound('sounds/wrong.wav', SND_FILENAME)
        self.betMoney = 0
        self.LplayerMoney.configure(text='You have $' + str(self.playerMoney))
        self.LbetMoney.configure(text='$' + str(self.betMoney))
        self.Check['state'] = 'disabled'
        self.Check['bg'] = 'gray'
        self.BetX1['state'] = 'disabled'
        self.BetX1['bg'] = 'gray'
        self.BetX2['state'] = 'disabled'
        self.BetX2['bg'] = 'gray'
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'active'
        self.Again['bg'] = 'white'

BlackJack()