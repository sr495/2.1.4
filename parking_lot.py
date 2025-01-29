vexcode_brain_precision = 0
vexcode_console_precision = 0
row = 0
col = 0
openSpots = 0
ParkingLot = [[0 for y in range(10)] for x in range(5)]


def when_started1():
   global row, col, openSpots, ParkingLot, vexcode_brain_precision, vexcode_console_precision
   row = 1
   col = 1
   openSpots = 0
   ParkingLot = [
       [0, 0, 0, 0, 0],
       [0, 2, 1, 1, 2],
       [0, 1, 1, 2, 1],
       [0, 0, 0, 0, 0],
       [0, 1, 2, 2, 1]
   ]
   while row < 6:
       col = 1
       while col < 6:
           if ParkingLot[row - 1][col - 1] == 2:
               openSpots = openSpots + 1
           else:
               openSpots = openSpots + 0
           col = col + 1
           wait(5, MSEC)
       brain.screen.next_row()
       row = row + 1
       wait(5, MSEC)
   brain.screen.print(openSpots, precision=6 if vexcode_brain_precision is None else vexcode_brain_precision)


when_started1()
