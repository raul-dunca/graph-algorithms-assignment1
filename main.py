import copy
import time
import random

class Vertex:
    def __eq__(self, other):
        pass
    def __hash__(self):
        pass

class Graph:

    def __init__(self, n):
        self.vertices = dict()
        for i in range(n):
            self.vertices[i] = (set(),set())
        self.edges=dict()

    def add_edge(self, x, y,c):
        if x not in self.vertices:
            print("Invalid input!")
            return
        if y not in self.vertices:
            print("Invalid input!")
            return
        if c==0:
            print("Invalid input!")
            return
        if str(x)+"-"+str(y)  in self.edges:
            print("Edge already there!")
            return
        self.vertices[x][0].add(y)
        self.vertices[y][1].add(x)
        self.edges[str(x)+"-"+str(y)]=c
    def remove_edge(self,x,y):
        if x not in self.vertices:
            print("Invalid input!")
            return
        if y not in self.vertices:
            print("Invalid input!")
            return
        if str(x)+"-"+str(y) not in self.edges:
            print("Invalid input!")
            return
        self.vertices[x][0].remove(y)
        self.vertices[y][1].remove(x)
        self.edges[str(x) + "-" + str(y)] = 0
    def add_vertex(self):
        self.vertices[self.get_nr_of_vertices()+1]=(set(),set())
    def delete_vertex(self,x):
        if x not in self.vertices:
            print("Invalid input!")
            return
        new_dic=dict()
        l=self.parse_vertices()
        for i in l:
            if x in self.vertices[i][0]:
                self.vertices[i][0].remove(x)
            if x in self.vertices[i][1]:
                self.vertices[i][1].remove(x)
        del self.vertices[x]
        for key in self.edges:
            if int(key[0])==int(x) or int(key[2])==int(x):
                pass
            else:
                new_dic[key]=self.edges[key]

        self.edges=copy.deepcopy(new_dic)
    def is_edge(self, x, y):
        if x not in self.vertices:
            print("Invalid input!")
            return
        if y not in self.vertices:
            print("Invalid input!")
            return
        if (y in self.vertices[x][0]):
            return 1, self.edges[str(x)+"-"+str(y)]
        else:
            return 0,0

    def get_cost(self,x,y):
        if x not in self.vertices:
            print("Invalid input!")
            return
        if y not in self.vertices:
            print("Invalid input!")
            return
        if str(x)+"-"+str(y) not in self.edges:
            print("Invalid input!")
            return

        return self.edges[str(x)+"-"+str(y)]

    def set_cost(self,x,y, new):
        if x not in self.vertices:
            print("Invalid input!")
            return
        if y not in self.vertices:
            print("Invalid input!")
            return
        if new ==0:
            print("Invalid input!")
            return
        if str(x)+"-"+str(y) not in self.edges:
            print("Invalid input!")
            return
        self.edges[str(x)+"-"+str(y)] = new
    def parse_vertices(self):
        vertices_list = list()
        for key in self.vertices:
            vertices_list.append(key)
        return vertices_list

    def parse_nout(self, x):
        if x not in self.vertices:
            print("Invalid input!")
            return
        nout_vertices = list()
        for y in self.vertices[x][0]:
            nout_vertices.append(y)
        return nout_vertices

    def parse_nin(self, x):
        if x not in self.vertices:
            print("Invalid input!")
            return
        nin_vertices = list()
        for y in self.vertices[x][1]:
            nin_vertices.append(y)
        return nin_vertices
    def get_nr_of_vertices(self):
        return len(self.vertices)
    def get_nr_of_edges(self):
        return len(self.edges)
    def get_out_degree(self,x):
        if x not in self.vertices:
            print("Invalid input!")
            return

        return len(self.vertices[x][0])

    def get_in_degree(self,x):
        if x not in self.vertices:
            print("Invalid input!")
            return

        return len(self.vertices[x][1])
        # def write_textfile(self,filename):
   #     f = open(filename, "wt")  # wt -> write, text-mode
   #     for cl in self._data:
    #        f.write(str(cl.idc) + ',' + cl.name + "\n")

    #    f.close()
    def copy(self):
        n=copy.deepcopy(self)
        return n

