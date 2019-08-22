import socket
import threading
from sqlite3 import *
import os
import json
import ast

class server():

    '''
There are two conns. One conn is for connecting to clients and other conn is
for connecting to data base.
    '''
    vd_list = []

    def __init__(self):
        host = ''
        port = 5000

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.s.bind((host, port))

        self.s.listen(5)

        print('\n\n----------------------------------------------- Welcome to FCalc Server -----------------------------------------------\n\n\n\n Waiting for connections...\n\n')

        self.conn = connect('prices.db', check_same_thread= False)

        self.c = self.conn.cursor()



    def vd(self):

         self.vd_list.append(['SN 500', 0.891, 0.00])
         self.vd_list.append(['SN 150', 0.881, 0.00 ])
         self.vd_list.append(['N 500 (GII)', 0.869, 0.00 ])
         self.vd_list.append(['N 150 (GII)', 0.8625, 0.00 ])
         self.vd_list.append(['BS 150', 0.8975, 0.0 ])
         self.vd_list.append(['est 4 (GIII)', 0.850, 0.0 ])
         self.vd_list.append(['est 6 (GIII)', 0.854, 0.0 ])
         self.vd_list.append(['LBO', 0.8725, 0.0])
         self.vd_list.append(['MBO', 0.8725, 0.0])
         self.vd_list.append(['HBO', 0.8775, 0.0 ])
         self.vd_list.append(['Virgin VI', 0.850, 0.0])
         self.vd_list.append(['VII (P.132)', 0.847, 0.0 ])
         self.vd_list.append(['VII (P.132 GII)', 0.850, 0.0 ])
         self.vd_list.append(['Block (VII) (GII)', 0.853, 0.0 ])
         self.vd_list.append(['MADDOC 6391', 0.999, 0.0 ])
         self.vd_list.append(['MADDOC 6585', 1.015, 0.0 ])
         self.vd_list.append(['MADDOC 6874', 0.985, 0.0 ])
         self.vd_list.append(['MADDOC 6772', 1.065, 0.0])
         self.vd_list.append(['(TBN) MADDOC 4140', 1.215, 0.0 ])
         self.vd_list.append(['(PPD) MADOC (3811)', 0.890, 0.0 ])
         self.vd_list.append(['HITEC 9890', 0.893, 0.0 ])
         self.vd_list.append(['(Block) HITEC 5825H', 0.869, 0.0 ])
         self.vd_list.append(['HITEC 8712', 1.036, 0.0 ])
         self.vd_list.append(['HITEC 12204L', 0.972, 0.0 ])
         self.vd_list.append(['HITEC 12200', 0.989, 0.0 ])
         self.vd_list.append(['HITEC 521', 1.031, 0.0])
         self.vd_list.append(['HITEC 9325', 0.980, 0.0 ])
         self.vd_list.append(['HITEC 419', 0.92, 0.0 ])
         self.vd_list.append(['ANTIFOAM', 0.78, 0.0 ])
         self.vd_list.append(['MADDOC 4961', 0.969, 0.0 ])
         self.vd_list.append(['MADDOC 6395', 0.990, 0.0 ])
         self.vd_list.append(['MADDOC 6577', 1.035, 0.0 ])
         self.vd_list.append(['MADDOC 6211', 1.080, 0.0 ])
         self.vd_list.append(['MADDOC 6358', 0.995, 0.0 ])
         self.vd_list.append(['MADDOC 6884', 0.970, 0.0 ])
         self.vd_list.append(['MADDOC 5122', 1.087, 0.0 ])
         self.vd_list.append(['MADDOC 5252', 0.925, 0.0 ])
         self.vd_list.append(['MADDOC 5470', 1.087, 0.0 ])
         self.vd_list.append(['HITEC 523', 0.990, 0.0 ])
         self.vd_list.append(['HITEC 9305 (TBN)', 1.107, 0.0])
         self.vd_list.append(['HITEC 343', 1.080, 0.0 ])

    def set_up(self):

        self.c.execute("CREATE TABLE prices (chemical TEXT, price REAL)")


        for i in range(len(self.vd_list)):
            name_input = self.vd_list[i][0]
            self.c.execute("INSERT INTO prices VALUES(?, 0.0)",(name_input,))

        self.conn.commit()



    def connect(self):
        while True:
            conn, addr  = self.s.accept()
            print('Connected with ' + addr[0] + ': ' + str(addr[1]) + '\n\n')
            threading.Thread(target = serv.get_data, args = (conn, self.c, self.conn, )).start()


    def get_data(self, conn, c, conn1):



        #.close() ruins everything. Don't use it for both server and client.

        while True:
            number = conn.recv(1024)

            if number.decode() != '': # this recv is not 'blocked' like s.accept() so in fact it is constantly receiving an empty String.
                data = ''
                if int(number.decode()[0]) == 1:
                    data = ast.literal_eval(number.decode()[1:])
                    for i in range(len(self.vd_list)):
                        chem_name = data[i][0]
                        data_input = round((data[i][1]/1000)*self.vd_list[i][1], 4)
                        c.execute("UPDATE prices SET price = ? WHERE chemical = ?", (data_input, chem_name,))
                    conn1.commit()

                    print(data)
                    print('\n\n')

                else:
                    c.execute("""SELECT * FROM prices""")
                    message  = c.fetchall()
                    conn1.commit()
                    conn.send(str(message).encode())




serv = server()
serv.vd()
#serv.set_up()
serv.connect()
