#!/usr/bin/env python3

import os
import sys
import networkx as nx

G = nx.DiGraph()

for i in os.listdir(sys.argv[1]):
    ii = os.path.realpath(sys.argv[2] + '/' + i).rpartition('/')[2]
    with open(sys.argv[1] + '/' + i) as deps:
        for j in deps:
            j = j.strip()
            jj = os.path.realpath(sys.argv[2] + '/' + j).rpartition('/')[2]
            G.add_edge(ii, jj)

for c in nx.strongly_connected_components(G):
    if len(c) > 1:
        print(c)
        print(nx.to_dict_of_lists(G.subgraph(c).copy()))
