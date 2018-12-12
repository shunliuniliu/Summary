#1.

````
1.输入是一个只含有 0 和 1 的二维矩阵，每一行都是排过序的，也就是说每一行前一部分都 是 0,剩下的全都是 1。请找哪些行包含的 1 最多。要求对于 MxN 的矩阵，时间复杂度是 O(M+N)，空间复杂度是 O(1)
示例:
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
对于上面的函数，第 2 行和第 6 行都有 8 个 1。所以输出[2,8] 和 [6,8];

````



```python
#Python3.6

def solution(matrix):
    result = []
    result_dict = {}
    index = 1
    for array in matrix:
        result_dict[index] = sum(array)
        index += 1

    max_sum = max(result_dict.values())

    for key, value in result_dict.items():
        if value == max_sum:
            result.append([key,value])

    return result


if __name__ ==  '__main__':

    # 默认矩阵中都是int型的0和1
    input_matrix = [
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    result = solution(input_matrix)

    for item in result:
        print(item)

```



# 2.

```
输入一个字符串比如{[(2+3)*(1-3)] + 4}*(14-3)，分析它的括号使用是否正确 括号有三种，小括号()，中括号[]，大括号{} 正确的括号使用必须满足以下条件(和数学上定义一致):
1) 左右括号必须匹配
2) 每一种类型括号只能和同一类型的括号匹配，即(和)匹配 [和]匹配 {和}匹配
3) 括号有优先级，小括号在最内层，中括号必须嵌套在小括号外面，大括号必须嵌套的中
括号外面
4) 比如{}, ([])这样都是非法的
5) 除了最外层可以连续嵌套大括号外，小括号和中括号不能连续嵌套，比如(()), [[()]]都是
非法的，但是{{[()]}}是合法的
6) 不需要考虑除了括号之外的其他字符是否违反了数学上的规定
```



```python
#Python3.6

import sys

class Stack:
    """模拟栈"""

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

def check(left, right):

    if right==')' and left=='(':
        return True

    if right==']' and left=='[' :
        return True

    if right=='}' and left=='{':
        return True

    return False

if __name__ ==  '__main__':

    error_message = 'error in input string'

    left_set  = set( '([{')
    right_set = set( ')]}')
    input_string = sys.stdin.readline()
    # input_string = "{[(2 + 3) * (1 - 3)] + 4} * (14 - 3)"
    input_string = input_string.replace(' ','')

    stack = Stack()
    try:
        for character in input_string:
            if character in left_set:
                stack.push(character)
            if character in right_set:
                if not check(stack.pop(),character):
                    print(error_message)
                    break

        if not stack.isEmpty():
            print(error_message)

    except Exception:
        print(error_message)

    print("right")

```



# 3.

```
房间里面有一个机器人位于位置(0, 0)。房间的形状和面积都是未知的。你可以通过一个 遥控器来控制机器人往前后左右四个方向中的任何一个移动一个格子。
移动的函数是 boolean move(int direction), direction: 0, 1, 2, 3。如果机器人发现移动方向上被 墙壁挡住，这个方法会返回 false，否则这个函数就会返回 true，机器人就会移动到相应的位 置。
请实现一个函数，来找到房间的面积。
注:房间的形状是不规则的，但是是由许多大小为 1x1 的格子组成的，比如下图表示的房子 里面，每一个 X 表示一个格子，房间的总面积是 10
X
XXXX 
XXXXX
```



深度优先、广度优先都可以

#### 方法一：采用深度优先遍历，借助Stack实现

```
# x*100+y的思路是为了将x和y的坐标信息融合到一个数字里，添加到stack中
# 取出的时候，用/和%剥离出x和y的坐标信息
# 其实，也可以将x和y放在一个集合，列表中或者作为一个对象实例，再添加到stack中，然后再取出来
```

