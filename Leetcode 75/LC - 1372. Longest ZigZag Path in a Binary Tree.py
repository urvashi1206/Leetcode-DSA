class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def build_tree_from_level_order(arr):
    from collections import deque
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1
    while queue and i < len(arr):
        current = queue.popleft()
        if i < len(arr) and arr[i] is not None:
            current.left = TreeNode(arr[i])
            queue.append(current.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            current.right = TreeNode(arr[i])
            queue.append(current.right)
        i += 1
    return root

def maxZigZag(node, dir, length) -> int:
    if node is None:
        return length-1
    if(dir==0):
        r=maxZigZag(node.right,1,length+1)
        l=maxZigZag(node.left,0,1)
    else:
        r=maxZigZag(node.right,1,1)
        l=maxZigZag(node.left,0,length+1)
    return max(l,r)
        
def longestZigZag(root: TreeNode) -> int:
    if root.left is None and root.right is None:
        return 0
    node=root
    length=0
    return maxZigZag(node, 0, length)

arr = [1,1,1,None,1,None,None,1,1,None,1]
root = build_tree_from_level_order(arr)
result=longestZigZag(root)
print(result)