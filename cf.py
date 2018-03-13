# -*- coding: utf-8 -*-

class command_file():
    def __init__( self, cfpath ):
        self.path = cfpath

        # open and read cffile
        f = self.read()
        if f != 0:
            print("open success")
        else:
            print("open error")


    def read( self ):
        try:
            f = open(self.path, 'r')
        except IOError:
            print('"%s" cannot be opned.', self.path)
            return 0
        
        return f


