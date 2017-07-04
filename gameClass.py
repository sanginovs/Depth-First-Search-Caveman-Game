import Tkinter

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 21:51:54 2016

Sher Sanginov 
Depth-First Search Caveman Game

"""

import copy #copy will be used when we make a copy of the location stack
from Stack import Stack #stack will be ussed to keep track of loca
import turtle
import time

SOB = 30
PATH = "assets_path.gif"
STEP = "assets_footstep.gif"
DIRECTION = "assets_Cross.gif"
TREASURE = "assets_treasure.gif"
WALL = "assets_wall.gif"
ME = "assets_me.gif"

class Cave: 
    ''' This is the cave class which creates a map 
    for the game and then haave all the oother methods for the remaining steps in the game'''
    def __init__(self):
        self.map = [] #this list will keep track of the map
        self.row = -1 #this will keep of the dimension of the row of the map
        self.col = -1 #this will keep track of the dimension of the col of the map
        self.initialrow= -1 #this will keep track of the initial row for M
        self.initialcol= -1 #this will keep track of the initial col for M
        
        self.currentrow = -1 #this will keep track of the current row that M is at
        self.currentcol = -1 #this will keep track of the current col that M is at
        
        self.location = Stack() #this strack will keep track of the positions that we moved at so that we can backtrack
        self.direction = Stack()
        
        self.path = [] #this will make a copy of self.location when we need it to output the track to a particular treasure
        
        self.move = "y" #keep track whether user wants next move or not



        ########################
        self.score=0 #this counts the number of treasure that we have


        self.alex=turtle.Turtle()       #created instance of turtle named Alex
        self.sher=turtle.Turtle()       #created new instance of turtle Sher
        self.sher.speed(0)
        self.sher.hideturtle()
        self.alex.speed(0)


        self.wn=turtle.Screen()
        self.wn.title("Maze Game")
        self.wn.bgcolor("Blue")
        self.wn.addshape(PATH)    #new .gif picture shape of path added on turtle
        self.wn.addshape(STEP)      # .gif picture of path added on turtle
        self.wn.addshape(DIRECTION) #.gif picture of direction added
        self.wn.addshape(TREASURE)  #.gif picture of treasure added
        self.wn.addshape(WALL)      #pic of wall registered
        self.wn.addshape(ME)        #picture of character added
        
        
        self.wn.setworldcoordinates(0, 0, 400, 400)     #coordinates of screen set
        self.wn.setup(width=1.0, height=1.0, startx=None, starty=None)
        self.alex.hideturtle()




   
    def find_m(self):
        '''this method looks for the position of M in the map
        after that, we update initial row, initial col and current row and current col
        pre: The map
        post: traverses the map, and look for M and the update variables accordingly'''
        for i in range(int(self.row)):
            for j in range(int(self.col)):
                if self.map[i][j] == "M":
                    self.initialrow = int(i)
                    self.initialcol = int(j)
                    self.currentrow = int(i)
                    self.currentcol = int(j)
    
    def check_m(self):
        ''' this method checks if there is an M or not
        if there is no M, then we tell use that that is not 
        pre: the variables that keep track of position of M
        post: if the variables have value -1, then M has not been found'''
        if (self.initialcol == -1) and (self.initialrow == -1): #check if current roow and col have been updated or not
            print "M not found"
                    
    def decide_next_move(self):
        '''this method checks an extreme position of M
        sometimes, M can not go North anymore, because of a wall,
        similarly, M might not be able to go west, east, and south
        no elif is used, becayse it is possible that M can not go 2 directions, (stuck in a corder)
        pre: current row and col of M
        post: check if the current col and row are at a corner'''
        if self.currentrow == 0: #check if we can not go north
            print "Can not go north anymore"

        if self.currentcol == (self.col - 1): #check if we can not go east
            print "Can not go east anymore"
            
        if self.currentrow == (self.row - 1): #check if we can not go south
            print "Can not go south anymore"
            
        if self.currentcol == 0: #check if we can not go west
            print "Can not go west anymore"
    
    def make_move(self):
        ''' this function actually makes the next move
        elif have been used so that we can prioritise North, East, South, and then West
        depensing on what move we will make, we update the current col and current row accordingly
        this function calls itself recursively after making a move
        the base case is when we have to backrack, and then, the function does not call itself anymore
        pre: current col, and current row
        post: update current col, current row, according to move made
        post: also update the stack with location moved'''
   
        if self.check_north() == True: #first check, if we can move north

            print "We move move north now"
            self.map[self.currentrow][self.currentcol] = "V"  #update the place we checked already
            self.drawShape(self.currentrow, self.currentcol, STEP)
            time.sleep(0.5)

            self.location.push([self.currentrow , self.currentcol]) #update the stack with  location 
            self.check_treasure(self.currentrow-1, self.currentcol) #checks if there is a treasure
            self.map[self.currentrow-1][self.currentcol] = "M" #updates M for that location
            self.drawShape(self.currentrow -1 , self.currentcol, ME)
            time.sleep(0.5)

            self.currentrow -= 1 #updates current row
            self.make_move() #recursion call
            
        elif self.check_east() == True: #after north, check east
           
           print "We can move east now"
           self.map[self.currentrow][self.currentcol] = "V" #update the place we checked already
           self.drawShape(self.currentrow, self.currentcol, STEP)
           time.sleep(0.5)


           self.location.push([self.currentrow , self.currentcol]) #update the stack with  location 
           self.check_treasure(self.currentrow, self.currentcol+1) #checks if there is a treasure
           self.map[self.currentrow][self.currentcol+1] = "M" #updates M for that location
           self.drawShape(self.currentrow, self.currentcol+1, ME)
           time.sleep(0.5)

           self.currentcol += 1 #updates current row
           self.make_move() #recursion call
           
        elif self.check_south() == True: #after east, check south
            
            print "We can move south now"
            self.map[self.currentrow][self.currentcol] = "V"  #update the place we checked already
            self.drawShape(self.currentrow, self.currentcol, STEP)
            time.sleep(0.5)

            self.location.push([self.currentrow , self.currentcol]) #update the stack with  location 
            self.check_treasure(self.currentrow +1 , self.currentcol) #checks if there is a treasure
            self.map[self.currentrow+1][self.currentcol] = "M"  #updates M for that location
            self.drawShape(self.currentrow+1, self.currentcol, ME)
            time.sleep(0.5)

            self.currentrow += 1#updates current row      
            self.make_move() #recursion call
            
        elif self.check_west() == True: #after south, check west
            print "We can move west now"
            self.map[self.currentrow][self.currentcol] = "V"  #update the place we checked already
            self.drawShape(self.currentrow, self.currentcol, STEP)
            time.sleep(0.5)

            self.location.push([self.currentrow , self.currentcol])  #update the stack with  location 
            self.check_treasure(self.currentrow, self.currentcol-1) #checks if there is a treasure
            self.map[self.currentrow][self.currentcol-1] = "M" #updates M for that location
            self.drawShape(self.currentrow, self.currentcol-1, ME)
            time.sleep(0.5)

            self.currentcol -= 1  #updates current col
            self.make_move() #recursion call
            
        else:  #if we could not move anywhere, then we have to backtrack!!
            print "Can not move any direction now! Because we are stuck between walls"
            self.backtrack() #calls ths backtrack function
            
    def backtrack(self):
        ''' This function checks whether it is posible to backtrack or not
        if we can backtrack, then the game is over
        pre: current row, current col, backtrack stack
        post: backtrack if we can, and then call the make_move method
        post: if we ccan not backtrack, then we say so'''
        
        print "We will now try do a backtrack because we do not have other places to go"
        
        if self.location.size() == 0: #if we can not backtrack
            #note if the size is zero, and there are places to go, then this function wuld have never been called anyway
            #this functin gets called only when there is no where to go
            print "Unfortunately there is nowhere to backtrack"
        else: #if there is a location to backtrack
            n = self.location.pop() #takes the location from the stack
            self.map[self.currentrow][self.currentcol] = "V"  #update the place we checked already
            self.drawShape(self.currentrow, self.currentcol, STEP)
            time.sleep(0.5)
            self.currentrow = n[0] #update current row
            self.currentcol = n[1] #update current col
            self.map[self.currentrow][self.currentcol] = "M"
            self.drawShape(self.currentrow, self.currentcol, ME)
            time.sleep(0.5)
            self.make_move() #calls the make_move function (indirect recursion)


    def check_north(self):
        ''' check if we can move to north or not
        pre: current row and current col
        post: check if there is no wall in north direction'''
        if self.map[self.currentrow-1][self.currentcol]  == "T" or self.map[self.currentrow-1][self.currentcol]  == ".":
            return True
            
    def check_east(self):
        ''' check if we can move to east or not
        pre: current row and current col
        post: check if there is no wall in east'''
        if self.map[self.currentrow][self.currentcol+1] == "T" or self.map[self.currentrow][self.currentcol+1] == ".":
            return True
            
    def check_south(self):
        ''' check if we can move to south or not
        pre: current current and current col\
        post: check if there is no wall in south direction'''
        if self.map[self.currentrow+1][self.currentcol] == "T" or self.map[self.currentrow+1][self.currentcol] == "."  :
            return True
            
    def check_west(self):
        ''' check if we can move to west or not
        pre: current col and current row
        post: check if there is no wall in west direction'''
        if self.map[self.currentrow][self.currentcol-1] == "T" or self.map[self.currentrow][self.currentcol-1] == ".":
            return True
    
    def check_treasure(self, r, c):
        ''' check if there is a treasure at next move or not
        pre: values of next move(row and col)
        post: check if there is a T, and updates variables accordingly'''
        if self.map[r][c] == "T":
           
            self.score+=1
            self.draw_score()   
            self.path=copy.deepcopy(self.location)
            self.path.push([r, c]) #update the stack with  location of treasure 
            print "The path from the treasure to the starting point is "
            self.treasurePath()
           
        
    def makeMap(self,filen):
        '''this methods creates the map for the game, and creates a 2d array in the process
        pre: the name of the txt file
        post: updates the row for each line in the text, and updates the row in self.map(creating a 2-d array in doing so)'''
       
        file1=open(filen) #opens the txt file
        d=file1.readline() #rread the first line to extract dimension of array
        self.row, self.col= d.split() #create dimension row and col
        self.row = int(self.row) #converting string into integer
        self.col = int(self.col)
        for i in range(int(self.row)): 
            line=[] #updating the self.map list, and making the list into an array
            r=file1.readline() #reach each line in the file
            for j in range(int(self.col)):
                line.append(r[j]) #updating values of the map

            self.map.append(line) #adding list of  rows into the list of map
    

    def sendMap(self):
        '''draws the maze map
        pre: none
        post: goes through each [row][col] index and draws the map '''
        self.alex.speed(10)
        self.wn.tracer(0)
        for i in range(self.row):
            for j in range(self.col):
                if self.map[i][j] == "W" or self.map[i][j] == "w": #if the index contains a "W", the turtle draws a wall
                    self.drawShape(i,j,WALL)
                elif self.map[i][j] == "T" or self.map[i][j] == "t": #if indicated index contains the letter "T", turtle draws a treasure
                    self.drawShape(i, j, TREASURE)
                elif self.map[i][j] == "m" or self.map[i][j] == "M":  #if indicated index contains the letter "M" turtle draws blank cell which indicates the startinf position
                    self.drawShape(i, j, ME)

                else:
                    if self.map[i][j] == "." :  #if indicated index is equal to period, turtle draws a path
                        self.drawShape(i, j, PATH)
        self.wn.update()
        self.wn.tracer(1)



    def drawShape(self, x, y, shape):
        '''draws different shapes of wall, treasure, path, character on the map
        pre: the x location, y location, and the shape to be put at that location
        post: put the shape and the specified location on the screen
        '''


        self.alex.penup()
        x = x * SOB
        y = y * SOB

        self.alex.setpos(-50 + x, 400 - y) #going to the x and y coordinate
        self.alex.shape(shape)
        self.alex.pendown()
        self.alex.stamp() #putting the shape down



    def draw_score(self):
        '''depicts the number of treasure collected once the character finds the treasure
        pre: none
        post: draws the "Treasure Collected: 0" and changes 0 according to number of treasure collected by the character
        '''


        self.sher.undo()
        self.sher.penup()
        self.sher.hideturtle()
        self.sher.setposition(-100,0) #ging to the location where we will write message
        scorestring="Treasure Collected: %s" %self.score #writing message
        self.sher.write(scorestring, False, align="center", font=("Arial",24,"normal"))


    def treasurePath(self):
        '''draws the path taken once the treasure is found
        post: uses the turtle to highlight the path taken to find a treasure'''
        x = []  # empty list to store taken paths
        bhavesh = turtle.Turtle()  # turtle instace created named Bhavesh
        bhavesh.hideturtle()
        bhavesh.speed(0)

        for p in range(self.path.size()):  # path is appended to the list
            x.append(self.path.pop())
        for shape in (DIRECTION, STEP):
            self.blinkScreen()
            bhavesh.shape(shape)
            for i in range(len(x)):
                y = x[i]
                r = y[0]
                c = y[1]

                bhavesh.penup()
                bhavesh.setpos(-50 + (r * SOB), 400 - (c * SOB))
                bhavesh.stamp()


    def blinkScreen(self):
        '''blinks the screen by changing its background to four different colors
        pre: none
        post: changes the background color quickly to red, green, orange, blue'''
        for color in ("Red", "Green", "Orange", "Blue"):
            self.wn.bgcolor(color)
            time.sleep(0.25)


















        
        
