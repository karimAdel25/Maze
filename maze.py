# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 15:51:01 2022

@author: mohamed
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 15:19:21 2022

@author: mohamed
"""

from pyamaze2 import maze,agent,COLOR,textLabel
from tkinter import *
from timeit import timeit
from queue import PriorityQueue

def h(cell1,cell2):
    x1,y1=cell1
    x2,y2=cell2

    return abs(x1-x2) + abs(y1-y2)
def aStar(m):
    start=(m.rows,m.cols)
    g_score={cell:float('inf') for cell in m.grid}
    g_score[start]=0
    f_score={cell:float('inf') for cell in m.grid}
    f_score[start]=h(start,(1,1))

    open=PriorityQueue()
    open.put((h(start,(1,1)),h(start,(1,1)),start))
    aPath={}
    while not open.empty():
        currCell=open.get()[2]
        if currCell==(1,1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                if d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                if d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if d=='S':
                    childCell=(currCell[0]+1,currCell[1])

                temp_g_score=g_score[currCell]+1
                temp_f_score=temp_g_score+h(childCell,(1,1))

                if temp_f_score < f_score[childCell]:
                    g_score[childCell]= temp_g_score
                    f_score[childCell]= temp_f_score
                    open.put((temp_f_score,h(childCell,(1,1)),childCell))
                    aPath[childCell]=currCell
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[aPath[cell]]=cell
        cell=aPath[cell]
    return fwdPath

def BFS(m):
    start=(m.rows,m.cols)
    frontier=[start]
    explored=[start]
    bfsPath={}
    while len(frontier)>0:
        currCell=frontier.pop(0)
        if currCell==(1,1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell]=currCell
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return fwdPath
def DFS(m):
    start=(m.rows,m.cols)
    explored=[start]
    frontier=[start]
    dfsPath={}
    while len(frontier)>0:
        currCell=frontier.pop()
        if currCell==(1,1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in explored:
                    continue
                explored.append(childCell)
                frontier.append(childCell)
                dfsPath[childCell]=currCell
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[dfsPath[cell]]=cell
        cell=dfsPath[cell]
    return fwdPath

def BFS_Button():
    m.tracePath({a:path})
    textLabel(m,'BFS Time',t2)
    l=textLabel(m,'BFS Cost',len(path)+1)
def DFS_Button():
    m.tracePath({b:path2})
    textLabel(m,'DFS Time',t1)
    l=textLabel(m,'DFS Cost',len(path2)+1)
def aStar_Button():
    m.tracePath({d:path3})
    textLabel(m,'aStar Time',t3)
    l=textLabel(m,'aStar Cost',len(path3)+1)    
      

          
if __name__=='__main__':
    m=maze(9,20)
    m.CreateMaze(loopPercent=20)
    path=BFS(m)
    path2=DFS(m)
    path3=aStar(m)
   

    a=agent(m,footprints=True,filled=True)
    b=agent(m,footprints=True,filled=True,shape="arrow",color="green")
    c=agent(m,footprints=True,filled=True,color="red")
    d=agent(m,footprints=True,filled=True,shape="arrow",color="yellow")

    m.enableArrowKey(c)
    t1=timeit(stmt='DFS(m)',number=1000,globals=globals())
    t2=timeit(stmt='BFS(m)',number=1000,globals=globals())
    t3=timeit(stmt='aStar(m)',number=1000,globals=globals())

    
    #textLabel(m,'BFS Time',t2)
    textLabel(m,'Maze Game','@')
    Button(
        m._win,
        text="Solution By BFS",
        font="100",
        width="50",
        padx="50",
        pady="5",
        border="5",
        background="black",
        foreground="green",
        command=lambda:BFS_Button()   
    ).pack()
    Button(
        m._win,
        text="Solution By DFS",
        font="100",
        width="50",
        padx="50",
        pady="5",
        border="5",
        background="black",
        foreground="green",
        command=lambda:DFS_Button() 
    ).pack()
    Button(
        m._win,
        text="Solution By aStar",
        font="100",
        width="50",
        padx="50",
        pady="5",
        border="5",
        background="black",
        foreground="green",
        command=lambda:aStar_Button() 
    ).pack()
  
    #l=textLabel(m,'BFS Cost',len(path)+1)
    #l=textLabel(m,'DFS Cost',len(path2)+1)

    m.run()