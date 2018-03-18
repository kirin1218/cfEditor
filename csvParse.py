# -*- coding: utf-8 -*-
import csv
class csvParse():
    def __init__(self, csvpath = "" ):
        self.path = csvpath
        self.f = 0
        self.data = []
        self.col = 0
        self.row = 0

        if( csvpath != "" ):
            self.read()
        else:
            print("not path")
    
    def read2(self):
        try:
            with open(self.path,'r') as f:
                line = f.readline()

                while line:
                    #çsÇ≤Ç∆ÇÃèàóù
                    line = f.readline()
        except IOError:

            
    def read(self):
        try:
            with open(self.path,'r') as f:
                i = 0
                reader = csv.reader(f)
                #header = next(reader)
                for row in reader:
                    self.data.append([])
                    for cell in row:
                        self.data[i].append(cell)
                    i=i+1
        except IOError:
            self.f = 0
            return False 
        self.col = CountCol()
        self.row = CountRow()
        return True 

    def Col(self):
        return self.col

    def Row(self):
        return self.row

    def CountCol(self):
        i=0
        for row in self.data:
            if i < len(row):
                i = len(row)
        return i

    def CountRow(self):
        return len(self.data)
