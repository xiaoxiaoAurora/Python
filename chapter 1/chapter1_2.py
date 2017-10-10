
# coding: utf-8

# In[1]:


'''
由用户从键盘给定任意正整数n，打印1+2+3+...n的和

'''


n = int(input('Please Enter The Number:'))

total = 0
i = 0

while i <= n:
    total = total + i
    i+=1
print('1+2+3+...+n = ',total)


# In[2]:


'''
2.8 实践与练习

练习1：仿照任务2完整代码，打印n!。

'''

n = int(input('Please Enter The Number:'))

multi = 1
i = 1

while i<=n:
    multi = multi*i
    i+=1
    
    
print('n! = ',multi)


# In[1]:


'''
实践1：键入如下代码并观察执行结果。


'''


name = input('请输入你的姓名，以回车结束。')
print('你好!', name)

n = int(input('请输入一个正整数，以回车结束。'))
m = int(input('请输入一个正整数，以回车结束。'))

print('两个数的和是：', m+n)
print('再见！', name)



# In[8]:


'''
练习2：仿照实践1，写出由用户指定整数个数，并由用户输入多个整数，并求和的代码。

'''
# 疑问：限制个数，如果输入的个数大于要求的个数，自动选取前n个数


n = int(input('请输入整数个数：'))

list = []

str = input("请输入数值，用空格隔开,以回车结束:")  
list1 = str.split(" ")

total = 0  
i = 0
while i<=len(list1)+1:
    list.append(int(list1.pop()))
    i+=1

def sum(total):
    "对列表的数值求和"  

    for x in list:
        total = total + x
    return total

print('输入的数字之和是：',sum(total))

    


# In[1]:


'''
练习2：仿照实践1，写出由用户指定整数个数，并由用户输入多个整数，并求和的代码。

'''
# 疑问：限制个数，如果输入的个数大于要求的个数，自动选取前n个数   已解决


n = int(input('请输入整数个数：'))


total = 0  
i = 0
while i<n:
    
    m = int(input('请输入一个整数：'))
    total = total + m
    i+=1

print('输入的数字之和是：',total)


# In[7]:


'''
练习3：用户可以输入的任意多个数字，直到用户不想输入为止。

'''

num = input('请输入一个整数：')

while num != '#':
    num = input('请输入一个整数：')
        


# In[ ]:


'''
练习4：用户可以输入的任意多个数字，直到输入所有数字的和比当前输入数字小，且输入所有数字的积比当前输入数字的平方大。

	Question:不能实现满足条件后退出循环

'''

num_1 = int(input('请输入第一个整数：'))
num_next = int(input('请输入下一个整数：'))

total = num_1
multi = num_1

total = total + num_next
multi = multi * num_next

while (total>num_next) or (multi<(num_next**2)):
    
    num_next = int(input('请输入下一个整数：'))
    
    total = total + num_next
    multi = multi * num_next
    
print('total=',total)
print('multi=',multi)
            
        