```python
#Python3.6

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



def solution(stack, arr,x, y , unpassed_flag ,passed_flag):
    #初始化位置

    global map_size

    m = len(arr)
    n =len(arr[0])

    # 上下左右

    if x - 1 >= 0 and y >= 0 and arr[x - 1][y] == 'x':
        stack.push((x-1) * 100+y)
        arr[x - 1][y] = passed_flag
        map_size += 1

    if x + 1 < m and y >= 0 and arr[x + 1][y] == 'x':
        stack.push((x+1) * 100+y)
        arr[x + 1][y] = passed_flag
        map_size += 1

    if x >= 0 and y - 1 >= 0 and arr[x][y - 1] == 'x':
        stack.push(x * 100+(y-1))
        arr[x][y - 1] = passed_flag
        map_size += 1

    if x >= 0 and y + 1 < n and arr[x][y + 1] == 'x':
        stack.push(x * 100+(y+1))
        arr[x][y + 1] = passed_flag
        map_size += 1

    while not stack.isEmpty():
         size = stack.size()
         poll = stack.pop()
         print(poll)
         solution(stack, arr, int(poll/100), poll%100, 'x','p')




if __name__ ==  '__main__':

    stack = Stack()

    map_size = 0

    #已经走过
    passed = 'p'
    map_arr = [
            ['x',' ',' ', ' ',' '],
            ['x','x','x',' ' ,'x'],
            ['x','x','x','x' ,'x']
    ]
    solution(stack, map_arr,0,0,'x','p')

    print('房间大小为',map_size)


```

java版本

```Java
// x*100+y的思路是为了将x和y的坐标信息融合到一个数字里，添加到stack中
// 取出的时候，用/和%剥离出x和y的坐标信息
// 其实，也可以将x和y放在一个集合，列表中或者作为一个对象实例，再添加到stack中，然后再取出来
import java.util.Scanner;
import java.util.Stack;
public class Main {
    public static Stack<Integer> stack = null;
    public static int result = 0;
    //用来标记已经走过
    public static char used = 'u';
    public static void main(String[] args) {
        stack = new Stack<>();
        char[][] arr = {{'x',' ',' ', ' ',' '},{'x','x','x',' ','x'},{'x','x','x','x','x'}};
        fun(arr, 0, 0, 'x');
        System.out.println(result);
    }

    public static void fun(char[][] arr, int x, int y, char c) {
        int m = arr.length;
        int n =arr[0].length;
        // 遍历上下左右
        if (x - 1 >= 0 && y >= 0 && arr[x - 1][y] == 'x') {
            stack.push((x-1)*100+y);
            arr[x - 1][y] = used;
            result++;
        }
        if (x + 1 < m && y >= 0 && arr[x + 1][y] == 'x') {
            stack.push((x+1)*100+y);
            arr[x + 1][y] = used;
            result++;
        }
        if (x >= 0 && y - 1 >= 0 && arr[x][y - 1] == 'x') {
            stack.push(x*100+(y-1));
            arr[x][y - 1] = used;
            result++;
        }
        if (x >= 0 && y + 1 < n && arr[x][y + 1] == 'x') {
            stack.push(x*100+(y+1));
            arr[x][y + 1] = used;
            result++;
        }
        while (!stack.isEmpty()) {
            int size = stack.size();
            int poll = stack.pop();
            System.out.println(poll);
            fun(arr, poll/100, poll%100, 'x');
        }
    }
}
```



#### 方法二：采用广度优先遍历，借助Queue实现

```java
// x*100+y的思路是为了将x和y的坐标信息融合到一个数字里，添加到stack中
// 取出的时候，用/和%剥离出x和y的坐标信息
// 其实，也可以将x和y放在一个集合，列表中或者作为一个对象实例，再添加到stack中，然后再取出来
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    public static int result = 0;
    public static Queue<Integer> queue = new LinkedList<>();

    public static void main(String[] args) {
        char[][] arr = new char[][] { { 'x', ' ', ' ', ' ', ' ' }, { 'x', 'x', 'x', ' ', 'x' },
                { 'x', 'x', 'x', 'x', 'x' } };
        fun(arr, 0, 0, 'u');
        System.out.println(result);
    }

    public static void fun(char[][] arr, int x, int y, char used) {
        int m = arr.length;
        int n = arr[0].length;
        // 遍历上下左右
        if (x - 1 >= 0 && y >= 0 && arr[x - 1][y] == 'x') {
            queue.offer((x - 1) * 100 + y);
            arr[x - 1][y] = used;
            result++;
        }
        if (x + 1 < m && y >= 0 && arr[x + 1][y] == 'x') {
            queue.offer((x + 1) * 100 + y);
            arr[x + 1][y] = used;
            result++;
        }
        if (x >= 0 && y - 1 >= 0 && arr[x][y - 1] == 'x') {
            queue.offer(x * 100 + (y - 1));
            arr[x][y - 1] = used;
            result++;
        }
        if (x >= 0 && y + 1 < n && arr[x][y + 1] == 'x') {
            queue.offer(x * 100 + (y + 1));
            arr[x][y + 1] = used;
            result++;
        }
        while (!queue.isEmpty()) {
            Integer poll = queue.poll();
            fun(arr, poll / 100, poll % 100, used);
        }
    }
}

```

