#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 00:55:36 2020

@author: pranatagrawal
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 02:10:50 2020

@author: pranatagrawal
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 03:18:54 2020

@author: pranatagrawal
"""
#path = "/home/pi/Desktop/my_drive/Lucknow_Marbles/stone_app_current/"
path = os.getcwd() + "/Inventory/"

from xlrd import open_workbook
from PIL import Image, ImageTk
from stone_frames.untitled_folder_1 import Discription
"""read the files"""
"""create granites"""
"""add them in a list"""
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk
from pyexcel_ods import get_data
from collections import OrderedDict
import os
from pyexcel_ods import save_data

import copy

def shortlist(list_of_types_of_granites, catagory):
    shortlested_granites = []
    for i in range(list_of_types_of_granites):
        if i.color == catagory:
            shortlested_colors.append(i)
    return shortlested_granites

class Stone_cut:
        def __init__(self, color, price, quality, stone_type, name_of_stone,file, img_paths):
            self.img_paths = img_paths
            self.name_of_stone = name_of_stone
            self.thickness = {}
            self.stone_type = stone_type
            self.color = color
            self.price = price
            self.quality = quality
            self.total_stock = {}
            self.total_stock_all = 0
            self.stock = {}
            self.pieces = {}
            self.prices = []
            list_of_sold = {}
            list_thappi_files_and_serialnumbers = file
            sold = get_data(path + "Sale_data_2020_cut_size.ods")["Sheet1"]
            wb = get_data(path + list_thappi_files_and_serialnumbers)
            files = wb["Sheet1"]
            sold = sold[1:]
            for i in range(1, len(files)):
                if files[i] != []:
                    list_of_sold[str(files[0][0]+files[i][0])] = 0
            for i in sold:
                if i != []:
                    print(i[1])
                    if i[1][0] == files[0][0][0] and i[1][1] == files[0][0][1] and i[1][2] == files[0][0][2]:
                        list_of_sold[i[1]] += float(i[2])
            for n in range(1, len(files)):
                if files[n] != []:
                    number_left = files[n][1] - list_of_sold[(files[0][0] + files[n][0])]
                    self.stock[files[n][0]] = [number_left, files[n][2], files[n][3]]
                    self.total_stock_all += (files[n][2]*files[n][3]*number_left)/144
                    self.prices.append(files[n][4])


class Stone:
    def __init__(self, color, price, quality, list_thappi_files_and_serialnumbers, stone_type, name_of_stone, cut_price, img_paths):

        #:param color:
        #:param price:
        #:param stock: is a dictionary with keys as length, width and seriel number.
        #:param size:
        #:param quality:
        self.img_paths = img_paths
        self.name_of_stone = name_of_stone
        self.thickness = {}
        self.stone_type = stone_type
        self.color = color
        self.price = price
        self.cut_price = cut_price
        self.quality = quality
        self.total_stock = {}
        self.total_stock_all = 0
        self.average_size = {}
        self.stock = {}
        self.pieces = {}
        list_of_sold = []
        sold = get_data(path + "Sale_data_2020.ods")["Sheet1"]
        wb = get_data(path + list_thappi_files_and_serialnumbers)
        files = wb["Sheet1"]
        sold = sold[1:]
        for i in sold:
            if i != []:
                list_of_sold.append(i[1])
        for n in range(1, len(files)):
            if files[n] != []:
                wb = get_data(path + files[n][1])
                a = wb["Sheet1"]
                self.stock[files[n][
                    0]] = {}  # list of pieces (piece number) and their sizes
                total_area = 0
                length_total = 0
                width_total = 0
                #print(a)
                print(a)
                for i in range(1, len(a)):
                    if a[i] != []:
                        if not(str(files[n][0]) +str(a[i][0]) in list_of_sold):
                            self.stock[files[n][0]][a[i][0]] = [a[i][1], a[i][2]]
                            total_area += float(a[i][1]) * float(a[i][2])
                            length_total += float(a[i][1])
                            width_total += float(a[i][2])
                self.pieces[files[n][0]] = len(self.stock[files[n][0]])
                if self.pieces[files[n][0]] != 0:
                    self.total_stock[files[n][0]] = total_area/144.0
                    self.average_size[files[n][0]] = [length_total/self.pieces[files[n][0]], width_total / self.pieces[files[n][0]]]
                    self.total_stock_all += total_area/144.0
                    #self.thickness[files[n][0]] = files[n][2]



    def is_in(self, list_):
        for i in list_:
            if self.name_of_stone == i.name_of_stone and self.thickness == i.thickness and self.stone_type == i.stone_type and self.quality == i.quality and self.average_size == i.average_size and self.price == i.price and self.total_stock == i.total_stock and self.average_size == i.average_size:
                return True
        return False


class Match:
    def __init__(self, list_of_types_of_granites):
        self.list_of_types_of_granites = list_of_types_of_granites

    def shortlist_color(self, color):
        shortlist(self.list_of_types_of_granites, color)

    def shortlist_length_width(self, length_, width_):
        set_of_stones_length_width = set()
        for i in self.list_of_types_of_granites:
            stock_keys = i.average_size.keys()
            n = 0
            for j in stock_keys:
                if length_ != "" and width_ != "":
                    if i.average_size[j][0] > float(length_) and i.average_size[j][1] > float(width_) and n < 1:

                        set_of_stones_length_width.add(i)
                        n += 1
                if length_ != "" and  width_ == "":
                    if i.average_size[j][0] > float(length_) and i.average_size[j][1] > 0.0 and n < 1:
                        set_of_stones_length_width.add(i)
                        n += 1
                if length_ == "" and  width_ != "":
                    if i.average_size[j][0] > 0.0 and i.average_size[j][1] > float(width_) and n < 1:
                        set_of_stones_length_width.add(i)
                        n += 1
        return set_of_stones_length_width


    def shortlist_price(self, low, high, cut_or_uncut):
        shortlested_granites = set()
        for i in range(len(self.list_of_types_of_granites)):
            if cut_or_uncut == 0:
                if low ==  "":
                    if 0.0 < float(self.list_of_types_of_granites[i].price) < float(high):
                        shortlested_granites.add(self.list_of_types_of_granites[i])
                if high ==  "":
                    if float(low) < float(self.list_of_types_of_granites[i].price) < 100000.0:
                        shortlested_granites.add(self.list_of_types_of_granites[i])
                if low != "" and high != "":
                    if float(low) < float(self.list_of_types_of_granites[i].price) < float(high):
                        shortlested_granites.add(self.list_of_types_of_granites[i])
            if cut_or_uncut == 1:
                if low ==  "":
                    if 0.0 < float(self.list_of_types_of_granites[i].cut_price) < float(high):
                        shortlested_granites.add(self.list_of_types_of_granites[i])
                if high ==  "":
                    if float(low) < float(self.list_of_types_of_granites[i].cut_price) < 100000.0:
                        shortlested_granites.add(self.list_of_types_of_granites[i])
                if low != "" and high != "":
                    if float(low) < float(self.list_of_types_of_granites[i].cut_price) < float(high):
                        shortlested_granites.add(self.list_of_types_of_granites[i])
        return shortlested_granites

    def have_stock(self, stock_demanded):
        shortlested_granites = set()
        for i in self.list_of_types_of_granites:
            list_of_keys = list(i.total_stock.keys())
            n = 0
            l = 0
            while n <= 1 and l < len(list_of_keys):
                if float(i.total_stock[list_of_keys[l]]) > float(stock_demanded):
                    n += 1
                    shortlested_granites.add(i)
                    #print(list_of_keys)
                l += 1
        return shortlested_granites

    def shortlist_quality(self, quality):
        shortlist(self.list_of_types_of_granites, quality)

    def sort_according_to_price(self):
        prices = []
        for i in range(self.list_of_types_of_granite):
            prices.append(i.price)
        prices.sort()
        copy_prices = copy.deepcopy(prices)
        #for i in range(self.list_of_types_of_granite):
        #   if
        return
#insert_new_granites()



class HelloWorld(ttk.Frame):

    def __init__(self, parent, controller, put_on_grid, stones, total_stock, match_stones, stones_cut):
        super().__init__(parent)
        for j in range(11):
            self.grid_rowconfigure(j, weight = 1)


        for i in range(5):
            self.columnconfigure(i, weight = 1)
        self.list_of_entries = []
        self.stones_cut = stones_cut
        self.match_stones = match_stones
        self.put_on_grid = put_on_grid

        self.parent = parent
        self.stones = stones
        self.list_= ["name_of_stone", "thickness", "stone_type", "color", "min_price", "max_price", "quontity_required", "length", "width"]
        self.myentries = []
        self.list_of_intersect = stones
        self.my_buttons = []
        self.radio_button_selected = 0
        self.labels_discription = []
        self.controller = controller
        self.corrent_stone = []
        self.my_buttons_cut =[]
        self.labels_discription_cut = []
        self.selected_cut = tk.IntVar
        r = tk.IntVar()
        self.selected_option = tk.IntVar()
        check = tk.Checkbutton(
        self,
        text="Cut_to_size",
        variable=self.selected_option,
        onvalue=1,
        offvalue=0)
        self.grid_rowconfigure(9,weight=1)
        self.grid_columnconfigure(2,weight=1)
        check.grid(row = 9,column = 2)
        len_stones = len(self.stones)
        for i in range(len_stones):
            button = ttk.Radiobutton(self, text = self.stones[i].name_of_stone, variable = r, value = i, command = lambda: self.product_details(r.get()))

            self.my_buttons.append(button)

            if 0 <= i < 12:

                button.grid(row = i, column = 0)
            if 12 <= i < 24:

                button.grid(row = i-12, column = 1)

            if 24 <= i < 36:

                button.grid(row = i-24, column = 2)
            if 36 <= i < 48:

                button.grid(row = i-36, column = 3)
        for i in range(len(self.stones_cut)):
            button = ttk.Radiobutton(self, text = self.stones_cut[i].name_of_stone, variable = r, value = i+len_stones, command = lambda: self.product_details_cut(r.get()))
            self.my_buttons_cut.append(button)
            button.grid(row = (i+len_stones)%12, column = (i+len_stones)//12)
            self.my_buttons.append(button)



        for i in range(9):
            myLabel1 = ttk.Label(self, text = self.list_[i])

            myLabel1.grid(row = i, column= 4)
            myEntry = ttk.Entry(self)
            myEntry.grid(row = i, column= 5)
            self.myentries.append(myEntry)


        myButton_1 = ttk.Button(self, text = "submit" , command = lambda:self.function_())
        myButton_1.grid(row = 10, column=5)


        myLabel_6 = ttk.Label(self, text = "total_stock = " + str(int(total_stock)))
        myLabel_6.grid(row=11, column = 4)









    def function_(self):

        list_of_stones = [set(), set(), set(), set(), set(), set(), set()]
        set_a = set()
        store = [self.myentries[0].get(), self.myentries[1].get(), self.myentries[2].get(), self.myentries[3].get(), self.myentries[4].get(), self.myentries[5].get(), self.myentries[6].get(), self.myentries[7].get(), self.myentries[8].get()]
        b = self.stones
        if "" != store[4] or "" != store[5]:
            list_of_stones[4] = self.match_stones.shortlist_price(store[4], store[5], self.selected_option.get())
        if "" == store[4] and  "" == store[5]:
            list_of_stones[4] = set_a
        if "" != store[7] or "" != store[8]:
            list_of_stones[6] = self.match_stones.shortlist_length_width(store[7],store[8])
        if "" == store[7] and "" == store[8]:
            list_of_stones[6] = set_a
        if "" == store[0]:
            list_of_stones[0] = set_a
        for k in self.stones:
            set_a.add(k)
        for j in range(len(self.stones)):
            if self.stones[j].name_of_stone == store[0]:
                list_of_stones[0].add(b[j])
            if "" == store[1]:
                list_of_stones[1] = set_a
            if self.stones[j].stone_type == store[2]:
                list_of_stones[2].add(b[j])
            if "" == store[2]:
                list_of_stones[2] = set_a
            if self.stones[j].color == store[3]:
                list_of_stones[3].add(b[j])
            if "" == store[3]:
                list_of_stones[3] = set_a
            if "" != store[6]:
                list_of_stones[5] = self.match_stones.have_stock(store[6])
            if "" == store[6]:
                list_of_stones[5] = set_a
        set_of_intersection = list_of_stones[0].intersection(list_of_stones[1], list_of_stones[2], list_of_stones[3], list_of_stones[4], list_of_stones[5], list_of_stones[6])
        list_of_intersect_1 = list(set_of_intersection)

        list_of_intersect = copy.deepcopy(list_of_intersect_1)
        self.list_of_intersect = list_of_intersect
        for i in self.my_buttons:
            i.grid_forget()
        r_1 = tk.IntVar()
        for q in range(len(list_of_intersect)):
            button = ttk.Radiobutton(self, text = list_of_intersect[q].name_of_stone, variable = r_1, value = q, command = lambda: self.product_details(r_1.get()))
            self.my_buttons.append(button)
            if 0 <= q < 12:
                button.grid(row= q, column =0,pady=10, padx=10)
            if 12 <= q < 24:
                button.grid(row= q-12, column =1,pady=10, padx=10)
            if 24 <= q < 36:
                button.grid(row= q-24, column =2,pady=10, padx=10)
            if 36 <= q < 48:
                button.grid(row= q-36, column =3,pady=10, padx=10)


    def product_details(self, r):
        if self.labels_discription_cut != []:
            for i in self.labels_discription_cut:
                i.grid_forget()
        stock_required = self.myentries[6].get()
        if self.labels_discription != []:
            for i in self.labels_discription:
                i.grid_forget()

        for p in range(len(self.list_of_intersect)):
            if p == r:
                self.controller.p = self.list_of_intersect[p]
                myButton2 = ttk.Button(self, text=self.list_of_intersect[p].name_of_stone, command = self.put_on_grid)
                myButton2.grid(row=0, column =6,pady=10, padx=10)
                myLabel3 = ttk.Label(self, text=self.list_of_intersect[p].color)
                myLabel3.grid(row=1, column =6,pady=10, padx=10)
                myLabel4 = ttk.Label(self, text="price = "+str(self.list_of_intersect[p].price))
                myLabel4.grid(row=2, column =6,pady=10, padx=10)
                myLabel5 = ttk.Label(self, text=self.list_of_intersect[p].stone_type)
                myLabel5.grid(row=3, column =6,pady=10, padx=10)
                myLabel6 = ttk.Label(self, text="cut price = "+str(self.list_of_intersect[p].cut_price))
                myLabel6.grid(row=4, column =6,pady=10, padx=10)
                list_of_keys = list(self.list_of_intersect[p].total_stock.keys())
                self.labels_discription.append(myButton2)
                self.labels_discription.append(myLabel3)
                self.labels_discription.append(myLabel4)
                self.labels_discription.append(myLabel5)
                if self.list_of_intersect[p].img_paths != "1":
                    canvas = tk.Canvas(self, width=300, height=300)
                    img = ImageTk.PhotoImage(Image.open(path + self.list_of_intersect[p].img_paths))
                    canvas.grid(row = 7, column = 8)
                    canvas.create_image(20, 20, anchor="center", image=img)
                    canvas.image = img
                for l in range(len(list_of_keys)):
                    k = self.list_of_intersect[p].total_stock[list_of_keys[l]]
                    myLabel6 = ttk.Label(self, text = "" + "stock_avalable = " + str(int(k)))
                    myLabel6.grid(row=l, column =7,pady=10, padx=10)
                    self.labels_discription.append(myLabel6)
                    myLabel7 = ttk.Label(self, text = "" + "average_size = " + str(int(self.list_of_intersect[p].average_size[list_of_keys[l]][0]))+", "+ str(int(self.list_of_intersect[p].average_size[list_of_keys[l]][1])))
                    myLabel7.grid(row=l, column =8,pady=10, padx=10)
                    self.labels_discription.append(myLabel6)
                    self.labels_discription.append(myLabel7)


                """
                    if stock_required == "":
                        myLabel6 = ttk.Label(self, text = "" + "stock_avalable =" + str(k))
                        myLabel6.grid(row=5, column =l,pady=10, padx=10)
                        self.labels_discription.append(myLabel6)
                """
    def product_details_cut(self, r):
        if self.labels_discription != []:
            for i in self.labels_discription:
                i.grid_forget()
        if self.labels_discription_cut != []:
            for i in self.labels_discription_cut:
                i.grid_forget()
        len_stones = len(self.stones)
        for i in range(len(self.stones_cut)):
            if (i + len_stones) == r:
                #exec("self.controller(" + str(len_stones) + ") = self.stones_cut[i]")
                keys_stock = list(self.stones_cut[i].stock.keys())
                for j in range(len(keys_stock)):
                    myLabel3 = ttk.Label(self, text = self.stones_cut[i].prices[j])
                    myLabel3.grid(row=j%11, column=8+(j//11)*3)
                    myLabel1 = ttk.Label(self, text = str(self.stones_cut[i].stock[keys_stock[j]][1]) + " * " + str(self.stones_cut[i].stock[keys_stock[j]][2]))
                    myLabel1.grid(row= j%11, column =7+(j//11)*3,pady=10, padx=10)
                    myLabel2 = ttk.Label(self, text = str("stock avalable = " + str(self.stones_cut[i].stock[keys_stock[j]][0])))
                    myLabel2.grid(row= j%11, column =6+(j//11)*3,pady=10, padx=10)
                    self.labels_discription_cut.extend([myLabel2,myLabel1,myLabel3])
    def change(self, i, key, j):
        data = get_data(path + "Sale_data_2020_cut_size.ods")["Sheet1"]
        to_append = [self.list_of_entries[j][0].get(),key, self.list_of_entries[j][1].get()]
        data.append(to_append)

        data_1 = OrderedDict()
        data_1.update({"Sheet1": data})
        os.remove(path + "Sale_data_2020_cut_size.ods")
        save_data(path + "Sale_data_2020_cut_size.ods",  data_1)




#class sale:
#    def __init__(self, amount, rate, name_of_stone, date, time, list_of_peaces):
