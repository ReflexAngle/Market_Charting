from tkinter import *
from bs4 import BeautifulSoup
import requests
import statistics
import time

Window = Tk(className='Market Charting')
Window.geometry("800x400")

# scrapes the prices for each oif the markets.
# uses a loop to continuously scrape every 15 seconds.
# all three sources will be averaged out to try and get a
# more accurate number this is diffrent sources give diffrent numbers.
DOW = 'https://markets.businessinsider.com/futures/dow-futures'
SP = 'https://markets.businessinsider.com/futures/s&p-500-futures'
NAS = 'https://markets.businessinsider.com/index/nasdaq_100'

DOW2 = 'https://www.marketwatch.com/investing/index/djia'
SP2 = 'https://www.marketwatch.com/investing/index/spx'
NAS2 = 'https://www.marketwatch.com/investing/index/comp'

DOW3 = ''
SP3 = ''
NAS3 = ''

# each variable above is place in the array.
Markets = [DOW, SP, NAS]
Markets2 = [DOW2, SP2, NAS2]
Markets3 = [DOW3, SP3, NAS3]

Market_results = []

# runs each link through a loop to scrape the information.
# scrapes from business insider.
for i in Markets:
    page = i
    page = requests.get(page)
    soup = BeautifulSoup(page.text, "html.parser")

    result = soup.find('span', class_='price-section__current-value')
    result = result.string
    result = result.replace(',', '')
    # converts string to float to average out values.
    result = float(result)
    Market_results.append(result)

# scrapes fom market watch.
for i in Markets2:
    page2 = i
    page2 = requests.get(page2)
    soup = BeautifulSoup(page2.text, "html.parser")

    # had to use find twice to get result I was looking for on market watch.
    # tried this with other markets didn't have to do this twice.
    # well this is annoying the website switches HTML tags throughout the day.
    # use a try to try both bg-quote and span.
    try:
        result = soup.find('h2', class_='intraday__price')
        result = result.find('bg-quote', class_='value')
        result = result.string
        result = result.replace(',', '')
        result = float(result)
        Market_results.append(result)
    except:
        result = soup.find('h2', class_='intraday__price')
        result = result.find('span', class_='value')
        result = result.string
        result = result.replace(',', '')
        result = float(result)
        Market_results.append(result)
    # use else for safe measure
    else:
        result = 'invalid'
        Market_results.append(result)

# stores the variables from the array in individual variables.
# Average the results from the sources.
# 0 - 2 BI 3 - 5 MW.
# use a check to see if any equal invalid.
if Market_results[3] or Market_results[4] or Market_results[5] == 'invalid':
    Dow_A = Market_results[0]
    SP_A = Market_results[1]
    NAS_A = Market_results[2]
else:
    Dow_A = Market_results[0] + Market_results[3]
    SP_A = Market_results[1] + Market_results[4]
    NAS_A = Market_results[2] + Market_results[5]
    # rounds the number to the nearest hundred place so there isn't long decimal places for a price.
    Dow_A = round((Dow_A / 2), 2)
    SP_A = round((SP_A / 2), 2)
    NAS_A = round((NAS_A / 2), 2)

revert = [Dow_A, SP_A, NAS_A]
RevertS = []

for i in revert:
    revert = i
    revert = str(revert)
    revert = revert.join(',')
    RevertS.append(revert)
print(RevertS[0])

# print the prices from each market on the screen.
DLabel = Label(Window, text=Dow_A, font="ubuntu")
SLabel = Label(Window, text=SP_A, font="ubuntu")
NLabel = Label(Window, text=NAS_A, font="ubuntu")

# place labels on the screen
DLabel.grid(row=1, column=0)
SLabel.grid(row=1, column=1)
NLabel.grid(row=1, column=2)


# ____________________________________________________________________________________________________________________ #
# The part of the application that does stuff.
URL1 = 'https://markets.businessinsider.com/'
URL2 = 'https://www.marketwatch.com/'

# function for the commodity button.
def button_click():
    Stock_Input = input('')

    newLabel = Label(Window, text="Click")
    newLabel.grid(row=5, column=0)

    enter = Entry(Window)
    enter.grid(row=7, column=0)

    if enter == "v":
        print("hello")

# function for the stock button.
def other_click():
    second_label = Label(Window, text="other click")
    second_label.grid(row=5, column=0)

    enter = Entry(Window)
    enter.grid(row=7, column=0)


Name_Lable = Label(Window, text="Market Charting", font="ubuntu")

Commodity_Button = Button(Window, text="Commodity", command=button_click)
Stock_Button = Button(Window, text="Stock", command=button_click)

Name_Lable.grid(row=0, column=0)

Commodity_Button.grid(row=3, column=0)
Stock_Button.grid(row=3, column=1)

Window.mainloop()
