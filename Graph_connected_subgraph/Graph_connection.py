import networkx as nx
import matplotlib.pyplot as plt

pointList = ['A','B','C','D','E','F','G']
linkList = [('A','B'),('B','C'),('C','D'),('E','F'),('F','G'),]
G = nx.Graph()

 # 转化为图结构
for node in pointList:
    G.add_node(node)

for link in linkList:
    G.add_edge(link[0], link[1])
#
def subgraph():



    # 画图
    plt.subplot(211)
    nx.draw_networkx(G, with_labels=True)
    color =['y','g']
    subplot = [223,224]
    # 打印连通子图
    for c in nx.connected_components(G):
        nodeSet = G.subgraph(c).nodes()
        nodeName = []
        for node in nodeSet:
            nodeName.append(node)

        subgraph = G.subgraph(c)
        plt.subplot(subplot[0])  # 第二整行
        nx.draw_networkx(subgraph, with_labels=True,node_color=color[0])
        color.pop(0)
        subplot.pop(0)

    plt.show()

subgraph()


# 测试networkx的球连通子图的方法

def plain_bfs(G, source):
    """A fast BFS node generator"""
    G_adj = G.adj
    seen = set()
    nextlevel = {source}
    while nextlevel:
        thislevel = nextlevel
        nextlevel = set()
        for v in thislevel:
            if v not in seen:
                yield v
                seen.add(v)
                nextlevel.update(G_adj[v])
def connected():

    seen = set()
    for v in G:
        if v not in seen:
            c = set(plain_bfs(G, v))
            yield c
            seen.update(c)
    # return seen

for c in connected():
    print(c)


G_adj = G.adj
seen = set()
def DFSTraverse(G):
    for v in G:
        if v not in seen:
            c = set(DFS(G,v))
            seen.update(c)

def DFS(G,v):
    seen.add(v)
    yield v
    # 访问操作
    print(v)
    for w in G_adj[v]:
        if w not in seen:
            DFS(G,w)

DFSTraverse(G)

def DFS2(G,node0):
    G_adj = G.adj
    #queue本质上是堆栈，用来存放需要进行遍历的数据
    #order里面存放的是具体的访问路径
    queue,order=[],[]
    #首先将初始遍历的节点放到queue中，表示将要从这个点开始遍历
    queue.append(node0)
    while queue:
        #从queue中pop出点v，然后从v点开始遍历了，所以可以将这个点pop出，然后将其放入order中
        #这里才是最有用的地方，pop（）表示弹出栈顶，由于下面的for循环不断的访问子节点，并将子节点压入堆栈，
        #也就保证了每次的栈顶弹出的顺序是下面的节点
        v = queue.pop()
        order.append(v)
        #这里开始遍历v的子节点
        for w in G_adj[v]:
            #w既不属于queue也不属于order，意味着这个点没被访问过，所以讲起放到queue中，然后后续进行访问
            if w not in order and w not in queue:
                queue.append(w)
    return order

def DFSTraverse2(G):
    seenArray = []
    for v in G:
        if v not in seenArray:
            order = DFS2(G,v)
            seenArray.extend(order)
    return seenArray

seenArray = DFSTraverse2(G)
print(seenArray)