#### 方法三：借助move和递归，既不是深度优先也不是广度优先

```java
// 利用move和递归，往集合set中不断添加走过的坐标，最后计算几何set的大小
// 既不是广度优先，也不是深度优先
import java.util.*;

public class Main {

    static int x = 0, y = 0;//初始机器人位置

    public static boolean move(int dir) {//为了测试，自己写了一个move方法，比较片面
        // 0表示是房间可移动的位置，1表示墙壁障碍
        int[][] array = {//地图矩阵
                {0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1},
                {0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1},
                {0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1},
                {0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1},
                {0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1},
                {0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1}
        };
        int x_m = array.length;
        int y_m = array[0].length;
        switch (dir) {
            case 0:
                if (y + 1 >= y_m || array[x][y + 1] != 0) {
                    return false;
                }
                y++;
                break;
            case 1:
                if (x + 1 >= x_m || array[x + 1][y] != 0) {
                    return false;
                }
                x++;
                break;
            case 2:
                if (y - 1 < 0 || array[x][y - 1] != 0) {
                    return false;
                }
                y--;
                break;
            case 3:
                if (x - 1 < 0 || array[x - 1][y] != 0) {
                    return false;
                }
                x--;
                break;
            default:
                break;
        }
        return true;
    }

    //计算面积的函数
    public static int problem3(int x, int y, Set<String> set) {

        set.add(x + "," + y); //如果方向0的位置未到达过，且该位置没有障碍物，则移动到该位置。
        if (!set.contains(x + "," + (y + 1)) && move(0)) {
            problem3(x, y + 1, set);//迭代计算下一个位置的情况
            move(2);//回溯
        }
        if (!set.contains((x + 1) + "," + y) && move(1)) {
            problem3(x + 1, y, set);
            move(3);
        }
        if (!set.contains(x + "," + (y - 1)) && move(2)) {
            problem3(x, y - 1, set);
            move(0);
        }
        if (!set.contains((x - 1) + "," + y) && move(3)) {
            problem3(x - 1, y, set);
            move(1);
        }
        return set.size();
    }

    public static void main(String[] String) {
        Set<String> set = new HashSet<String>();
        System.out.println(problem3(0, 0, set));
        System.out.println(set);
    }
}

```



# 4.		

```
给定 K 个有序数组 a1, a2, ... , ak，求一个最小长度的区间 [s, t],使得每个数列 ai 都至少有 一个元素 aij 在这个区间内。如果有多个长度相等的区间满足条件，则选择起始点 s 最小的 那一个。
示例:
输入:
[1, 3, 5] [4, 8] [2, 5]
输出: [4, 5]
```

题目中举的例子较为简单，给一个一般的例子，和对应的解法：

最小区间原题

k个有序的数组，找到最小的区间范围使得这k个数组中，每个数组至少有一个数字在这个区间范围内。比如：

> - 数组1：[4, 10, 15, 24, 26]
> - 数组2：[0, 9, 12, 20]
> - 数组3：[5, 18, 22, 30]

最小的区间是[20, 24]，这个区间包含了数组1中的24，数组2中的20，数组3中的22

**手动推演一遍，就会发现采用小根堆解决，知道其中一个数组遍历完才结束。是最好解法**

