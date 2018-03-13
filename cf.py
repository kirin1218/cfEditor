# -*- coding: utf-8 -*-

class command_file():
    def __init__( self, cfpath ):
        self.path = cfpath

    def read( self ):
        print(self.path)
