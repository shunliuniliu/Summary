# PDD面试

关键点**采用非递归**

```
           1
    |               |   
    2               3
 |    |           |   |
 4    7          8   9
每次遇到叶子节点，打印从根节点到叶子节点的路径，非递归
124
127
138
139

class Node {
	Node left;
	Node right;
	int val;
}

```

## 思路1

**递归转栈**，手动推一遍，画出来，很简单

第一反应是用栈来解决

````Python

#Python3.6
import copy

class Stack:
    #模拟栈

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)



error_message = 'errors in inputing'

stack = Stack()

def print_single_path(stack):
    temp_list= []
    while not stack.isEmpty():
        node = stack.pop()
        temp_list.append(node)
    temp_list = temp_list[::-1]

    print(''.join(temp_list))

def print_all_ath(node):

    if node == None:
        return error_message
    stack.push(node)

    while stack.isEmpty():

        if node.left!=None:
            stack.push(node.left)

        elif node.right!=None:
            stack.push(node.right)

        else:
            print_single_path(copy.deepcpy(stack))
            node = stack.pop()

````

## 思路2

**递归**

要找到所有的路径，利用**前序遍历即可做到**，我们维护一个数组保存路径上面的点，同时维护一个sum，当到达叶子结点的时候判断是否相等即可

```c++
//二叉树结点  
struct BinaryTreeNode{  
    int value;  
    BinaryTreeNode *lson;  
    BinaryTreeNode *rson;  
};   
  
//打印路径  
void Print(int *path, int n){  
    for(int i = 0; i < n; i++){  
        cout<<path[i]<<" ";   
    }  
    cout<<endl;   
}   
  
//打印和为k的所有路径  
void PrintPath(BinaryTreeNode *root, int *path, int pos, int sum, int k){  
    //不合法数据   
    if(path == NULL){  
        return;  
    }  
    //到底叶子结点   
    if(root == NULL){  
        //和为value就打印   
        if(sum == k){  
            Print(path, pos);  
        }  
    }  
    path[pos] = root->value;  
    PrintPath(root->lson, path, pos+1, sum+root->value, k);  
    PrintPath(root->rson, path, pos+1, sum+root->value, k);  
}   
```

