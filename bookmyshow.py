#import numpy as np
#import pandas as pd
class Bookmy_Tickets:
    print('Welcome to StarkCinemas')

    def __init__(self):
        self.display()
        #self.name = "MY name is vishal gupta"

    def display(self):
        print('******************************************')
        print('PLEASE ENTER YOUR CHOICE : ')
        print('******************************************')
        print('1. Show the screens')
        print('2. Buy a Tickets')
        print('3. Statistics')
        print('4. Show booked Tickets User Info')
        print('5. Exit')
        choice = int(input('Enter your choice'))
        if choice == 0:
            exit()
        if choice == 1:
            print('Called')
            self.show_screens()
            #Bookmy_Tickets.show_screens()

    #@classmethod
    def show_screens(self):

        print('Type of screen you want enjoy watching movie')
        print('1 . IMAX 4K Dual Digital Projecter')
        print('2 . Min_screen with Stellar Surround Sound')

        choice=int(input('Enter your screen Type you want'))

        if choice == 1:
            print("Total Seats in Imax_screen:")
            self.row = 6
            self.col = 6
            self.details = {}
            self.matrix = []
            self.pricing = {}
            for i in range(self.row):
                a = []
                for j in range(self.col):
                    a.append("S")

                self.matrix.append(a)
            print(end="  ")
            for j in range(self.col):
                print(j + 1, end=" ")
            print()
            for i in range(self.row):
                print(i + 1, end=" ")
                for j in range(6):
                    print(self.matrix[i][j], end=" ")
                print()

        buy = input('To Procced with Booking Tickets Press "Yes" or "No" ')
        if buy in ['Yes', 'yes', 'YES']:
            self.Buy_tickets()
            #Bookmy_Tickets.Buy_tickets()
        elif buy in ['No', 'NO', 'no']:
            self.display()
            #Bookmy_Tickets.display()
            # arr = np.array(self.matrix)
            # df = pd.DataFrame(arr)
            # df.iloc[2, 3] = 'b'
            # print(df)


        elif choice == 2:

            print("Total Seats in MinScreen :")
            self.row = 8
            self.col = 8
            self.details = {}
            self.matrix = []

            self.pricing = {}
            for i in range(self.row):
                a = []
                for j in range(self.col):
                    a.append("S")

                self.matrix.append(a)
            print(end="  ")
            for j in range(self.col):
                print(j + 1, end=" ")
            print()
            for i in range(self.row):
                print(i + 1, end=" ")
                for j in range(8):
                    print(self.matrix[i][j], end=" ")
                print()
            # arr = np.array(self.matrix)
            #
            # # print(arr)
            #
            # df = pd.DataFrame(arr)
            # df.iloc[2,3] = 'b'
            # print(df)

        # print('To Procced with Booking Tickets Press "Yes" or "No" ')
        buy=input('To Procced with Booking Tickets Press "Yes" or "No" ')
        if buy in ['Yes' , 'yes' , 'YES']:
            self.Buy_tickets()
#            #Bookmy_Tickets.Buy_tickets()

        if buy in ['No' , 'NO' , 'no']:
            self.Buy_tickets()
            #Bookmy_Tickets.display()

    #@classmethod
    def Buy_tickets(self):
        print("Enter Row and Column Number for your desired Place")
        #arr = np.array(self.matrix)
        #df = pd.DataFrame(arr)
        #df.iloc[2,3] = 'b'
        #print(df)
        print("buyticket is called")



movie = Bookmy_Tickets()
movie.Buy_tickets()
