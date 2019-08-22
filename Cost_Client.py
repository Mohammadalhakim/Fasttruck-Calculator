import socket
from sqlite3 import *
from tkinter import *
import time
import csv
import json


class Prices():
    vd_list = []


    def __init__(self):
        root.title('Fasttruck Cost Client')
        root.geometry('1350x1000')
        #root.configure(background = 'grey')
        self.frame = Frame(root, pady = 20, padx =10)
        self.frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.conn = connect('prices.db', check_same_thread= False)
        self.c = self.conn.cursor()


    def vd(self):

         self.vd_list.append([StringVar(), 'SN 500', 0.891])
         self.vd_list.append([StringVar(), 'SN 150', 0.881])
         self.vd_list.append([StringVar(), 'N 500 (GII)', 0.869])
         self.vd_list.append([StringVar(), 'N 150 (GII)', 0.8625])
         self.vd_list.append([StringVar(), 'BS 150', 0.8975])
         self.vd_list.append([StringVar(), 'est 4 (GIII)', 0.850])
         self.vd_list.append([StringVar(), 'est 6 (GIII)', 0.854])
         self.vd_list.append([StringVar(), 'LBO', 0.8725])
         self.vd_list.append([StringVar(), 'MBO', 0.8725])
         self.vd_list.append([StringVar(), 'HBO', 0.8775])
         self.vd_list.append([StringVar(), 'Virgin VI', 0.850])
         self.vd_list.append([StringVar(), 'VII (P.132)', 0.847])
         self.vd_list.append([StringVar(), 'VII (P.132 GII)', 0.850])
         self.vd_list.append([StringVar(), 'Block (VII) (GII)', 0.853])
         self.vd_list.append([StringVar(), 'MADDOC 6391', 0.999])
         self.vd_list.append([StringVar(), 'MADDOC 6585', 1.015])
         self.vd_list.append([StringVar(), 'MADDOC 6874', 0.985])
         self.vd_list.append([StringVar(), 'MADDOC 6772', 1.065])
         self.vd_list.append([StringVar(), '(TBN) MADDOC 4140', 1.215])
         self.vd_list.append([StringVar(), '(PPD) MADOC (3811)', 0.890])
         self.vd_list.append([StringVar(), 'HITEC 9890', 0.893])
         self.vd_list.append([StringVar(), '(Block) HITEC 5825H', 0.869])
         self.vd_list.append([StringVar(), 'HITEC 8712', 1.036])
         self.vd_list.append([StringVar(), 'HITEC 12204L', 0.972])
         self.vd_list.append([StringVar(), 'HITEC 12200', 0.989])
         self.vd_list.append([StringVar(), 'HITEC 521', 1.031])
         self.vd_list.append([StringVar(), 'HITEC 9325', 0.980])
         self.vd_list.append([StringVar(), 'HITEC 419', 0.92])
         self.vd_list.append([StringVar(), 'ANTIFOAM', 0.78])
         self.vd_list.append([StringVar(), 'MADDOC 4961', 0.969])
         self.vd_list.append([StringVar(), 'MADDOC 6395', 0.990])
         self.vd_list.append([StringVar(), 'MADDOC 6577', 1.035])
         self.vd_list.append([StringVar(), 'MADDOC 6211', 1.080])
         self.vd_list.append([StringVar(), 'MADDOC 6358', 0.995])
         self.vd_list.append([StringVar(), 'MADDOC 6884', 0.970])
         self.vd_list.append([StringVar(), 'MADDOC 5122', 1.087])
         self.vd_list.append([StringVar(), 'MADDOC 5252', 0.925])
         self.vd_list.append([StringVar(), 'MADDOC 5470', 1.087])
         self.vd_list.append([StringVar(), 'HITEC 523', 0.990])
         self.vd_list.append([StringVar(), 'HITEC 9305 (TBN)', 1.107])
         self.vd_list.append([StringVar(), 'HITEC 343', 1.080])


    def set_up(self):

        self.c.execute("CREATE TABLE prices (chemical TEXT, price REAL)")


        for i in range(len(self.vd_list)):
            name_input = self.vd_list[i][1]
            self.c.execute("INSERT INTO prices VALUES(?, 0.0)",(name_input,))

        self.conn.commit()

    def make_tile(self):
           self.tile_list = []
           for i in range(len(self.vd_list)):
               tile = Tile_class()
               #text
               tile.text = self.vd_list[i][1]
               #textvariable
               tile.textvariable = self.vd_list[i][0]
               #column for label and entry
               if i < 33:
                   if i%3 == 0:
                       tile.labelCol = 0
                       tile.entryCol = 1
                   elif i%3 == 1:
                       tile.labelCol = 2
                       tile.entryCol = 3
                   elif i%3 == 2:
                       tile.labelCol = 4
                       tile.entryCol = 5
                   #rows for both
                   tile.labelRow = tile.entryRow = i//3
               else:
                   if i%3 == 0:
                       tile.labelCol = 6
                       tile.entryCol = 7
                   elif i%3 == 1:
                       tile.labelCol = 8
                       tile.entryCol = 9
                   elif i%3 == 2:
                       tile.labelCol = 10
                       tile.entryCol = 11
                   # elif i%3 == 3:
                   #     tile.labelCol = 12
                   #     tile.entryCol = 13
                       tile.padx = (0,0)
                   #rows for both
                   tile.labelRow = tile.entryRow = (i//4)

               self.tile_list.append(tile)

           for tile in self.tile_list:
               Label(self.frame, text = tile.text).grid(column = tile.labelCol,
                row = tile.labelRow, sticky = tile.labelSticky)
               entry = Entry(self.frame, width = tile.width,
               textvariable = tile.textvariable)
               entry.insert(END, '0.0')
               entry.grid(column = tile.entryCol, row = tile.entryRow,
               pady = tile.pady, padx = tile.padx, sticky = tile.entrySticky)

    def connect(self):
        Label(self.frame, text = ' '*50).grid(column = 7, row = 0, columnspan = 2)
        Label(self.frame, text = 'Connection is offline.').grid(column = 7,
        row = 0, columnspan = 2)

        host = '192.168.1.118'
        #host = '10.0.0.29'
        port = 5000
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, port))

        Label(self.frame, text = ' '*50).grid(column = 7, row = 0, columnspan = 2)
        Label(self.frame, text = 'Connection is online.', fg = 'green').grid(column = 7, row = 0, columnspan = 2)

        print('Connected!')

    def connect_button(self):
        Label(self.frame, text = 'Connection is offline.').grid(column = 7, row = 0, columnspan = 2)
        self.okay = Button(self.frame, text='Connect to Host', command = cal.connect)
        self.okay.grid(column = 9, row = 5)

    def load_button(self):

        reset = Button(self.frame, text='Load', command = cal.load)
        reset.grid(column = 9, row =  6 )

    def load(self):

        self.c.execute("""SELECT * FROM prices""")
        message  = self.c.fetchall()
        self.conn.commit()

        i = 0
        for tile in self.tile_list:
            entry = Entry(self.frame, width = tile.width, textvariable = tile.textvariable)
            entry.delete(0, END)
            entry.insert(END, message[i][1])
            entry.grid(column = tile.entryCol, row = tile.entryRow, pady = tile.pady, padx = tile.padx, sticky = tile.entrySticky)
            i += 1



    def send(self):


        Label(self.frame, text = 'Data was not sent.').grid(column = 7, row = 2)

        for i in range(len(self.vd_list)):
            chem_name = self.vd_list[i][1]
            data_input = float(self.vd_list[i][0].get())
            self.c.execute("UPDATE prices SET price = ? WHERE chemical = ?", (data_input, chem_name,))
        self.conn.commit()

        self.c.execute("""SELECT * FROM prices""")
        message  = self.c.fetchall()
        self.conn.commit()

         # data = r"{ "
         # #print(len(self.vd_list))
         # for i in range(len(self.vd_list)):
         #     #print(data + '\n\n')
         #     volume = str(float((self.vd_list[i][0].get())/1000)*self.vd_list[i][2])
         #     data = data + "\"" + self.vd_list[i][1] + "\"" + ':' + volume + ', '
         # data = data[:-2]
         # data += '}'
         #
         # print(data + '\n\n')
         #
         # message = '1' + data
         #
         # info = json.loads(data)

        message = '1' + str(message)



        self.s.send(message.encode())

        Label(self.frame, text = ' ' * 50).grid(column = 7
        , row = 2)

        Label(self.frame, text = 'Sent!').grid(column = 7
        , row = 2)





    def send_button(self):
        self.okay = Button(self.frame, text='Send', command = cal.send)
        self.okay.grid(column = 7, row = 5)


class Tile_class:
     text = ''
     labelCol = 0
     labelRow = 0
     labelSticky  = E
     entrySticky = W
     width = 10
     textvariable = None
     entryCol = 1
     entryRow = 0
     padx = (0, 20)
     pady = (20,20)

root = Tk()
cal = Prices()
cal.vd()
cal.make_tile()
cal.load_button()
cal.connect_button()
#cal.set_up()
cal.send_button()
root.mainloop()
