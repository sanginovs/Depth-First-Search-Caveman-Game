# Project Title

Depth-First Search Caveman

## Description

Depth-First Search Caveman is a game in which a caveman automatically goes around the cave to look for
a treasure. There are several treasures that are located in different coordinates on the map. That's why,
caveman walks around looking for a treasure. If the caveman gets stuck, he starts to backtrack until he finds a direction
which is open for him to go, otherwise he keeps backtracking.

## Motivation

I was motivated to work on this project after learning about different data structures like stacks, queues and
design and algorithm concepts like Depth-First Search and Breadth-First search. Thus, I decided to make
a game that uses Depth-First search, stacks, queues, 2D arrays in its implementation in order to show the use of
data structures and algorithmic concepts in the real world.

## File descriptions

* [main.py](main.py) - this is the file that runs the program
* [gameClass.py](gameClass.py) - all the implementation of the Caveman game is located in this file as a Cave class.
* [Stack.py](Stack.py) - this file contains an impelemention of stack in Python which is used in the game. Stack is a common LIFO(for last in, first out) data structure.
* [setup.sh](setup.sh) - installs all the dependencies to get started with the development environment
* You can ignore other files with .gif or .txt extensions since they are used by [gameClass.py](gameClass.py) and [main.py](main.py) files.
* Files with .txt extensions (sample_input_map.txt) are used as a user input since they are the actual
maps that are used in the game. Here's a simple input map:

```
4 12
WWWWWWWWWWWW
WWW...WWW.WW
WW.....WW.WW
WW.W.WWW...W
```

In the example above, 4 is a number of rows while 12 is a number of columns in the map. "W" means walls
and "."(dot) means open path. This type of input allowed me to use 2-D arrays in the implementation
of my game as the cave map.
* Files with .gif extension (assets_wall.gif) are gif images that are used by Tkinter library for graphical purposes.





## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Prerequisites

What things you need to install the software and how to install them

```
a)It is necessary to have Python2.7 or Python3.5 installed on your local machine.
b)Python Tkinter library is required
```

### Installing

You can simply run the [setup.sh](setup.sh) file which installs all the dependecies for you.

Or

Install it without running the setup file:

a) Installing Python 2.7
```
Download Python2.7 from Python website: https://www.python.org/downloads/
```

b) Install Tkinter Library

```
You can install Tkinter by simply typing this command in the terminal(linux):
sudo apt-get install python-tk
```


## Running the program

In order to run the program, you just need to run [main.py](main.py) file. You can run it from your IDE or terminal.
Make sure you are inside this directory. In the terminal, type:
python [main.py](main.py)

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```


## Built With

* [Python](https://www.python.org/) - The programming language
* [Tkinter](https://docs.python.org/2/library/tkinter.html) - Python Graphical User Interface Library


## Authors

* **Sher Sanginov**



## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* **StackOverflow**