```
分析

该题看起来还算比较简单，大家通常都会想到：为每一个数组设置一个遍历变量，选择最小值的数组，继续往后移动一位。由于是有k个数组，数组的数量有可能很多，所以如何去选择和替换最小的值，我们就会想到一个数据结构最小堆来维护最小的值。

解答方法：
初始化大小为k的最小堆，k个数字是每个数组中的最小值，设置变量maxValue记录k个数字中最大值，删除堆顶元素，将原堆顶元素对应的数组中下一个值加入到堆中，调整堆，并且记录当前区间范围（maxValue - minValue），重复执行直到某个数组所有值都被删除。


比如.
List 1: [4, 10, 15, 24, 26]
List 2: [0, 9, 12, 20]
List 3: [5, 18, 22, 30]


最小堆大小为3. 从三个数组中取最小值
Heap [0, 4, 5] maxValue 5
Range - 6


删除0 ，加入9
Heap [4, 9, 5] maxValue 9
Range - 6

删除4 ，加入10
Heap [5, 9, 10] maxValue 10
Range - 6

重复执行，最终得到结果

代码如下：
```

```c++
struct pn
{
    int n; /* belong to which array */
    int d; /* the data value */
    pn(int _n, int _d) { n = _n; d = _d; }
    pn(const pn& _pn) { n = _pn.n; d = _pn.d; }
};

inline void swap(pn& a, pn& b) { pn c = a; a = b; b = c; }

void adjust(int n, pn a[])
{
    int i = 0, max = 0;
    int l = 0, r = 0;
    for(i = n / 2; i >= 0; i--)
    {
        max = i;
        l = 2 * i + 1;
        r = 2 * i + 2;
        if(l < n && a[l].d > a[max].d) { max = l; }
        if(r < n && a[r].d > a[max].d) { max = r; }
        if(max != i) { swap(a[max], a[i]); }
    }
}

void heapsort(int n, pn a[])
{
    int i = 0;
    adjust(n, a);
    for(i = n - 1; i > 0; i--)
    {
        swap(a[0], a[i]);
        adjust(i, a);
    }
}

int main()
{
    int i = 0, j = 0;
    const int m = 3;
    const int n = 5;
    int ms = 0, me = 0;
    int ts = 0, te = 0;
    int a[m][n] = { {4, 10, 15, 24, 26}, {0, 9, 12, 20, 35}, {5, 18, 22, 30, 50} };
    int cur[m] = {1, 1, 1}; /* record the current positions of each array which haven't been used */
    pn heap[m] = {pn(0, a[0][0]), pn(1, a[1][0]), pn(2, a[2][0])};

    heapsort(m, heap);
    ms = heap[0].d;
    me = heap[m - 1].d;
    while(true)
    {
        heapsort(m, heap);
        ts = heap[0].d;
        te = heap[m - 1].d;
        /* if the current range is smaller than the minimum range */
        if(te - ts < me - ms) { ms = ts; me = te; }

        /* if the sub-array which the smallest element comes from hasn't to the end */
        if(cur[heap[0].n] != n)
        {
            heap[0].d = a[heap[0].n][cur[heap[0].n]];
            cur[heap[0].n] += 1;
        }
        else
        {
            break;
        }
    }
    cout << ms << endl;
    cout << me << endl;
    return 0;
}
```





# 二 简答题

## 1.请简述线程和进程的区别

### 总的来说

进程是具有一定独立功能的程序关于某个数据集合上的一次运行活动,进程是系统进行资源分配和调度的一个独立单位.

线程是进程的一个实体,是CPU调度和分派的基本单位,它是比进程更小的能独立运行的基本单位.线程自己基本上不拥有系统资源,只拥有一点在运行中必不可少的资源(如程序计数器,一组寄存器和栈),但是它可与同属一个进程的其他的线程共享进程所拥有的全部资源.

一个线程可以创建和撤销另一个线程;同一个进程中的多个线程之间可以并发执行.

线程是一个更加接近于执行体的概念，它可以与同进程中的其他线程共享数据，但拥有自己的栈空间，拥有独立的执行序列。

### 区别1

进程和线程的主要差别在于它们是不同的操作系统资源管理方式。进程有独立的地址空间，一个进程崩溃后，在保护模式下不会对其它进程产生影响，而线程只是一个进程中的不同执行路径。线程有自己的堆栈和局部变量，但线程之间没有单独的地址空间，**一个线程死掉就等于整个进程死掉，所以多进程的程序要比多线程的程序健壮**，但在**进程切换时，耗费资源较大，效率要差一些**。但对于一些要求**同时进行并且又要共享某些变量**的并发操作，**只能用线程，不能用进程。**

1) 简而言之,一个程序至少有一个进程,一个进程至少有一个线程.

