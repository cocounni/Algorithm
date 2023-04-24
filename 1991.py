import sys

n = int(sys.stdin.readline().strip())

graph = {}

for i in range(n):
    node, left, right = sys.stdin.readline().split()
    graph[node] = [left, right]


def preorder(node):
    if node != ".":
        print(node, end="")
        preorder(graph[node][0])    #left
        preorder(graph[node][1])    #right

def inorder(node):
    if node != ".":
        inorder(graph[node][0])
        print(node, end="")
        inorder(graph[node][1])

def postorder(node):
    if node != ".":
        postorder(graph[node][0])
        postorder(graph[node][1])
        print(node, end="")

preorder("A")
print()
inorder("A")
print()
postorder("A")


# print(graph)