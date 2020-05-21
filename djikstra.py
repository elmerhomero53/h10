# -*- coding: utf-8 -*-
"""
Created on Thu May 21 11:50:27 2020

@author: jefe de jefes
"""

def djikstra(origen, destino):
    W = list(G.nodes)
    dist = {origen: 0}
    for w in W:
        if w != origen:
            dist.update({w: inf})
    
