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
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("MacBook"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("ThinkPad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root        

if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree()