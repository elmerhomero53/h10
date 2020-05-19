# -*- coding: utf-8 -*-
"""
Created on Mon May 18 21:36:50 2020

@author: jose ramos
"""


import networkx as nx
from numpy import zeros, shape, inf

def pedir():
    origen = input("Cual es su ciudad origen?\n")
    destino = input("Cual es su ciudad destino?\n")
    return (origen,destino)

def menu1():
    n = 0
    while n<4:
        print("Gracias por usar nuestro programa")
        print("Desea:")
        print("1. Calcular la ruta mas corta")
        print("2. Modificar el grafo")
        print("3. Calcular el centro del grafo")
        print("4. Salir")
        n = int(input("Ingrese el numero de la opcion que quiere por favor"))
        if n == 1:
            o,d = pedir()
            findPath(o,d)
        elif n == 2: 
            print("Desea:")
            print("1. Agregar nodos")
            print("2. Agregar aristas")
            print("3. Ambos")
            m = input("Ingrese el numero de la opcion:")
            if m==1:
                modificar(True,False)
            elif m==2:
                modificar(False,True)
            else:
                modificar(True,True)
        elif n==3:
            m = center()
            ciudades = list(G.nodes)
            print("El centro del grafo es: ",ciudades[m])
        else:
            print("Gracias por usar el programa")
    
def jalarinfo():
    f = open("guategrafo.txt","r")
    for x in f:
        x = x.split()
        G.add_node(x[0])
        G.add_node(x[1])
        G.add_edge(x[0],x[1], weight = int(x[2]))
        
def modificar(agregarN,agregarC):
    if agregarN:
        c = input("Ingrese el nombre de la ciudad que desea agregar")
        G.add_node(c)
    elif agregarC:
        c1 = input("Donde comienza su nueva ruta?")
        c2 = input("Donde comienza su nueva ruta?")
        w = input("Cual es el costo de esta ruta?")
        G.add_edge(c1,c2,weight=w)        
    
def center():
    T = M.T
    y = []
    for x in T:
        x[x== inf] = 0
        y.append(max(x))
    return y.index(min(y))

def floyd():
    global M
    M = M.A
    P = zeros(shape(M))
    for i in range(shape(M)[0]):
        for j in range(shape(M)[0]):
            if i==j:
                M[i][j] = 0
            elif M[i][j] == 0:
                M[i][j] = inf
    for k in range(shape(M)[0]):
        for i in range(shape(M)[0]):
            for j in range(shape(M)[0]):
                if M[i][j] > M[i][k] + M[k][j]:
                    M[i][j] = M[i][k] + M[k][j]
                    P[i][j] = k+1      
    return P

def findPath(s,t):
    global P
    global G
    path = []
    ciudades = list(G.nodes)
    s = ciudades.index(s)
    t = ciudades.index(t)
    path.append(P[s][t])
    n = int(path[-1])
    while n != 0:
        path.append(P[n-1][t])
        n = int(path[-1])
    print("El camino mas corto es: ")
    print(ciudades[s])
    for x in path:
        if x!=0:
            print(ciudades[int(x-1)])
        else:
            print(ciudades[t])
            break
            
G = nx.DiGraph()

jalarinfo()
M = nx.to_numpy_matrix(G)
P = floyd()

menu1()
