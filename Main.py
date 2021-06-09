import io
import collections
from Cell import Cell

mypuzzle = []
mygraph = dict()


address = ".\puzzles\puzzle0.txt"
with open(address) as reader :
    myinput = reader.read()


buf = io.StringIO(myinput)
n , m = map(int ,buf.readlines(1)[0].replace("\t" , " ").replace("\n" , "").split(" "))
for i in range(n):
    buffread = buf.readlines(1)[0].replace("\t" , " ").replace("\n" , "").split(" ")
    mynd = []
    for ii in range(m) : 
        mynd.append(buffread[ii])
    mypuzzle.append(mynd)

for i in range(n):
    for ii in range(m):
        mygraph[(i,ii)] = Cell(mypuzzle[i][ii])

# print(mygraph)


def forward_checking(graph ,x, y , n):
    onesCol = 0
    zerosCol = 0
    onesRow = 0
    zerosRow = 0
    for i in range(n):
        if graph[(i , y)].value == 1:
            onesCol +=1
        elif graph[(i , y)].value == 0:
            zerosCol +=1
        if graph[(x , i)].value == 1:
            onesRow +=1
        elif graph[(x , i)].value == 0:
            zerosRow +=1

    checkEmptyInRow  = False
    checkEmptyInCol = False
# check number of 0's and 1's
    for i in range(n):
        if graph[(i , y)].value == -1:
            checkEmptyInCol = True
            if onesCol >= n/2 :
                if 1 in graph[(i , y)].domain:
                    graph[(i , y)].domain.remove(1)
                    if len(graph[(i , y)].domain) == 0:
                        return False
            if  zerosCol >= n/2 :
                if 0 in graph[(i , y)].domain:
                    graph[(i , y)].domain.remove(0)
                    if len(graph[(i , y)].domain) == 0:
                        return False
            

        if graph[(x , i)].value == -1:
            checkEmptyInRow = True
            if onesRow >= n/2 :
                if 1 in graph[(x , i)].domain:
                    graph[(x , i)].domain.remove(1)
                    if len(graph[(x , i)].domain) == 0:
                        return False
            
                
            if zerosRow >= n/2 :
                if 0 in graph[(x , i)].domain:
                    graph[(x , i)].remove(0)
                    if len(graph[(x , i)].domain) == 0:
                        return False
        

#  check in row
    for i in range(-2 , 3 , 2):
        if i == 0 :
            continue
        if x + i < n and x + i >= 0: 
            if graph[(x + i , y)] == -1 :
                if graph[(x, y)] == 1 and graph[(x + i/2 , y)] == 1:
                    if 1 in graph[(x + i, y)].domain:
                        graph[(x + i, y)].domain.remove(1)
                        if len(graph[(x+ i , y)].domain) == 0:
                            return False
                if graph[(x, y)] == 0 and graph[(x + i/2 , y)] == 0:
                    if 0 in graph[(x + i, y)].domain:
                        graph[(x + i, y)].domain.remove(0)
                        if len(graph[(x + i , y)].domain) == 0:
                            return False
            
        
        if y + i < n and y + i >= 0: 
            if graph[(x , y + i)] == -1 :
                if graph[(x, y)] == 1 and graph[(x , y + i/2)] == 1:
                    if 1 in graph[(x, y + i)].domain:
                        graph[(x , y + i)].domain.remove(1)
                        if len(graph[(x , y + i)].domain) == 0:
                            return False
            
                if graph[(x, y)] == 0 and graph[(x  , y + i/2)] == 0:
                    if 0 in graph[(x, y + i)].domain:
                        graph[(x, y + i)].domain.remove(0)
                        if len(graph[(x , y + i)].domain) == 0:
                            return False
            

    #    check Same  NOT SURE
        
        # row = ""
        # col = ""
        # if checkEmptyInCol == False : 
        #     for i in range(n):
        #         row += graph[(i , y)] 

        # if checkEmptyInRow == False : 
        #     for i in range(n) : 
        #         col += graph(x , i)


    return True

                
 
                


