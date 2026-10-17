import json
line2 = "((3),(4),(2))"
tree = eval(line2)
print(tree)

line2 = "[[3],[4],[2]]"
tree = json.loads(line2)
print(tree)