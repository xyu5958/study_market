# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 13:24:11 2019
gcd_euclidean_algorithm.py
@author: yuxun
"""

import numpy as np

# gcd(a, b)
def gcd(a, b):
    """
    辗转相除迭代法计算两个数的最大公约数，计算原理(a>b时)为：
    gcd(a, b) = gcd(b, a%b) = ... = gcd(c, 0)
    最后一个式子中的c，即为a和b的最大公约数。
    Inputs:
        a, b: 两个求最大公约数的输入数
    Outputs:
        c: 最大公约数    
    """
    # 先求出a和b中较大数maxnum和较小数minnum
    maxnum = max(a, b)
    minnum = min(a, b)
    # 然后进行迭代，迭代结束条件为minnum==0
    if minnum == 0:
        return maxnum
    else:
        return gcd(minnum, maxnum%minnum)

# gbs(a, b)
def gbs(a, b):
    """
    求两个数的最小公倍数，计算原理是先求出它们的最大公约数，那么：
    gbs(a, b) = a*b/c
    Inputs:
        a, b: 两个求最小公倍数的输入数
    Outputs:
        c: 最小公倍数
    """
    c = gcd(a, b)
    return int(a*b/c)

# canMeasureWater(x, y, z)
def canMeasureWater(x, y, z):
    """
    leetcode_365的求解函数
    :type x: int
    :type y: int
    :type z: int
    :rtype: bool
    """
    if z <= (x + y):  # 待测量的z不能超过(x+y)，否则装不下
        gcd_x_y = gcd(x, y)
        if z%gcd_x_y == 0:
            return True
        else:
            return False
    else:
        return False

# gcd_integer_solution
def gcd_integer_solution(maxnum, minnum):
    """
    求一个形如px+qy=gcd(p,q)(p、q均为正整数)方程的整数解的函数。
    Inputs:
        maxnum, minnum: 方程左边的系数，注意这里要区分大小
    Outputs:
        x, y: 与maxnum和minnum对应的未知数的解
    """
    # 递归终止条件: 较小值等于0时
    if minnum == 0:
        return 1, 0  # 返回(1,0)——当方程右侧是gcd(p,q)时，最后的解肯定是(1,0)
    # 递归的过程：调用函数取出(n+1)轮的解(x,y)，利用递推公式计算n轮的解(x,y)并return它
    else:
        x, y = gcd_integer_solution(minnum, maxnum%minnum)  # (p,q)-->(q,p%q)的递归过程
        a = y  # 将(n+1)轮的解转换为n轮，引入a是避免交叉赋值出错
        y = x - (maxnum//minnum)*a
        x = a
        return x, y

# integer_solution
def integer_solution(p, q, c):
    """
    求一个形如px+qy=c(p、q均为正整数,c为整数)方程的整数解的函数。
    Inputs:
        p, q: 方程左边的系数，输入正整数
        c: 方程右边的系数
    Outputs:
        x, y: 方程的解
    """     
    gcd_p_q = gcd(p, q)
    # 只有在方程有解时才求解
    if c%gcd_p_q == 0:
        # 首先求解px+qy=gcd(p,q)
        maxnum = max(p, q)
        minnum = min(p, q)
        max_gcd, min_gcd = gcd_integer_solution(maxnum, minnum)
        # 然后转换为px+qy=c=gcd(p,q)*(c/gcd(p,q))的解
        max_coef, min_coef = max_gcd*(c/gcd_p_q), min_gcd*(c/gcd_p_q)
        x = (p>=q)*max_coef + (p<q)*min_coef  # x和y依据p、q大小来取值
        y = (p>=q)*min_coef + (p<q)*max_coef       
        return x, y
    # 方程无解时返回两个None
    else:
        return None, None




if __name__ == '__main__':
    # test of gcd():
    print(gcd(12, 18))
    print(gcd(7890, 123456))
    # test1 of canMeasureWater():
    print('test of canMeasureWater')
    x, y, z = 3, 5, 4
    print(f'Input: x={x}, y={y}, z={z}')
    print(f'Can Measure?--Answer: {canMeasureWater(x, y, z)}')
    # test2 of canMeasureWater():
    print('test of canMeasureWater')
    x, y, z = np.random.randint(1, 100, 3)
    print(f'Input: x={x}, y={y}, z={z}')
    print(f'Can Measure?--Answer: {canMeasureWater(x, y, z)}')
    # test1 of integer_solution():
    print('test of integer_solution')
    p, q, c = 5, 3, 4
    x, y = integer_solution(p, q, c)
    print(f'The equation is: {p}x + {q}y = {c}')
    print(f'Solution: x={x}; y={y}')
    # test2 of integer_solution():
    print('test of integer_solution')
    p, q, c = np.random.randint(1, 100, 3)
    x, y = integer_solution(p, q, c)
    print(f'The equation is: {p}x + {q}y = {c}')
    print(f'Solution: x={x}; y={y}')
    
    