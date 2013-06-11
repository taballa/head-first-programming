#!/usr/bin/env python
# -*- coding: utf-8 -*-

def save_transaction(price, credit_card, description):
    file = open("transactions.txt", "a") # "a"表示把文件添加到结尾
    file.write("%16s%07d%s\n" % (credit_card, price*100, description))
    file.close()

items = ["DONUT", "LATTE", "FILTER", "MUFFIN"]
price = [1.50, 2.0, 1.80, 1.20]
running = True

while running:
    option = 1
    for choice in items:
       print(str(option) + '. ' + choice) 
       option = option + 1
    print(str(option) + ". Quit")
    choice = int(input("Choose an option: "))
    if choice == option:
        running = False
    else:
        credit_card = input("Credit card number: ")
        save_transaction(price[choice - 1], credit_card, items[choice - 1])