## 10个不为人知的 Python 冷知识

### **1. 省略号也是对象**

`...` 这是省略号，在Python中，一切皆对象。它也不例外。

在 Python 中，它叫做 Ellipsis 。

在 Python 3 中你可以直接写…来得到这玩意。

```
>>> ...
Ellipsis
>>> type(...)
<class  ellipsis >
```

而在 2 中没有…这个语法，只能直接写Ellipsis来获取。

```
>>> Ellipsis
Ellipsis
>>> type(Ellipsis)
<type  ellipsis >
>>>
```

它转为布尔值时为真

```
>>> bool(...)
True
```

最后，这东西是一个单例。

```
>>> id(...)
4362672336
>>> id(...)
4362672336
```

这东西有啥用呢？据说它是Numpy的语法糖，不玩 Numpy 的人，可以说是没啥用的。

在网上只看到这个 用 `...` 代替 pass ，稍微有点用，但又不是必须使用的。

```
try:
    1/0
except ZeroDivisionError:
    ...
```

### 2. 类首字母不一定是大写

在正常情况下，我们所编写的所见到的代码，好像都默许了类名首字母大写，而实例用小写的这一准则。但这并不是强制性的，即使你反过来的也没有关系。

但有一些内置的类，首字母都是小写，而实例都是大写。

比如 bool 是类名，而 True，False 是其实例；
比如 ellipsis 是类名，Ellipsis是实例；
还有 int，string，float，list，tuple，dict 等一系列数据类型都是类名，它们都是小写。

### 3. 增量赋值的性能更好

诸如 `+=` 和 `*=` 这些运算符，叫做 增量赋值运算符。

这里使用用 += 举例，以下两种写法，在效果上是等价的。

```
# 第一种
a = 1 ; a += 1

# 第二种
a = 1; a = a + 1
```

`+=` 其背后使用的魔法方法是 __iadd__，如果没有实现这个方法则会退而求其次，使用 __add__ 。

这两种写法有什么区别呢？

用列表举例 a += b，使用 __iadd__ 的话就像是使用了a.extend(b),如果使用 __add__ 的话，则是 a = a+b,前者是直接在原列表上进行扩展，而后者是先从原列表中取出值，在一个新的列表中进行扩展，然后再将新的列表对象返回给变量，显然后者的消耗要大些。

所以在能使用增量赋值的时候尽量使用它。

### 4. and 和 or 的取值顺序

and 和 or 是我们再熟悉不过的两个逻辑运算符。而我们通常只用它来做判断，很少用它来取值。

如果一个or表达式中所有值都为真，Python会选择第一个值，而and表达式则会选择第二个。

```python
>>> a = 2 or 3
>>> a
2
>>> 2 or 3
2
>>> 2 and 3
3
>>> a = 2 and 3
>>> a
3
>>> a = True and 3
>>> a
3
>>> a = False and 3
>>> a
False
>>> a = False or 3
>>> a
3
>>> False or 3
3
>>> False and 3
False
>>> True or 3
True

```

###  5. 如何修改解释器提示符

这个当做今天的一个小彩蛋吧。应该算是比较冷门的，估计知道的人很少了吧。

正常情况下，我们在 终端下 执行Python 命令是这样的。

```python
>>> for i in range(2):
...     print (i)
...
0
1
```

你是否想过 `>>>` 和 `...` 这两个提示符也是可以修改的呢？

```python
>>> import sys                      
>>> sys.ps1                         
 >>>                                
>>> sys.ps2                         
 ...                                
>>>                                 
>>> sys.ps2 =  ................                  
>>> sys.ps1 =  Python编程时光>>>        
Python编程时光>>>for i in range(2):     
................    print (i)                    
................                                 
0                                   
1         
```

### 06. 默认参数最好不为可变对象

函数的参数分三种

- 可变参数
- 默认参数
- 关键字参数

这三者的具体区别，和使用方法在 廖雪峰的教程 里会详细的解释。这里就不搬运了。

今天要说的是，传递默认参数时，新手很容易踩雷的一个坑。

先来看一个示例

```python
def func(item, item_list=[]):
    item_list.append(item)
    print(item_list)

func( iphone )
func( xiaomi , item_list=[ oppo , vivo ])
func( huawei )
```

