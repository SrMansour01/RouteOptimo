import networkx as nx
import matplotlib.pyplot as plt
import random
import math
from PIL import Image
import time

etapa = 1

direcoes = {
    'direita': (1, 0),
    'esquerda': (-1, 0),
    'cima': (0, 1),
    'baixo': (0, -1)
}

#cria o grafo
rows, cols = 15, 15
G = nx.grid_2d_graph(rows, cols)

#Robo = (random.randint(0, rows - 1), random.randint(0, cols - 1))
#pc = (random.randint(0,rows-1), random.randint(0, cols-1))

Robo = (0,1)
pc = (0,9)

G.graph['start'] = Robo
G.graph['end'] = pc

#Obs = [(random.randint(0, rows-1), (random.randint(0, cols-1))) for i in range(random.randint(0, 10))]
#G.remove_nodes_from(Obs)

print(G.nodes())

#G.remove_node((9,0))
#G.remove_edge((0,2), (0,1))



pos = dict((n, n) for n in G.nodes())

path = nx.dijkstra_path(G, Robo, pc)
path_edges = list(zip(path, path[1:]))

fig, ax = plt.subplots()

nx.draw_networkx_nodes(G, pos, node_size=800, nodelist=[pc], node_color='red')
nx.draw_networkx_nodes(G, pos, node_size=800, nodelist=[Robo], node_color='black')
nx.draw_networkx_nodes(G, pos, node_size=500, nodelist=path, node_color="yellow")
nx.draw(G, pos, with_labels=True)
#plt.savefig("graph.png")

#with Image.open("graph.png") as img:
#    print(img.format, img.size, img.mode)
#    img.show()

print(f"{Robo} => {pc}")

print(f"caminho: {path}")
print(f"distancia: {len(path_edges)}m vai levar {int((len(path_edges)/20)*60)}seg")

robo_pos = Robo

for edge in path_edges:

    info_etap = []

    robo_posA = edge[0]
    robo_posP = edge[1]

    robo_dirI = (0,1)

    dx = robo_posP[0] - robo_posA[0]
    dy = robo_posP[1] - robo_posA[1]

    dir_Atual = (dx, dy)

    print(f"{etapa} = {robo_posA} => {robo_posP} | {dir_Atual}")

    plt.clf()
    nx.draw_networkx_nodes(G, pos, node_size=800, nodelist=[pc], node_color='red')
    nx.draw_networkx_nodes(G, pos, node_size=800, nodelist=[Robo], node_color='orange')
    nx.draw_networkx_nodes(G, pos, node_size=800, nodelist=[robo_posP], node_color='black')
    nx.draw_networkx_nodes(G, pos, node_size=500, nodelist=path, node_color="yellow")

    nx.draw(G, pos, with_labels=True)
    plt.text(0.01, 1, f"{etapa} = {robo_posA} => {robo_posP} | {dir_Atual}", transform=ax.transAxes, fontsize=8, color="black")
    plt.pause(10/20)

    etapa += 1

plt.show()