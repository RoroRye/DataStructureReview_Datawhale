"""
数组：
    读取元素时间复杂度为0(1)
    添加元素时间复杂度为0(n)
    删除元素时间复杂度为0(n)
"""

class MyArray:
    def __init__(self, MAXSIZE=20):
        """存储空间初始分配量"""
        self._MAXSIZE = MAXSIZE
        self._length = 0
        self._data = [None] * self._MAXSIZE

    def __GetElem__(self, item):
        """返回索引值"""
        return self._data[item]

    def GetLength(self):
        """返回有效元素的个数"""
        return self._length
    
    def GetMAXSIZE(self):
        """返回数组的容量"""
        return self._MAXSIZE

    def isEmpty(self):
        """判断数组是否为空"""
        return self._size == 0
    
    def _resize(self, NewMAXSIZE):
        """放缩容量"""
        ArrayNew = MyArray(NewMAXSIZE)
        for i in range(self._size):
            ArrayNew.ArrayInsert(i, self._data[i])
        self._MAXSIZE = NewMAXSIZE
        self._data = ArrayNew._data

    def ArrayInsert(self, index, elem):
        """
        index: 添加的元素所在的索引
        elem:  所要添加的元素
        """
        if self._size == self._MAXSIZE:  #数组已满
            self._resize(self._MAXSIZE * 2)
        if index < 0 or index > self._size:
            raise Exception('Insert Failed. Require 0 <= index <= self._length')

        for i in range(self._length - 1, index-1, -1):
            self._data[i+1] = self._data[i]
        
        self._data[index] = elem
        self._size += 1
    
    def ArrayDelete(self, index):
        """
        删除索引index处的元素
        返回该索引元素的值
        """
        if index < 0 or index > self._size:
            raise Exception('Insert Failed. Require 0 <= index <= self._length')
        elem = self._data[index]
        for i in range(index+1, self._size):
            self._data[i-1] = self._data[i]
        self._size -=1
        self._data[self._size] = None
        return elem
    
