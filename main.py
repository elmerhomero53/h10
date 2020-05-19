# -*- coding: utf-8 -*-
"""
Created on Mon May 18 21:36:50 2020

@author: jose ramos
"""


import networkx as nx
from numpy import zeros, shape

def menu():
    print("Gracias por usar nuestro programa")
    print("Por favor asegurese que el archivo de texto se llame:")
    print("'guategrafo.txt' y se encuentre en este mismo folder")
    origen = input("Cual es su ciudad origen? ")
    destino = input("Cual es su ciudad destino? ")
    return (origen,destino)

def jalarinfo():
    f = open("guategrafo.txt","r")
    for x in f:
        x = x.split()
        G.add_node(x[0])
        G.add_node(x[1])
        G.add_edge(x[0],x[1], weight = int(x[2]))
        
def floyd():
    global M
    P = zeros(shape(M))
    M = M.A
    for k in range(shape(M)[0]):
        for i in range(shape(M)[0]):
            for j in range(shape(M)[0]):
                if M[i][j] > M[i][k] + M[k][j]:
                    M[i][j] = M[i][k] + M[k][j]
                    P[i][j] = k
    return P

def findPath(s,t):
    global P
    global G
    path = []
    ciudades = list(G.nodes)
    s = ciudades.index(s)
    t = ciudades.index(t)
    k = P[s][t]
    path.append(k)
    for i in range(k):
        path.append()

G = nx.DiGraph()

jalarinfo()
M = nx.to_numpy_matrix(G)

o,d = menu()

P = floyd()