def read_textfile(filename):
        k=0
        f = open(filename, "rt")  # rt -> read, text-mode
        for line in f.readlines():
            if k==0:
               n, m = line.split(maxsplit=1, sep=' ')
               g = Graph(int(n))
               k+=1
            else:
                x, y,cost= line.split(maxsplit=2, sep=' ')

                g.add_edge(int(x),int(y),int(cost))

        f.close()
        return g


def write_textfile(g,filename):

    f = open(filename, "wt")  # rt -> read, text-mode
    f.write(str(g.get_nr_of_vertices())+" "+ str(g.get_nr_of_edges())+"\n")
    for key in g.edges:
        f.write(str(key[0]) + " " + str(key[2]) + " "+ str(g.get_cost(int(key[0]),int(key[2]))) + "\n")

    f.close()
def print_edges(g):
    for key in g.edges:
        print(key, g.get_cost(int(key[0]),int(key[2])))
def print_graph(g):
    print("Outbound neighbors:")
    for x in g.parse_vertices():
        s = str(x) + ":"

        for y in g.parse_nout(x):
            s = s + " " + str(y)
        print(s)
    print("Inbound neighbors:")
    for x in g.parse_vertices():
        s = str(x) + ":"
        for y in g.parse_nin(x):
            s = s + " " + str(y)
        print(s)

def create_random_graph(n, m):
    g = Graph(n)
    while m > 0:
        x = random.randrange(n)
        y = random.randrange(n)
        if g.is_edge(x, y)==(0,0):
            g.add_edge(x, y,random.randint(2,20))
            m = m - 1
    return g
def print_menu():
    print("0. Exit")
    print("1. Add edge")
    print("2. Remove edge")
    print("3. Add vertex")
    print("4. Remove vertex")
    print("5. Get cost of edge")
    print("6. Set cost of edge")
    print("7. Get nr of vertices")
    print("8. Get nr of edges")
    print("9. Parse all vertices")
    print("10. Parse nin")
    print("11. Parse nout")
    print("12. Print graph")
    print("13. Get nout degree")
    print("14. Get nin degree")


def start(g):
    while True:
        print("\n")
        print_menu()
        opt = input()
        if opt == "1":
            x = input("Give the x: ")
            y = input("Give the y: ")
            c=input("Give the cost: ")
            g.add_edge(int(x),int(y),int(c))

        elif opt == "2":
            x = input("Give the x: ")
            y = input("Give the y: ")
            g.remove_edge(int(x),int(y))

        elif opt == "3":
            g.add_vertex()
        elif opt == "4":
            x = input("Give the x: ")
            g.delete_vertex(int(x))

        elif opt == "5":
            x = input("Give the x: ")
            y = input("Give the y: ")
            print(g.get_cost(int(x),int(y)))
        elif opt == "6":
            x = input("Give the x: ")
            y = input("Give the y: ")
            n=input("New cost is: ")
            g.set_cost(int(x),int(y),int(n))
        elif opt == "7":
            print(g.get_nr_of_vertices())
        elif opt == "8":
            print(g.get_nr_of_edges())
        elif opt == "9":
            l=g.parse_vertices()
            for i in l:
                print(i)
        elif opt == "10":
            x= input("Give x: ")
            l=g.parse_nin(int(x))
            for i in l:
                print(i)
        elif opt == "11":
            x = input("Give x: ")
            l = g.parse_nout(int(x))
            for i in l:
                print(i)
        elif opt == "12":
            print_graph(g)
        elif opt=="13":
            x = input("Give x: ")
            print(g.get_in_degree(int(x)))
        elif opt=="14":
            x = input("Give x: ")
            print(g.get_out_degree(int(x)))
        elif opt=="0":
            return
def main():

    g=create_random_graph(100,100*10)
    #g=read_textfile("random_graph1.txt")
    start(g)
    #print_graph(g)
    # parse_graph(g)


main()