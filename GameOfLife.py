#!/usr/bin/env python
import curses, random, time
import numpy as np

def getNLivingNeighbours((X,Y), screen):
  output = 0

  xmin = X-1
  xmax = X+2
  ymin = Y-1
  ymax = Y+2

  if X == 0:
    xmin = 0
  if Y == 0:
    ymin = 0

  if X == screen.xmax - 1:
    xmax = X
  if Y == screen.ymax - 1:
    ymax = Y

  for x in range(xmin, xmax):
    for y in range(ymin, ymax):
      if screen.coords[x,y] != '':
        output += 1

  if screen.coords[X,Y] != '':
    output -= 1

  return output


class Screen:

  def __init__(self, (ymax, xmax), nCells):
    self.coords = np.zeros((xmax, ymax), dtype=str)
    self.nCells = nCells
    self.xmax   = xmax
    self.ymax   = ymax

  def update(self):

    new_coords   = np.zeros((self.xmax, self.ymax), dtype=str)

    for (x, y), element in np.ndenumerate(self.coords):

      ## Calculate number of living neighbours ##
      #living_neighbours = getNLivingNeighbours((x,y), self)
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
          new_coords[x][y] = 'X'
      elif living_neighbours == 3:
          new_coords[x][y] = 'X'

    self.coords = new_coords

  def setup_random(self):
    for N in range(self.nCells):
      randx  = random.randint(0, self.xmax - 1)
      randy  = random.randint(0, self.ymax - 1)
      self.coords[randx][randy] = 'X'

  def setup_blinker(self):
    self.coords[10, 10] = 'X'
    self.coords[10, 11] = 'X'
    self.coords[10, 12] = 'X'

  def setup_pentadecathlon(self):
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

  def setup_pulsar(self):
    self.coords[12,  0] = 'X'
    self.coords[13,  0] = 'X'
    self.coords[19,  0] = 'X'
    self.coords[20,  0] = 'X'
    self.coords[13,  1] = 'X'
    self.coords[14,  1] = 'X'
    self.coords[18,  1] = 'X'
    self.coords[19,  1] = 'X'
    self.coords[10,  2] = 'X'
    self.coords[13,  2] = 'X'
    self.coords[15,  2] = 'X'
    self.coords[17,  2] = 'X'
    self.coords[19,  2] = 'X'
    self.coords[22,  2] = 'X'
    self.coords[10,  3] = 'X'
    self.coords[11,  3] = 'X'
    self.coords[12,  3] = 'X'
    self.coords[14,  3] = 'X'
    self.coords[15,  3] = 'X'
    self.coords[17,  3] = 'X'
    self.coords[18,  3] = 'X'
    self.coords[20,  3] = 'X'
    self.coords[21,  3] = 'X'
    self.coords[22,  3] = 'X'
    self.coords[11,  4] = 'X'
    self.coords[13,  4] = 'X'
    self.coords[15,  4] = 'X'
    self.coords[17,  4] = 'X'
    self.coords[19,  4] = 'X'
    self.coords[21,  4] = 'X'
    self.coords[12,  5] = 'X'
    self.coords[13,  5] = 'X'
    self.coords[14,  5] = 'X'
    self.coords[18,  5] = 'X'
    self.coords[19,  5] = 'X'
    self.coords[20,  5] = 'X'

    self.coords[12,  7] = 'X'
    self.coords[13,  7] = 'X'
    self.coords[14,  7] = 'X'
    self.coords[18,  7] = 'X'
    self.coords[19,  7] = 'X'
    self.coords[20,  7] = 'X'
    self.coords[11,  8] = 'X'
    self.coords[13,  8] = 'X'
    self.coords[15,  8] = 'X'
    self.coords[17,  8] = 'X'
    self.coords[19,  8] = 'X'
    self.coords[21,  8] = 'X'
    self.coords[10,  9] = 'X'
    self.coords[11,  9] = 'X'
    self.coords[12,  9] = 'X'
    self.coords[14,  9] = 'X'
    self.coords[15,  9] = 'X'
    self.coords[17,  9] = 'X'
    self.coords[18,  9] = 'X'
    self.coords[20,  9] = 'X'
    self.coords[21,  9] = 'X'
    self.coords[22,  9] = 'X'
    self.coords[10, 10] = 'X'
    self.coords[13, 10] = 'X'
    self.coords[15, 10] = 'X'
    self.coords[17, 10] = 'X'
    self.coords[19, 10] = 'X'
    self.coords[22, 10] = 'X'
    self.coords[13, 11] = 'X'
    self.coords[14, 11] = 'X'
    self.coords[18, 11] = 'X'
    self.coords[19, 11] = 'X'
    self.coords[12, 12] = 'X'
    self.coords[13, 12] = 'X'
    self.coords[19, 12] = 'X'
    self.coords[20, 12] = 'X'

  def setup_toad(self):
    self.coords[12, 12] = 'X'
    self.coords[12, 13] = 'X'
    self.coords[12, 14] = 'X'
    self.coords[13, 11] = 'X'
    self.coords[13, 12] = 'X'
    self.coords[13, 13] = 'X'

  def setup_beacon(self):
    self.coords[11, 11] = 'X'
    self.coords[12, 11] = 'X'
    self.coords[11, 12] = 'X'
    self.coords[14, 13] = 'X'
    self.coords[13, 14] = 'X'
    self.coords[14, 14] = 'X'


def test(stdscr, nCells):

  random.seed(time.time())

  stdscr.clear()
  stdscr.refresh()

  myscreen = Screen(stdscr.getmaxyx(), nCells)
  #myscreen.setup_blinker()
  #myscreen.setup_random()
  #myscreen.setup_pulsar()
  #myscreen.setup_toad()
  #myscreen.setup_beacon()
  myscreen.setup_pentadecathlon()

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

def main():
  curses.wrapper(test, 1000)

if __name__ == "__main__":
  main()
