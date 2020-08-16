# 计算器类，包含加减乘除四个方法
class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if(b == 0):
            return '除数不能为0'
        else:
            return a / b
