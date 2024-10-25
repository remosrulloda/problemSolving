class ListNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def buildPyramid(self, pyramidValues):
        nodes = [[ListNode(val) for val in row] for row in pyramidValues]

        for row in range(len(nodes) - 1):
            for i in range(len(nodes[row])):
                nodes[row][i].left = nodes[row + 1][i]
                nodes[row][i].right = nodes[row + 1][i + 1]

        return nodes[0][0]
    
    def findPath(self, node, target, currentProduct=1, path=''):
        if node is None:
            return None

        newProduct = currentProduct * node.val

        if node.left is None and node.right is None:
            if newProduct == target:
                return path
            else:
                return None
        
        leftPath = self.findPath(node.left, target, newProduct, path + "L")
        if leftPath:
            return leftPath

        rightPath = self.findPath(node.right, target, newProduct, path + "R")
        if rightPath:
            return rightPath
        
        return None

    def solvePyramid(self, input):
        with open("pyramid_sample_input.txt", "r") as f:
                lines = f.read().strip().splitlines()

                target = int(lines[0].split(":")[1].strip())
                
                pyramidValues = [list(map(int, line.split(","))) for line in lines [1:]]
                
                root = self.buildPyramid(pyramidValues)

                path = self.findPath(root, target)

                return path if path else "No solution"
        

solution = Solution()
print(solution.solvePyramid("pyramid_sample_input.txt"))

            


    