2) 线程的划分尺度小于进程，使得多线程程序的并发性高。

3) 另外，进程在执行过程中拥有独立的内存单元，而多个线程共享内存，从而极大地提高了程序的运行效率。

4) 线程在执行过程中与进程还是有区别的。每个独立的线程有一个程序运行的入口、顺序执行序列和程序的出口。但是线程不能够独立执行，必须依存在应用程序中，由应用程序提供多个线程执行控制。

5) 从逻辑角度来看，多线程的意义在于一个应用程序中，有多个执行部分可以同时执行。但操作系统并没有将多个线程看做多个独立的应用，来实现进程的调度和管理以及资源分配。这就是进程和线程的重要区别。

### 区别2

通信方式不同

### 区别3

#### 优缺点不同

线程和进程在使用上各有优缺点：线程执行开销小，但不利于资源的管理和保护；而进程正相反。同时，线程适合于在SMP机器上运行，而进程则可以跨机器迁移。



# 2.请简述抢占式和非抢占式进程的区别

抢占式允许将逻辑上可继续运行的在运行过程暂停的调度方式 可防止单一进程长时间独占CPU 系统开销。

抢占式进程的开销更大。



非抢占式让进程运行直到结束或阻塞的调度方式。

非抢占式进程所需要的总时间就是所有进程的总时间的总和



# 3.两个不同的线程之间如何通信?两个进程之间呢? 

父子进程的派生是非常昂贵的，而且父子进程的通讯需要ipc或者其他方法来实现，比较麻烦。而线程的创建就花费少得多，并且同一进程内的线程共享全局存储区，所以通讯方便。

线程的缺点也是由它的优点造成的，主要是同步，异步和互斥的问题，值得在使用的时候小心设计。

### 线程之间通信

1.锁机制

包括互斥锁、条件变量、读写锁；

**互斥锁**提供了以排他方式防止数据结构被并发修改的方法。

**读写锁**允许多个线程同时读共享数据，而对写操作是互斥的。

**条件变量**可以以原子的方式阻塞进程，直到某个特定条件为真为止。对条件的测试是在互斥锁的保护下进行的。条件变量始终与互斥锁一起使用。

2.信号量

包括无名线程信号量和命名线程信号量

3.信号：类似进程间的信号处理



线程间的通信目的主要是用于线程同步，所以线程没有像进程通信中的用于数据交换的通信机制。



### 进程之间通信（进程间通信Interprocess Communication ——IPC）

1.信号：信号是一种比较复杂的通信方式，用于通知接收进程某个事件已经发生。

2.信号量：信号量是一个计数器，可以用来控制多个进程对共享资源的访问。它常作为一种锁机制，防止某进程正在访问共享资源时，其他进程也访问该资源。因此，主要作为进程间以及同一进程内不同线程之间的同步手段。

3.消息队列：消息队列是由消息的链表，存放在内核中并由消息队列标识符标识。消息队列克服了信号传递信息少、管道只能承载无格式字节流以及缓冲区大小受限等缺点。

4.共享内存：共享内存就是映射一段能被其他进程所访问的内存，这段共享内存由一个进程创建，但多个进程都可以访问。共享内存是最快的 IPC 方式，它是针对其他进程间通信方式运行效率低而专门设计的。**它往往与其他通信机制，如信号量，配合使用，来实现进程间的同步和通信**。

5.管道：管道是一种半双工的通信方式，数据只能单向流动，而且只能在具有亲缘关系的进程间使用。进程的亲缘关系通常是指父子进程关系。

6.有名管道：有名管道也是半双工的通信方式，但是它允许无亲缘关系进程间的通信。

7.套接字：与其他通信机制不同的是，它可用于不同机器间的进程通信。

## 4.如何实现一个线程安全的 hash map?

Java HashMap 是非线程安全的。在多线程条件下，容易导致死循环，具体表现为CPU使用率100%。

以下方法保证安全： 

- 使用 java.util.Hashtable 类，此类是线程安全的。
- 使用 java.util.concurrent.ConcurrentHashMap，此类是线程安全的。
- 使用 java.util.Collections.synchronizedMap() 方法包装 HashMap object，得到线程安全的Map，并在此Map上进行操作。
- 自己在程序的关键方法或者代码段加锁，保证安全性





