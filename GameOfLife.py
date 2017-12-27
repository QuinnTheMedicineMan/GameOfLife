#!/usr/bin/env python
import curses, random, time, sys, argparse
import numpy as np

class Screen:

  def __init__(self, (ymax, xmax), nCells):
    self.coords = np.zeros((xmax, ymax), dtype=str)
    self.xmax   = xmax
    self.ymax   = ymax
    self.nCells = nCells


  def update(self):

    new_coords   = np.zeros((self.xmax, self.ymax), dtype=str)

    for (x, y), element in np.ndenumerate(self.coords):

      ## Calculate number of living neighbours ##
      living_neighbours = 0

      xmin = x-1
      xmax = x+2
      ymin = y-1
      ymax = y+2

      if x == 0:
        xmin = 0
      if y == 0:
        ymin = 0

      if x == self.xmax - 1:
        xmax = x
      if y == self.ymax - 1:
        ymax = y

      for i in range(xmin, xmax):
        for j in range(ymin, ymax):
          if self.coords[i,j] != '':
            living_neighbours += 1

      if self.coords[x,y] != '':
        living_neighbours -= 1
      ## Calculation done, accounting for the edges of the board ##

      if element != '':
        if living_neighbours < 2 or living_neighbours > 3: # Rules 1 & 3, if a cell has fewer than two or greater than 3 neighbours, it dies
          new_coords[x][y] = ''
        else:
          new_coords[x][y] = 'X'                           # Else it survives
      elif living_neighbours == 3:
          new_coords[x][y] = 'X'                           # An empty cell with 3 neighbours comes to life

    self.coords = new_coords


  def setup_random(self):                                  # Fill a random set of cells to get the starting configuration of the board
    for N in range(self.nCells):
      randx  = random.randint(0, self.xmax - 1)
      randy  = random.randint(0, self.ymax - 1)
      self.coords[randx][randy] = 'X'


  def setup_blinker(self):                                 # Create a blinker
    self.coords[10, 10] = 'X'
    self.coords[10, 11] = 'X'
    self.coords[10, 12] = 'X'


  def setup_pentadecathlon(self):                          # Create a pentadecathlon
    self.coords[ 7,  9] = 'X'
    self.coords[ 8,  9] = 'X'
    self.coords[ 9,  9] = 'X'
    self.coords[10,  9] = 'X'
    self.coords[11,  9] = 'X'
    self.coords[12,  9] = 'X'
    self.coords[13,  9] = 'X'
    self.coords[14,  9] = 'X'
    self.coords[ 7, 10] = 'X'
    self.coords[ 9, 10] = 'X'
    self.coords[10, 10] = 'X'
    self.coords[11, 10] = 'X'
    self.coords[12, 10] = 'X'
    self.coords[14, 10] = 'X'
    self.coords[ 7, 11] = 'X'
    self.coords[ 8, 11] = 'X'
    self.coords[ 9, 11] = 'X'
    self.coords[10, 11] = 'X'
    self.coords[11, 11] = 'X'
    self.coords[12, 11] = 'X'
    self.coords[13, 11] = 'X'
    self.coords[14, 11] = 'X'


  def setup_pulsar(self):                                  # Create a pulsar
    self.coords[ 5,  8] = 'X'
    self.coords[ 5,  9] = 'X'
    self.coords[ 5, 10] = 'X'
    self.coords[ 5, 14] = 'X'
    self.coords[ 5, 15] = 'X'
    self.coords[ 5, 16] = 'X'
    self.coords[ 7,  6] = 'X'
    self.coords[ 7, 11] = 'X'
    self.coords[ 7, 13] = 'X'
    self.coords[ 7, 18] = 'X'
    self.coords[ 8,  6] = 'X'
    self.coords[ 8, 11] = 'X'
    self.coords[ 8, 13] = 'X'
    self.coords[ 8, 18] = 'X'
    self.coords[ 9,  6] = 'X'
    self.coords[ 9, 11] = 'X'
    self.coords[ 9, 13] = 'X'
    self.coords[ 9, 18] = 'X'
    self.coords[10,  8] = 'X'
    self.coords[10,  9] = 'X'
    self.coords[10, 10] = 'X'
    self.coords[10, 14] = 'X'
    self.coords[10, 15] = 'X'
    self.coords[10, 16] = 'X'

    self.coords[12,  8] = 'X'
    self.coords[12,  9] = 'X'
    self.coords[12, 10] = 'X'
    self.coords[12, 14] = 'X'
    self.coords[12, 15] = 'X'
    self.coords[12, 16] = 'X'
    self.coords[13,  6] = 'X'
    self.coords[13, 11] = 'X'
    self.coords[13, 13] = 'X'
    self.coords[13, 18] = 'X'
    self.coords[14,  6] = 'X'
    self.coords[14, 11] = 'X'
    self.coords[14, 13] = 'X'
    self.coords[14, 18] = 'X'
    self.coords[15,  6] = 'X'
    self.coords[15, 11] = 'X'
    self.coords[15, 13] = 'X'
    self.coords[15, 18] = 'X'
    self.coords[17,  8] = 'X'
    self.coords[17,  9] = 'X'
    self.coords[17, 10] = 'X'
    self.coords[17, 14] = 'X'
    self.coords[17, 15] = 'X'
    self.coords[17, 16] = 'X'


  def setup_toad(self):                                  # Create a toad
    self.coords[12, 12] = 'X'
    self.coords[12, 13] = 'X'
    self.coords[12, 14] = 'X'
    self.coords[13, 11] = 'X'
    self.coords[13, 12] = 'X'
    self.coords[13, 13] = 'X'


  def setup_beacon(self):                                # Create a beacon
    self.coords[11, 11] = 'X'
    self.coords[12, 11] = 'X'
    self.coords[11, 12] = 'X'
    self.coords[14, 13] = 'X'
    self.coords[13, 14] = 'X'
    self.coords[14, 14] = 'X'

  functions = {"random"         : setup_random,         # Dictionary of functions for command line access
               "blinker"        : setup_blinker,
               "pentadecathlon" : setup_pentadecathlon,
               "pulsar"         : setup_pulsar,
               "toad"           : setup_toad,
               "beacon"         : setup_beacon}

