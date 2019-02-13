
# coding: utf-8

# In[6]:


# %load q3.py


# In[ ]:


import string
import random

def start(gridsize,start,numberofmines):
    grid = [['0' for i in range(gridsize)] for i in range(gridsize)]
    gridsize = len(grid)
    mines = []
    for i in range(numberofmines):
        gridsize = len(grid)
        a = random.randint(0,gridsize-1)
        b = random.randint(0,gridsize-1)
        cell = (a,b)
        while cell==(start[0],start[1]) or cell in mines:
            gridsize = len(grid)
            a = random.randint(0,gridsize-1)
            b = random.randint(0,gridsize-1)
            cell = (a,b)
        else: mines.append(cell)

    for i,j in mines: grid[i][j] = 'X'
    gridsize = len(grid)
    for rowno,row in enumerate(grid):
        for colno,col in enumerate(row):
            if col!='X':
                values = [grid[r][c] for r,c in adjacent(grid,rowno,colno)]
                grid[rowno][colno] = str(values.count('X'))
    return (grid,mines)

def layout(grid):
    gridsize = len(grid)
    horizontal = '   '+4*gridsize*'-'+'-'
    toplabel = '     '
    for i in string.ascii_lowercase[:gridsize]:
        toplabel = toplabel+i+'   '
    print '\n'+toplabel+'\n'+horizontal
    for idx,i in enumerate(grid):
        row = '{0:2} |'.format(idx+1)
        for j in i:
            row = row+' '+j+' |'
        print row+'\n'+horizontal
    print ''


def adjacent(grid,rowno,colno):
    gridsize = len(grid)
    row = grid[rowno]
    column = grid[rowno][colno]

    neighbors = []

    for i in range(-1,2):
        for j in range(-1,2):
            if i == 0 and j == 0: continue
            elif -1<rowno+i<gridsize and -1<colno+j<gridsize:
                neighbors.append((rowno+i,colno+j))
    return neighbors

def out_mine(grid,start,numberofmines):
    gridsize = len(grid)
    mines = []
    for i in range(numberofmines):
        gridsize = len(grid)
        a = random.randint(0,gridsize-1)
        b = random.randint(0,gridsize-1)
        cell = (a,b)
        while cell==(start[0],start[1]) or cell in mines:
            gridsize = len(grid)
            a = random.randint(0,gridsize-1)
            b = random.randint(0,gridsize-1)
            cell = (a,b)
        else: mines.append(cell)

    for i,j in mines: grid[i][j] = 'X'
    return mines

def multiple(grid,currgrid,rowno,colno,checked=[]):
    gridsize = len(grid)
    neighbors = adjacent(grid,rowno,colno)
    for r,c in neighbors:
        if (r,c) not in checked:
            checked.append((r,c))
            if grid[r][c] != 'X' and currgrid[r][c] != 'F':
                currgrid[r][c] = grid[r][c]

            if grid[r][c] == '0':
                multiple(grid,currgrid,r,c)


def play(choice0,choice1):
    numberofmines= int (choice0)
    gridsize =int (choice1)

    currgrid = [[' ' for i in range(gridsize)] for i in range(gridsize)]
    layout(currgrid)
    grid = []
    flags = []
    while True:
        while True:
            lastcell = str(raw_input('Enter the cell: '))
            print ''
            flag = False
            try:
                if lastcell[2] == 'f': flag = True
            except IndexError: pass

            try:
                lastcell = (int(lastcell[1])-1,string.ascii_lowercase.index(lastcell[0]))
                break
            except (IndexError,ValueError):
                print "Invalid cell\n\n"

        if len(grid)==0:
            grid,mines = start(gridsize,lastcell,numberofmines)
        rowno,colno = lastcell

        if flag:
            if currgrid[rowno][colno]==' ':
                currgrid[rowno][colno] = 'F'
                flags.append((rowno,colno))
            elif currgrid[rowno][colno]=='F':
                currgrid[rowno][colno] = ' '
                flags.remove((rowno,colno))
            else: print 'Cannot put a flag there'

        else:
            if (rowno,colno) in flags:
                flags.remove((rowno,colno))
            currgrid[rowno][colno] = grid[rowno][colno]

            if grid[rowno][colno] == 'X':
                layout(grid)
                print 'Game Over'
                break
            elif grid[rowno][colno] == '0':
                multiple(grid,currgrid,rowno,colno)

        layout(currgrid)
        if set(flags)==set(mines):
            print 'You Win'

choice0 = raw_input('Enter number of mines: ')
choice1 = raw_input('Enter grid size: ')
                
play(choice0,choice1)


