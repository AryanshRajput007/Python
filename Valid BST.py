class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        # Create an array to keep track of parent nodes
        parent = [-1] * n

        for i in range(n):
            if leftChild[i] != -1:
                # If a left child exists, check if it has a valid parent
                if parent[leftChild[i]] != -1:
                    return False
                parent[leftChild[i]] = i

            if rightChild[i] != -1:
                # If a right child exists, check if it has a valid parent
                if parent[rightChild[i]] != -1:
                    return False
                parent[rightChild[i]] = i

        # Check if there is exactly one node with no parent, which is the root
        root_count = parent.count(-1)
        if root_count != 1:
            return False
        if root_count == 0:
            return False

        # Convert the parent array into a binary tree
        root = parent.index(-1)

        # Use the isBST function from the reference code to check if it's a BST
        prev = [float('-inf')]
        return self.isBSTUtil(root, parent, prev)

    def isBSTUtil(self, node, parent, prev):
        if node == -1:
            return True

        if not self.isBSTUtil(parent[node], parent, prev):
            return False

        if node <= prev[0]:
            return False

        prev[0] = node

        return True
      