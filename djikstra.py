# -*- coding: utf-8 -*-
"""
Created on Thu May 21 11:50:27 2020

@author: jose ramos
"""

"""
se baso en el algoritmo de djikstra de 
https://brilliant.org/wiki/dijkstras-short-path-finder/
para esta hoja
"""

def dijk(origen, destino):
    W = list(G.nodes)
    dist = {origen: (0,[])}
    for w in W:
        if w != origen:
            dist.update({w: (inf,[])})
    while W != []:
        sub = {v: dist[v] for v in W}
        v = min(sub, key= lambda x: x[0])
        W.remove(v)
        n = list(G.neighbors(v))
        #path = dist[v][1]
        #path.append('')
        for i in n:
            alt = G[v][i]['weight'] + dist[v][0]
            if alt < dist[i][0]:
                #path[-1] = v
                dist.update({i: (alt,path)})
        if v==destino:
            print('La ruta mas corta tiene distancia: ',dist[v][0])
            print('La ruta mas corta es: \n',dist[v][1])
            break