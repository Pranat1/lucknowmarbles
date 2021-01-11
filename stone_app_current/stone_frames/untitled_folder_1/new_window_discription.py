#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 01:10:20 2020

@author: pranatagrawal
"""

from pyexcel_ods import save_data
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk
import copy
from pyexcel_ods import get_data
import os
from collections import OrderedDict
#path = "/home/pi/Desktop/my_drive/Lucknow_Marbles/stone_app_current/"
path =  "/home/pi/Downloads/Inventory/"


class Discription(ttk.Frame):
    def __init__(self, parent, controller, p, back):
        super().__init__(parent)
        self.corrent_stone = p
        self.butten_checked = []
        self.list_ = []
        self.list_2 = []
        stone_keys = list(self.corrent_stone.stock.keys())
        #image_ = Image.open(self.corrent_stone.image)
        #photo = ImageTk.PhotoImage(image_)
        #label = ttk.Label(self, image = photo)
        #label.image = photo
        #label.grid(row = 1,column = 0)
        myEntry_1 = ttk.Entry(self)
        myEntry_1.grid(row = 0, column = 0)
        myEntry_2 = ttk.Entry(self)
        myEntry_2.grid(row = 0, column = 1)
        myButton = ttk.Button(self, text = "Cost Cut to size", command = lambda: self.display_cost(myEntry_1, myEntry_2))
        myButton.grid(row =2, column = 1)
        myLabel_1 = ttk.Label(self, text = "length")
        myLabel_1.grid(row =1, column = 0)
        myLabel_2 = ttk.Label(self, text = "width")
        myLabel_2.grid(row =1, column = 1)
        myButton_2 = ttk.Button(self, text = "Cost of Piece", command = lambda: self.cost_of_piece_())
        myButton_2.grid(row =4, column = 1)
        myEntry_3 = ttk.Entry(self)
        myEntry_3.grid(row = 5, column = 1)
        myButton_3 = ttk.Button(self, text = "Buy", command = lambda: self.buy(myEntry_3))
        myButton_3.grid(row =6, column = 1)
        myLabel_3 = ttk.Label(self, text = "Bill No")
        myLabel_3.grid(row = 5, column = 0)
        my_button_9 = ttk.Button(self, text = "Back", command = back)
        my_button_9.grid(row = 7, column= 1)


        for j in range(len(stone_keys)):
            pieces_keys = list(self.corrent_stone.stock[stone_keys[j]].keys())
            for i in range(len(pieces_keys)):
                myLabel2 = ttk.Label(self, text = pieces_keys[i] + "length = " + str(self.corrent_stone.stock[stone_keys[j]][pieces_keys[i]][0])+ " width =" + str(self.corrent_stone.stock[stone_keys[j]][pieces_keys[i]][1]))
                if 0 <= i < 12:
                    myLabel2.grid(row = i, column = 2+j*4)
                if 12 <= i < 24:
                    myLabel2.grid(row = i-12, column = 4+j*4)
                if 24 <= i < 36:
                    myLabel2.grid(row = i-24, column = 6+j*4)
                if 36 <= i <= 48:
                    myLabel2.grid(row = i-36, column = 8+j*4)
                if 48 <= i < 60:
                    myLabel2.grid(row = i-48, column = 10+j*4)
                if 60 <= i <= 72:
                    myLabel2.grid(row = i-60, column = 12+j*4)
                if 72 <= i <= 84:
                    myLabel2.grid(row = i-72, column = 14+j*4)
                int_var = tk.IntVar()
                check_button = ttk.Checkbutton(self, variable = int_var, onvalue = 1, offvalue = 0)
                if 0 <= i < 12:
                    check_button.grid(row = i, column = 3+j*4)
                if 12 <= i < 24:
                    check_button.grid(row = i-12, column = 5+j*4)
                if 24 <= i < 36:
                    check_button.grid(row =i-24, column = 7+j*4)
                if 36 <= i < 48:
                    check_button.grid(row = i-36, column = 9+j*4)
                if 48 <= i < 60:
                    check_button.grid(row = i-48, column = 11+j*4)
                if 60 <= i <= 72:
                    check_button.grid(row = i-60, column = 13+j*4)
                if 72 <= i <= 84:
                    check_button.grid(row = i-72, column = 15+j*4)
                self.butten_checked.append(int_var)
                a = self.corrent_stone.stock[stone_keys[j]][pieces_keys[i]]
                print(a)
                self.list_.append((float(a[0])*float(a[1]))*float(self.corrent_stone.price)/144.0)
                self.list_2.append(str(stone_keys[j]) + str(pieces_keys[i]))


    def display_cost(self, myEntry_1, myEntry_2):

        if int(myEntry_1.get())%3 != 0 and int(myEntry_2.get())%3 != 0:
            myLabel3 = ttk.Label(self, text = ("price = " + str(((3-int(myEntry_1.get())%3)+int(myEntry_1.get()))*((3-int(myEntry_2.get())%3)+int(myEntry_2.get()))*float(self.corrent_stone.cut_price)/144.0)))

        if int(myEntry_1.get())%3 == 0 and int(myEntry_2.get())%3 != 0:
            myLabel3 = ttk.Label(self, text = ("price = " + str((int(myEntry_1.get()))*((3-int(myEntry_2.get())%3)+int(myEntry_2.get()))*float(self.corrent_stone.cut_price)/144.0)))

        if int(myEntry_1.get())%3 != 0 and int(myEntry_2.get())%3 == 0:
            myLabel3 = ttk.Label(self, text = ("price = " + str(((3-int(myEntry_1.get())%3)+int(myEntry_1.get()))*(int(myEntry_2.get()))*float(self.corrent_stone.cut_price)/144.0)))

        if int(myEntry_1.get())%3 == 0 and int(myEntry_2.get())%3 == 0:
            myLabel3 = ttk.Label(self, text = ("price = " + str((int(myEntry_1.get()))*((int(myEntry_2.get()))*float(self.corrent_stone.cut_price)/144.0))))
        myLabel3.grid(row = 3, column = 1)


    def cost_of_piece_(self):
        cost = 0
        for i in range(len(self.butten_checked)):
            list_ = self.butten_checked[i].get()
            if list_ == 1:
                cost += self.list_[i]
        myLabel3 = ttk.Label(self, text = cost)
        myLabel3.grid(row = 5, column = 1)
    def buy(self, myEntry_3):

        data = get_data(path + "Sale_data_2020.ods")["Sheet1"]
        for i in range(len(self.butten_checked)):
            list_ = self.butten_checked[i].get()
            if list_ == 1:
                data.append([myEntry_3.get(), self.list_2[i]])
        data_1 = OrderedDict()
        data_1.update({"Sheet1": data})
        os.remove(path + "Sale_data_2020.ods")
        save_data(path + "Sale_data_2020.ods",  data_1)