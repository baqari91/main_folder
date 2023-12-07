class TreeNode:
    def __init__(self, value):
        self.value = value  # Data შეინახება კვანძში
        self.children = []  # სია სადაც შეინახება სხვა კვანძები, "შვილები"


    def add_child(self, child_node):
        # ქმნის მშობელ-შვილის ურთიერთობას child-კვანძის დამატებით
        print("Adding " + child_node.value + " to " + self.value)
        self.children.append(child_node)

    def remove_child(self, child_node):
        # Removes a parent-child relationship by removing the specified child node
        print("Removing " + child_node.value + " from " + self.value)
        self.children = [child for child in self.children if child is not child_node] # მეთოდში მითითებული მნიშვნელობის გარდა დაბრუნდება სიაში არსებული ყველა მონაცემი


    def traverse(self):
        # Traverses the tree using depth-first search and prints the values of nodes
        nodes_to_visit = [self]  # Starts with the current node in the list

        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()  # Takes the last node in the list
            print(current_node.value)  # Prints the value of the current node
            nodes_to_visit += current_node.children  # Adds children of the current node to the list


# Creating nodes
root = TreeNode("root")  # Creates the root node
child1 = TreeNode("child1")  # Creates child nodes
child2 = TreeNode("child2")
child3 = TreeNode("child3")

# Adding children to the root node
root.add_child(child1)
root.add_child(child2)
root.add_child(child3)

# Creating a wide tree by adding multiple children to child1
child1.add_child(TreeNode("child1-ის შვილები 1"))
child1.add_child(TreeNode("child1-ის შვილები 2"))

child2.add_child(TreeNode("child2-ის შვილები"))
child2.add_child(TreeNode("ცჰილ"))

child3.add_child(TreeNode("Gg"))
child3.add_child(TreeNode("Gg"))

# Traversing the tree starting from the root
root.traverse()
