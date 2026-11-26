# Problem Set 4A
# Name:
# Collaborators:

from tree import Node # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the test named test_data_representation should pass.
tree1 = Node(8,Node(2,Node(1),Node(6)), Node(10) )
tree2 = Node(7,Node(2,Node(1),Node(5,Node(3),Node(6))), Node(9,Node(8),Node(10)))
tree3 = Node(5,Node(3,Node(2),Node(4)),Node(14,Node(12),Node(21,Node(20),Node(26))))

# min_heap = Node(4,Node(10,Node(18),Node(11)),Node(5,(Node(7),Node(8))))
# max_heap = Node(21,Node(15,Node(7),Node(11)),Node(3,Node(2),Node(1)))


def find_tree_height(tree):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    
    depth_left  = 0
    depth_right = 0
    depth       = 0


    left_branch  = tree.get_left_child()
    right_branch = tree.get_right_child()
    
    
    if left_branch  is not None:
         depth_left  += 1 + find_tree_height(left_branch)
    if right_branch is not None:
         depth_right += 1 + find_tree_height(right_branch)
    
    
    depth = depth_left if depth_left > depth_right else depth_right
    
    return depth



def is_heap(tree, compare_func):
    '''
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value
            i.e. op(child_value,parent_value) for a max heap would return True if child_value < parent_value and False otherwise
                 op(child_value,parent_value) for a min meap would return True if child_value > parent_value and False otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    ''' # TODO: Remove pass and write your code here   
    heap_left  = True
    heap_right = True

    left_branch  = tree.get_left_child()
    right_branch = tree.get_right_child()

    if left_branch  is not None:
        heap_left   = compare_func(left_branch.value,tree.value)  and is_heap(left_branch, compare_func)
    if right_branch is not None:
        heap_right  = compare_func(right_branch.value,tree.value) and is_heap(right_branch, compare_func)
        
        
    return True if (heap_left and heap_right) else False


# max heap comparator
def compare_func_max(child_value, parent_value):
    if child_value < parent_value:
        return True
    return False

# min heap comparator
def compare_func_min(child_value, parent_value):
    if child_value > parent_value:
        return True
    return False
 

def main():
    
    # print(tree1)
    # print(tree2)
    # print(tree3)    
    # treeX  =tree2.get_left_child()
     # treeXX =treeX.get_left_child()
    # treeXYZ =treeX.get_left_child()

    # print(treeX.get_left_child())
    # print(treeXYZ.get_left_child())
    
    
    # print(find_tree_height(tree1), "hello")
    # print(find_tree_height(tree2), "hello")
    # print(find_tree_height(tree3), "hello")
    
    print(is_heap(tree1,compare_func_max))
    print(is_heap(tree2,compare_func_max))
    print(is_heap(tree3,compare_func_max))
    
    print(is_heap(tree1,compare_func_min))
    print(is_heap(tree2,compare_func_min))
    print(is_heap(tree3,compare_func_min))
    
    return 0 


if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    main()
