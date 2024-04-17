from tkinter import *


class MainGUI:
    def compute(self):
        mrate = float(self.rate.get()) / 1200
        f = float(self.money.get()) * (1 + mrate) ** (float(self.years.get()) * 12)
        self.futureValue.set("{0:.2f}".format(f))

    def __init__(self):
        window = Tk()
        window.title("투자금 계산하기")
        Label(window, text="투자금").grid(row=0, column=0, sticky=W)
        Label(window, text="기간").grid(row=1, column=0, sticky=W)
        Label(window, text="연이율").grid(row=2, column=0, sticky=W)
        Label(window, text="미래가치").grid(row=3, column=0, sticky=W)
        self.money = StringVar()
        Entry(window, textvariable=self.money, justify=RIGHT).grid(row=0, column=1)
        self.years = StringVar()
        Entry(window, textvariable=self.years, justify=RIGHT).grid(row=1, column=1)
        self.rate = StringVar()
        Entry(window, textvariable=self.rate, justify=RIGHT).grid(row=2, column=1)
        self.futureValue = StringVar()
        Label(window, textvariable=self.futureValue).grid(row=3, column=1, sticky=W)

        Button(window, text="계산하기", command=self.compute).grid(row=4, column=1, sticky=E)

        window.mainloop()


MainGUI()
