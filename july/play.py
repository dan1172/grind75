class Node:
    
    
    def __init__(self, children, data, name):
        self.children = children
        self.name = name
        self.data = data # -1 for another subdirectory, or any number >= 1 if its a file

class GigaNode(Node):
    pass

# root: root node of the tree like structure
def total_file_size(root):
    total_file_size = 0
    stack = [root]
    while stack:
        cur_node = stack.pop()
        if cur_node.data != -1:
            # it is a file
            total_file_size += cur_node.data
        else:
            for child in cur_node.children:
                stack.append(child)
    return total_file_size


def test_total_file_size():
    child1 = Node([], 5)
    child2 = Node([], 2)
    child3 = Node([], 1)
    child4 = Node([], 6)
    root = Node([child1, child2, child3, child4], -1)
    print(total_file_size(root))
    
# test_total_file_size()


def test_total_file_size():
    child1 = Node([], 5)
    child2 = Node([], 2)
    subdir1 = Node([child1, child2], -1)
    child3 = Node([], 1)
    child4 = Node([], 6)
    subdir2 = Node([child3, child4], -1)
    root = Node([subdir1, subdir2], -1)
    print(total_file_size(root))
    
# test_total_file_size()

# n : int
# list of names
def largest_collections(n, root):
    list = []
    
    def rec_count_collection_size(root):
        if root.data == -1:
            collection_size = 0
            for child in root.children:
                collection_size += rec_count_collection_size(child)
            list.append((root.name, collection_size))
            return collection_size
        else:
            return root.data
    rec_count_collection_size(root)
    
    list.sort(key = lambda e : e[1], reverse=True)
    for (name, size) in list[:n]:
        print(f"name: {name}, size: {size}")
      
def test_largest_collections1():
    child1 = Node([], 5, "child1")
    root = Node([child1], -1, "root")
    largest_collections(1, root)
        

def test_largest_collections2():
    child1 = Node([], 5, "child1")
    child2 = Node([], 2, "child2")
    subdir1 = Node([child1, child2], -1, "subdir1")
    child3 = Node([], 1, "child3")
    child4 = Node([], 7, "child4")
    subdir2 = Node([child3, child4], -1, "subdir2")
    root = Node([subdir1, subdir2], -1, "root")
    largest_collections(2, root)

# test_largest_collections2()

# file_list: list of files, n : int
def generate_report(root, n):
    total_size = total_file_size(root)
    print(f"The total file size is {total_size}")
    largest_collections(n, root)


def test_generate_report1():
    child1 = Node([], 5, "child1")
    child2 = Node([], 2, "child2")
    subdir1 = Node([child1, child2], -1, "subdir1")
    child3 = Node([], 1, "child3")
    child4 = Node([], 7, "child4")
    subdir2 = Node([child3, child4], -1, "subdir2")
    root = Node([subdir1, subdir2], -1, "root")
    generate_report(root, 2)
    
def test_generate_report():
    child1 = Node([], 5, "child1")
    child2 = Node([], 2, "child2")
    child3 = Node([], 1, "child3")
    child4 = Node([], 7, "child4")
    subsubdir1 = Node([child3, child4], -1, "subsubdir1")  # 8
    subdir1 = Node([child1, child2, subsubdir1], -1, "subdir1") # 15

    child7 = Node([], 11, "child7")
    child8 = Node([], 20, "child8")
    child9 = Node([], 20, "child9")
    subdir2 = Node([child7, child8, child9], -1, "subdir2") # 51
    
    child5 = Node([], 1, "child5")
    child6 = Node([], 7, "child6")
    root = Node([subdir1, child5, child6, subdir2], -1, "root") # 74
    # generate_report(root, 1)
    # generate_report(root, 2)
    # generate_report(root, 3)
    generate_report(root, 4)
    
    
    
test_generate_report()


# file system that stores files
# grouped into collections
# where are teh resources taken up
# which collections are the largest
# which file in each collection takes up the most case
# generate a report that lists the total file size
# and the largest n collections 