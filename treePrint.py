COUNT = [10]
def print2DUtil(root, space):
    # Base case
    if (root == None):
        return

    # Increase distance between levels
    space += COUNT[0]

    # Process right child first
    print2DUtil(root.r, space)

    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.val)

    # Process left child
    print2DUtil(root.l, space)


# Wrapper over print2DUtil()


def print2D(root):
    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)