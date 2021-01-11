#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Created on Thu Aug  6 01:38:20 2020

@author: pranatagrawal
"""
path = "/home/pi/Downloads/Inventory/"

import tkinter as tk
from tkinter import ttk
from collections import deque
from stone_frames import HelloWorld, Stone, Match, Stone_cut
from stone_frames.untitled_folder_1 import Discription
from xlrd import open_workbook
from pyexcel_ods import get_data


def main():

    wb = get_data(path + "main_biggest.ods")
    stones_files = wb["Sheet1"]
    wb_1 = get_data(path + "main_biggest_cut_size.ods")
    stones_files_1 = wb_1["Sheet1"]
    stones = []
    stones_cut = []
    for i in range(1,len(stones_files_1)):
        if stones_files_1[i] != []:
            if stones_files_1[i][2] != [] and stones_files_1[i][1]!= [] and stones_files_1[i][3]!= [] and stones_files_1[i][5] != [] and stones_files_1[i][4] != []:
                stones_cut.append(Stone_cut(stones_files_1[i][2], stones_files_1[i][1], stones_files_1[i][3], stones_files_1[i][5], stones_files_1[i][4],stones_files_1[i][6], "1"))

    for i in range(1, len(stones_files)):
        if stones_files[i] != []:
            if stones_files[i][2] != [] and stones_files[i][1] != [] and stones_files[i][3] != [] and stones_files[i][6] != [] and stones_files[i][5] != [] and stones_files[i][4] != [] and stones_files[i][7] != []:
                stones.append(Stone(stones_files[i][2], stones_files[i][1], stones_files[i][3], stones_files[i][6], stones_files[i][5], stones_files[i][4], stones_files[i][7], stones_files[i][8]))
    return [stones_cut, stones]

list_data = main()
stones = list_data[1]
stones_cut = list_data[0]
match_stones = Match(stones)



class App_Stone(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.p = 1
        self.container = ttk.Frame(self)
        self.container.grid()
        self.container.columnconfigure(0, weight=1)
        self.discription_frame = 1
        self.frames = {}
        self.total_stock = self.total_stock(stones, stones_cut)
        hello_world_frame = HelloWorld(self.container, self, lambda: self.put_on_grid(),stones, self.total_stock, match_stones, stones_cut)
        hello_world_frame.grid(row=0, column=0, sticky="NESW")
        self.frames[HelloWorld] = hello_world_frame
        self.show_frame(HelloWorld)



    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

    def put_on_grid(self):
        self.discription_frame = Discription(self.container, self, self.p, self.put_hello)
        self.frames[Discription] = self.discription_frame
        self.discription_frame.grid(row=0, column=0, sticky="NESW")
        self.show_frame(Discription)

    def put_hello(self):
        self.show_frame(HelloWorld)

    def total_stock(self, stones, stones_cut):
        all_ = 0
        for i in stones:
            all_ += i.total_stock_all
        for i in stones_cut:
            all_ += i.total_stock_all
        return all_


app = App_Stone()
app.mainloop()