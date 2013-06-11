#!/usr/bin/env python
# -*- coding: utf-8 -*-

def save_transaction(price, credit_card, description):
    file = open("transactions.txt", "a") # "a"表示把文件添加到结尾
    file.write("%16s%07d%s\n" % (credit_card, price*100, description))
    file.close()

