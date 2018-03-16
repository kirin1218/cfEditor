# -*- coding: utf-8 -*-
import csv
class csvParse():
    def __init__(self, csvpath = "" ):
        self.path = csvpath
        self.f = 0
        self.data = []

        if( csvpath != "" ):
            self.read()
        else:
            print("not path")
            
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
        return True 

    def CountCol(self):
        i=0
        for row in self.data:
            if i < len(row):
                i = len(row)
        return i

    def CountRow(self):
        return len(self.data)
