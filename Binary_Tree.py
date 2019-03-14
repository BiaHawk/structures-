class Node:

    def _init_(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    def _bool_(self):
        if self.key != None:
            return True
        return False


class Tree:

    def _init_(self, root):
        self.root = root

    def search(self, k):
        node = self.root
        while node and node.key != k:
            if k < node.key:
                node = node.left
            else:
                node = node.right
        if not node:
            print('Node with key \"{}\" not found.'.format(k))
        return node

    def maximum(self):
        node = self.root
        while node.right != None:
            node = node.right
        return node

    def minimum(self):
        node = self.root
        while node.left != None:
            node = node.left
        return node

    def insert(self, new_node):
        node = self.root
        if node == None:
            self.root = new_node
        else:
            k = new_node.key
            while True:
                if k <= node.key:
                    if node.left:
                        node = node.left
                    else:
                        node.left = new_node
                        new_node.parent = node
                        break
                else:
                    if node.right:
                        node = node.right
                    else:
                        node.right = new_node
                        new_node.parent = node
                        break

    def delete(self, k):
        node = self.search(k)
        if not node.left and not node.right:
            if k < node.parent.key:
                node.parent.left = None
            else:
                node.parent.right = None
        elif not node.left:
            if k < node.parent.key:
                node.parent.left = node.right
                node.right.parent = node.parent
            else:
                node.parent.right = node.right
                node.right.parent = node.parent
        elif not node.right:
            if k < node.parent.key:
                node.parent.left = node.left
                node.left.parent = node.parent
            else:
                node.parent.right = node.left
                node.left.parent = node.parent
        else:
            temp = node.right
            while temp.left:
                temp = temp.left
            if temp != node.right:
                if temp.right:
                    temp.parent.left = temp.right
                    temp.right.parent = temp.parent
                temp.parent = node.parent
                temp.left = node.left
                temp.right = node.right
                node.left.parent = temp
                node.right.parent = temp
                if node != self.root:
                    if k < node.parent.key:
                        node.parent.left = temp
                    else:
                        node.parent.right = temp
                else:
                    self.root = temp
            else:
                temp.left = node.left
                node.left.parent = temp
                temp.parent = node.parent
                if node != self.root:
                    if node == node.parent.left:
                        node.parent.left = temp
                    else:
                        node.parent.right = temp
                else:
                    self.root = temp

    def sucessor(self, k):
        node = self.search(k)
        if node.right:
            temp = node.right
            while temp.left != None:
                temp = temp.left
            return temp
        else:
            temp = node.parent
            while temp != None and temp.key < k:
                temp = temp.parent
            if not temp:
                return 0
            else:
                return temp.key

    def predecessor(self, k):
        node = self.search(k)
        if node:
            if node.left:
                temp = node.left
                while temp.right:
                    temp = temp.right
                return temp
            else:
                if node.parent:
                    if node.parent.key < k:
                        return node.parent.key
                return 0
        else:
            print('Node with key \"{}\" not found.'.format(k))