在这里，你可以暂停一下，思考一下会输出什么？

思考过后，你的答案是否和下面的一致呢

```python
[ iphone ]
[ oppo ,  vivo ,  xiaomi ]
[ iphone ,  huawei ]
```

如果是，那你可以跳过这部分内容，如果不是，请接着往下看，这里来分析一下。

**Python 中的 def 语句在每次执行的时候都初始化一个函数对象，这个函数对象就是我们要调用的函数，可以把它当成一个一般的对象，只不过这个对象拥有一个可执行的方法和部分属性。**

**对于参数中提供了初始值的参数，由于 Python 中的函数参数传递的是对象，也可以认为是传地址，在第一次初始化 def 的时候，会先生成这个可变对象的内存地址，然后将这个默认参数 item_list 会与这个内存地址绑定。在后面的函数调用中，如果调用方指定了新的默认值，就会将原来的默认值覆盖。如果调用方没有指定新的默认值，那就会使用原来的默认值。**

![python默认参数为可变对象](../images/python默认参数为可变对象.jpeg)

### 07. 访问类中的私有方法

大家都知道，类中可供直接调用的方法，只有公有方法（protected类型的方法也可以，但是不建议）。也就是说，类的私有方法是无法直接调用的。

这里先看一下例子

```python
class Kls():
    def public(self):
        print( Hello public world! )

    def __private(self):
        print( Hello private world! )

    def call_private(self):
        self.__private()

ins = Kls()

# 调用公有方法，没问题
ins.public()

# 直接调用私有方法，不行
ins.__private()

# 但你可以通过内部公有方法，进行代理
ins.call_private()
```

既然都是方法，那我们真的没有方法可以直接调用吗？

当然有啦，只是建议你千万不要这样弄，这里只是普及，让你了解一下。

```python
# 调用私有方法，以下两种等价
ins._Kls__private()
ins.call_private()    
```

### 08. 时有时无的切片异常

这是个简单例子

```python
my_list = [1, 2, 3, 4, 5]
print(my_list[5])   
```

执行一下，和我们预期的一样，会抛出索引异常。

```python
Traceback (most recent call last):
  File "F:/Python Script/test.py", line 2, in <module>
    print(my_list[5])
IndexError: list index out of range   
```

但是今天要说的肯定不是这个，而是一个你可能会不知道的冷知识。

来看看，如下这种写法就不会报索引异常，执行my_list[5:]，会返回一个新list：[]。

```python
my_list = [1, 2, 3]
print(my_list[5:]) 
```

### 09. 哪些情况下不需要续行符

在写代码时，为了代码的可读性，代码的排版是尤为重要的。

为了实现高可读性的代码，我们常常使用到的就是续行符 ``。

```python
>>> a =  talk is cheap,
...      show me the code.
>>>
>>> print(a)
talk is cheap,show me the code.
```

那有些情况下，是不需要写续行符的呢？

经过总结，在这些符号中间的代码换行可以省略掉续行符：`[]`,`()`,`{}`

```python
>>> my_list=[1,2,3,
...          4,5,6]

>>> my_tuple=(1,2,3,
...           4,5,6)

>>> my_dict={"name": "MING",
...          "gender": "male"}
```

另外还有，在多行文本注释中 `  ` ，续行符也是可以不写的。

```python
>>> text =    talk is cheap,
...           show me the code
```

上面只举了一些简单的例子。

但你要学会举一反三。一样的，在以下这些场景也同样适用

- 类，和函数的定义。
- 列表推导式，字典推导式，集合推导式，生成器表达式

### 10. Py2 也可以使用 print()

我相信应该有不少人，思维定式，觉得只有 Py3 才可以使用 print()，而 Py2 只能使用print   。

今天，小明要为 Py2 正名一次。

在Python 2.6之前，只支持

```
print "hello"
```

在Python 2.6和2.7中，可以支持如下三种

```python
print "hello"
print("hello")
print ("hello")
```

在Python3.x中，可以支持如下两种

```python
print("hello")
print ("hello")
print         ("hello")
print "hello"
print          "hello"
```







