#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 21:56:49 2020

@author: pranatagrawal
"""

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
from PIL import Image, ImageTk
from xlrd import open_workbook
from PIL import Image, ImageTk
from typing_extensions import Final
from stone_frames.untitled_folder_1 import Discription
"""read the files"""
"""create granites"""
"""add them in a list"""
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk
from pyexcel_ods import get_data


import copy






def shortlist(list_of_types_of_granites, catagory):
    shortlested_granites = []
    for i in range(list_of_types_of_granites):
        if i.color == catagory:
            shortlested_colors.append(i)
    return shortlested_granites

class Stone:
    def __init__(self, color, price, quality, list_thappi_files_and_serialnumbers, stone_type, name_of_stone, cut_price, image):

        #:param color:
        #:param price:
        #:param stock: is a dictionary with keys as length, width and seriel number.
        #:param size:
        #:param quality:
        self.image = image
        self.name_of_stone = name_of_stone
        self.thickness = {}
        self.stone_type = stone_type
        self.color = color
        self.price = price
        self.cut_price = cut_price
        self.quality = quality
        self.total_stock = {}
        self.average_size = {}
        self.stock = {}
        self.pieces = {}
        wb = open_workbook("/Users/pranatagrawal/Stones/" + list_thappi_files_and_serialnumbers)
        files = []
        for sheet in wb.sheets():
            number_of_rows = sheet.nrows
            number_of_columns = sheet.ncols
            items = []

            rows = []
            for row in range(0, number_of_rows):
                values = []
                for col in range(0, number_of_columns):
                    value = (sheet.cell(row, col).value)
                    values.append(value)
                files.append(values)

        for n in range(1, len(files)):
            wb = open_workbook("/Users/pranatagrawal/Stones/" + files[n][1])
            a = []
            for sheet in wb.sheets():
                number_of_rows = sheet.nrows
                number_of_columns = sheet.ncols
                items = []
                rows = []
                for row in range(0, number_of_rows):
                    values = []
                    for col in range(0, number_of_columns):
                        value = (sheet.cell(row, col).value)
                        values.append(value)
                    a.append(values)
            self.stock[files[n][
                0]] = {}  # list of pieces (piece number) and their sizes
            total_area = 0
            length_total = 0
            width_total = 0
            for i in range(1, len(a)):
                self.stock[files[n][0]][a[i][0]] = [a[i][1], a[i][2]]
                total_area += float(a[i][1]) * float(a[i][2])
                length_total += float(a[i][1])
                width_total += float(a[i][2])
            self.total_stock[files[n][0]] = total_area
            self.pieces[files[n][0]] = len(self.stock[files[n][0]])
            self.average_size[files[n][0]] = [length_total/self.pieces[files[n][0]], width_total / self.pieces[files[n][0]]]
            self.thickness[files[n][0]] = files[n][2]

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
                while  i.average_size[j][0] > float(length_) and i.average_size[j][1] > float(width_) and n < 1:
                    set_of_stones_length_width.add(i)
                    n += 1
        return set_of_stones_length_width
                    

    def shortlist_price(self, low, high, cut_or_uncut):
        shortlested_granites = set()
        for i in range(len(self.list_of_types_of_granites)):
            if cut_or_uncut == 0:
                if low != "" or high != "":
                    if low ==  "":
                        if 0 < float(self.list_of_types_of_granites[i].price) < float(high):
                            shortlested_granites.add(self.list_of_types_of_granites[i])
                    if high ==  "":
                        if float(low) < float(self.list_of_types_of_granites[i].price) < 0:
                            shortlested_granites.add(self.list_of_types_of_granites[i])
                    if low != "" and high != "":
                        if float(low) < float(self.list_of_types_of_granites[i].price) < float(high):
                            shortlested_granites.add(self.list_of_types_of_granites[i])
            if cut_or_uncut == 1:
                if low != "" or high != "":
                    if low ==  "":
                        if 0 < float(self.list_of_types_of_granites[i].cut_price) < float(high):
                            shortlested_granites.add(self.list_of_types_of_granites[i])
                    if high ==  "":
                        if float(low) < float(self.list_of_types_of_granites[i].cut_price) < 0:
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

    def __init__(self, parent, controller, put_on_grid, stones):
        super().__init__(parent)
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
        r = tk.IntVar()
        self.selected_option = tk.IntVar()
        check = tk.Checkbutton(
        self,
        text="Cut_to_size",
        variable=self.selected_option,
        onvalue=1,
        offvalue=0)
        check.grid(row = 9, column = 2, pady=10, padx=10)

        for i in range(len(self.stones)):
            button = ttk.Radiobutton(self, text = self.stones[i].name_of_stone, variable = r, value = i, command = lambda: self.product_details(r.get()))
            self.my_buttons.append(button)
            button.grid(row=i, column =0,pady=10, padx=10)
        for i in range(9):
            myLabel1 = ttk.Label(self, text = self.list_[i])
            myLabel1.grid(row=i, column =1,pady=10, padx=10)
            myEntry = ttk.Entry(self)
            myEntry.grid(row=i, column= 2, pady=10, padx=10)
            self.myentries.append(myEntry)
        
        myButton_1 = ttk.Button(self, text = "submit" , command = lambda:self.function_())
        myButton_1.grid(row=10, column =2, pady=20)
    
    def function_(self):

        list_of_stones = [set(), set(), set(), set(), set(), set(), set()]
        set_a = set()
        store = [self.myentries[0].get(), self.myentries[1].get(), self.myentries[2].get(), self.myentries[3].get(), self.myentries[4].get(), self.myentries[5].get(), self.myentries[6].get(), self.myentries[7].get(), self.myentries[8].get()]
        b = self.stones
        if "" != store[4] or "" != store[5]:
            list_of_stones[4] = match_stones.shortlist_price(store[4], store[5], self.selected_option.get())
        if "" == store[4] or  "" == store[5]:
            list_of_stones[4] = set_a
        if "" != store[7] or "" != store[8]:
            list_of_stones[6] = match_stones.shortlist_length_width(store[7],store[8])
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
                list_of_stones[5] = match_stones.have_stock(store[6])
            if "" == store[6]:
                list_of_stones[5] = set_a
        set_of_intersection = list_of_stones[0].intersection(list_of_stones[1], list_of_stones[2], list_of_stones[3], list_of_stones[4], list_of_stones[5])
        list_of_intersect_1 = list(set_of_intersection)

        list_of_intersect = copy.deepcopy(list_of_intersect_1)
        self.list_of_intersect = list_of_intersect
        for i in self.my_buttons:
            i.grid_forget()
        r_1 = tk.IntVar()
        for q in range(len(list_of_intersect)):
            button = ttk.Radiobutton(self, text = list_of_intersect[q].name_of_stone, variable = r_1, value = q, command = lambda: self.product_details(r_1.get()))
            self.my_buttons.append(button)
            button.grid(row= q, column =0,pady=10, padx=10)
    
    
    def product_details(self, r):
        stock_required = self.myentries[6].get()
        if self.labels_discription != []:
            for i in self.labels_discription:
                i.grid_forget()
        
        for p in range(len(self.list_of_intersect)):
            if p == r:
                self.controller.p = self.list_of_intersect[p]
                myButton2 = ttk.Button(self, text=self.list_of_intersect[p].name_of_stone, command = self.put_on_grid)
                myButton2.grid(row=0, column =3,pady=10, padx=10)
                myButton2 = ttk.Button(self, text=self.list_of_intersect[p].name_of_stone, command = lambda: self.controller.show_frame(Discription))
                myButton2.grid(row=0, column =4,pady=10, padx=10)
                myLabel3 = ttk.Label(self, text=self.list_of_intersect[p].color)
                myLabel3.grid(row=1, column =3,pady=10, padx=10)
                myLabel4 = ttk.Label(self, text="price = "+str(self.list_of_intersect[p].price))
                myLabel4.grid(row=2, column =3,pady=10, padx=10)
                myLabel5 = ttk.Label(self, text=self.list_of_intersect[p].stone_type)
                myLabel5.grid(row=3, column =3,pady=10, padx=10)
                myLabel6 = ttk.Label(self, text="cut price = "+str(self.list_of_intersect[p].cut_price))
                myLabel6.grid(row=4, column =3,pady=10, padx=10)
                list_of_keys = list(self.list_of_intersect[p].total_stock.keys())
                self.labels_discription.append(myButton2)
                self.labels_discription.append(myLabel3)
                self.labels_discription.append(myLabel4)
                self.labels_discription.append(myLabel5)
                for l in range(len(list_of_keys)):
                    if stock_required != "":
                        k = self.list_of_intersect[p].total_stock[list_of_keys[l]]
                        if float(stock_required) < k:
                            myLabel6 = ttk.Label(self, text = "" + "stock_avalable =" + str(k))
                            myLabel6.grid(row=l, column =4,pady=10, padx=10)
                            self.labels_discription.append(myLabel6)
                    myLabel7 = ttk.Label(self, text = "" + "average_size =" + str(self.list_of_intersect[p].average_size[list_of_keys[l]][0])+", "+ str(self.list_of_intersect[p].average_size[list_of_keys[l]][1]))
                    myLabel7.grid(row=l, column =5,pady=10, padx=10)
                    """
                        if stock_required == "":
                            myLabel6 = ttk.Label(self, text = "" + "stock_avalable =" + str(k))
                            myLabel6.grid(row=5, column =l,pady=10, padx=10)
                            self.labels_discription.append(myLabel6)
                    """

    
#class sale:
#    def __init__(self, amount, rate, name_of_stone, date, time, list_of_peaces):


