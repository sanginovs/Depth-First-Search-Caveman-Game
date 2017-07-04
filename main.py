#Depth-First Search Caveman Game
#Author: Sher Sanginov



from gameClass import Cave


def main():

   print "Welcome to the cave game. In this game, you will enter the name of a txt file, which the computer will read. \n The person in your file will go around the map to collect all possible treasures. \n You only need to provide a txt file which has a map."
   try:
      filen=int(raw_input("Which map you want to choose?\nPress 1 for Map1: \nPress 2 for Map2: \nPress 3 for Map3:"))

      if filen==1:
         filen="sample_input_map.txt"
      elif filen==2:
         filen="sample_input_map1.txt"
      else:
         filen="sample_input_map2.txt"
   except:
      print "You can only enter numbers."



   game = Cave() #creates an instance of the cave class for the game
   game.makeMap(filen) #creates the map
   game.sendMap()
   game.find_m() #look for m
   game.check_m() #check if we found m or not
   game.decide_next_move() #decide where to move next if we found m
   game.make_move() #make the next move


   #wn.exitonclick()  #

main()
