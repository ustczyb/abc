# coding=utf-8
"""
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素x推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
"""
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.m_stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        n = len(self.m_stack)
        if n == 0:
            self.m_stack.append(x)
        else:
            self.m_stack.append(min(self.m_stack[n - 1], x))


    def pop(self):
        """
        :rtype: void
        """
        self.m_stack.pop()
        return self.stack.pop()


    def top(self):
        """
        :rtype: int
        """
        n = len(self.stack)
        return self.stack[n - 1]


    def getMin(self):
        """
        :rtype: int
        """
        n = len(self.m_stack)
        return self.m_stack[n - 1]



        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()