from tkinter import *
from tkinter.colorchooser import askcolor
from numpy import *



from sys import maxsize 
INT_MAX = maxsize 

  
# Returns true if edge u-v is a valid edge to be  
# include in MST. An edge is valid if one end is  
# already included in MST and other is not in MST. 
def isValidEdge(u, v, inMST): 
    if u == v: 
        return False
    if inMST[u] == False and inMST[v] == False: 
        return False
    elif inMST[u] == True and inMST[v] == True: 
        return False
    return True

def nextLetter():
    global letter
    letter=letter+1

def addFalse():
    print("false")
    global adding
    adding = False

def addTrue():
    print("TRUE")
    global adding
    adding = True

class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()

        self.add_button = Button(self.root, text='Add Vertex',command=addTrue)
        self.add_button.grid(row=0, column=0)

        self.add_edge = Button(self.root, text='Add Edge',command=self.addEdge)
        self.add_edge.grid(row=0, column=1)

        self.prims = Button(self.root, text='Do Prims',command=self.doPrims)
        self.prims.grid(row=1, column=1)

        self.from_entry=Entry(width=10)
        self.from_entry.grid(row=0, column=2)
        self.to_entry=Entry(width=10)
        self.to_entry.grid(row=0, column=4)
        self.distance=Entry(width=10)
        self.distance.grid(row=0, column=3)
        self.c = Canvas(self.root, bg='white', width=600, height=600)
        self.c.grid(row=2, columnspan=5)

        self.l1=Label(text="Start Vertex")
        self.l1.grid(row=1,column=2)

        self.l2=Label(text="End Vertex")
        self.l2.grid(row=1,column=4)

        self.l3=Label(text="Weight")
        self.l3.grid(row=1,column=3)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
    
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        
        self.c.bind('<Button-1>', self.plot)
       
    def plot(self, event):
        if adding:
            self.c.create_oval(event.x-35, event.y-35, event.x+35, event.y+35, fill="#09dcf6", tags="A")
            self.c.create_text(event.x,event.y,text=chr(letter),width=30,font=("Purisa", 15))
            dict[letter]=[event.x,event.y]
            print(dict)
            nextLetter()
            addFalse()

    def addEdge(self):
        #1.) grab the letters from the entries
        global dict
        
        fromVertex=self.from_entry.get()
        toVertex=self.to_entry.get()
        #2.) update the matrix using row = 65 - asci(fromVertex) col = 65- asci(toVertex)
        print(ord(fromVertex))
        row=ord(fromVertex)-65
        col=ord(toVertex)-65
        print("row "+ str(row)+ " col " + str(col))
        matrix[row][col]=int(self.distance.get())
        matrix[col][row]=int(self.distance.get())
        
        self.c.create_line(dict[ord(fromVertex)][0],dict[ord(fromVertex)][1],dict[ord(toVertex)][0],dict[ord(toVertex)][1],width=3,fill="yellow")
        midx=(max(dict[ord(fromVertex)][0],dict[ord(toVertex)][0])+min(dict[ord(fromVertex)][0],dict[ord(toVertex)][0]))/2+12
        midy=(max(dict[ord(fromVertex)][1],dict[ord(toVertex)][1])+min(dict[ord(fromVertex)][1],dict[ord(toVertex)][1]))/2
        self.c.create_text(midx,midy,text=self.distance.get(),width=30,font=("Purisa", 15))
        
        print(matrix)


    def doPrims(self):
        
        global dict
        cost=matrix
        V=len(dict)
        inMST = [False] * V 
        
        # Include first vertex in MST 
        inMST[0] = True
    
        # Keep adding edges while number of included  
        # edges does not become V-1. 
        edge_count = 0
        mincost = 0
    
        print(V-1)
        while edge_count < V - 1: 
    
            # Find minimum weight valid edge. 
            minn = INT_MAX 
            a = -1
            b = -1
            for i in range(V): 
                for j in range(V): 
                    if cost[i][j] < minn: 
                        if isValidEdge(i, j, inMST): 
                            minn = cost[i][j] 
                            a = i 
                            b = j 
    
            if a != -1 and b != -1: 
                print("Edge %d: (%d, %d) cost: %d" % 
                    (edge_count, a, b, minn)) 
                self.c.create_line(dict[int(a)+65][0],dict[int(a)+65][1],dict[int(b)+65][0],dict[int(b)+65][1],width=3,fill="green")
                edge_count += 1
                mincost += minn 
                inMST[b] = inMST[a] = True
    
        print("Minimum cost = %d" % mincost) 
if __name__ == '__main__': 
    letter=65
    adding=False
    dict={}
    matrix = zeros(shape=(26,26))
    for x in range(26):
       for y in range(26):
            matrix[x][y]=INT_MAX
    print(matrix)
    addFalse()
    Paint()