def wrapper_function(stdscr, func, nCells):

  random.seed(time.time())

  stdscr.clear()
  stdscr.refresh()

  myscreen = Screen(stdscr.getmaxyx(), nCells)  # My screen/game board class

  if func not in myscreen.functions.keys():     # Check the function specified in the command line was valid
    print "Invalid function {0}.".format(func)
    print "Valid options are:"
    print myscreen.functions.keys()
    exit(1)

  if nCells < 0:
    print "Ah, I see you're a QA engineer."
    exit(1)
  elif nCells > (myscreen.xmax*myscreen.ymax):
    print "nCells is too high. It must be less than {0}.".format(myscreen.xmax*myscreen.ymax)
    exit(1)

  setup_function = myscreen.functions[func]     # Use a dictionary to get the right starting conditions
  setup_function(myscreen)

  for (x, y), element in np.ndenumerate(myscreen.coords):
    stdscr.addstr(y, x, element)

  k = stdscr.getch()

  while True:

    myscreen.update()

    stdscr.clear()
    stdscr.refresh()
    for (x, y), element in np.ndenumerate(myscreen.coords):
      stdscr.addstr(y, x, element)

    k = stdscr.getch()


def main(argv=sys.argv):

  zap = argparse.ArgumentParser()
  zap.add_argument("--function", "-f", type=str)
  zap.add_argument("--nCells",   "-n", type=int, default=1000)

  try:
    args = zap.parse_args()
  except:
    exit(1)

  curses.wrapper(wrapper_function, args.function, args.nCells)

if __name__ == "__main__":
  main()
