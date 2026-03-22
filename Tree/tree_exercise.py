class TreeNode:
    def __init__(self, data):   
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child_node):    
        child_node.parent = self
        self.children.append(child_node)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level    

    def print_tree(self):
        prefix = " " * self.get_level() * 3 + "|__" if self.parent else ""
        print(prefix + self.data.split("(")[0])
        if self.children:
            for child in self.children:
                child.print_tree()

    def print_hierarchy(self):
        prefix = " " * self.get_level() * 3 + "|__" if self.parent else ""
        print(prefix + self.data.split("(")[1].split(")")[0])
        if self.children:
            for child in self.children:
                child.print_hierarchy()            

def build_product_tree():
    root = TreeNode("Nilupul (CEO)")

    chinmay = TreeNode("Chinmay (CTO)")
    
    chinmay.add_child(TreeNode("Aamir (Application Head)"))

    vishwa = TreeNode("Vishwa (Infrastructure Head)")
    vishwa.add_child(TreeNode("Dhaval (Cloud Manager)"))    
    vishwa.add_child(TreeNode("Abhijit (App Manager)"))

    chinmay.add_child(vishwa)

    gels = TreeNode("Gels (HR Head)")
    gels.add_child(TreeNode("Waqas (Policy Manager)"))
    gels.add_child(TreeNode("Peter (Recruitment Manager)"))

    root.add_child(chinmay)
    root.add_child(gels)
   
    return root        

if __name__ == "__main__":
    root = build_product_tree()
     
    root.print_tree()
    root.print_hierarchy()