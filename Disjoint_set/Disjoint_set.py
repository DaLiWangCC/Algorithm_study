# 原始数据
pointList = ['A','B','C','D','E','F','G']
linkList = [('A','B'),('B','C'),('C','D'),('E','F'),('F','G'),]

# 递归方法

visted = []

def findNeighboor(v,oneSubset):
    oneSubset.append(v)
    visted.append(v)

    for link in linkList:
        if link[0]==v and link[1] not in oneSubset:
            findNeighboor(link[1],oneSubset)
        if link[1]==v and link[0] not in oneSubset:
            findNeighboor(link[0],oneSubset)
    return oneSubset

def findDisjointSet():
    allSet = []
    for point in pointList:
        if point not in visted:
            oneSubset = []
            oneSubset = findNeighboor(point,oneSubset)
            allSet.append(oneSubset.copy())
    print(allSet)

findDisjointSet()


# 并查集

class TreeNode():
    def __init__(self):
        self.parent = None
        self.children = []
        self.data = None

# 初始化
def initDisjointSet(allRootSet):
    nodes = {}
    for point in pointList:
        node = TreeNode()
        node.data = point
        node.parent = node
        allRootSet[point] = [point]
        nodes[point] = node
    return nodes

# 查询
def findRoot(a):
    nodes = []
    while a.parent != a:
        nodes.append(a)
        a = a.parent
    for node in nodes:
        node.parent = a
    return a

# 查询 递归实现
def findRoot2(a):
    if a == a.parent:
        return a
    else:
        a.parent = findRoot2(a.parent)

# 合并
def union_set(a,b,allRootSet):
    fa = findRoot(a)
    fb = findRoot(b)
    # fa的根指向fb,合并两个子树
    fa.root = fb
    # 删除一个子集代表
    allRootSet[fb.data].extend(allRootSet[fa.data])
    # if fa.data in allRootSet:
    allRootSet[fa.data] = None

def getDisjointSet():
    allRootSet = {}
    nodes = initDisjointSet(allRootSet)
    for link in linkList:
        union_set(nodes[link[0]],nodes[link[1]],allRootSet)

    print(allRootSet)

getDisjointSet()