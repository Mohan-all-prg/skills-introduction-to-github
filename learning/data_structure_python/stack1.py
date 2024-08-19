#the basic of stack is first in last out / last in first out
"""stack = []
def push():
    if len(stack)==c:
        print("max num of element is reached")
    else:
       a=input("enter the element=")
       stack.append(a)
       print(stack)
def pop_ele():
    if not stack:
        print("there is no element to remove")
    else:
        print("removed element=",stack.pop())
    print(stack)

c=int(input("How many elements to get in the stack="))
while True:
    print("enter the num to get push:1 or pop:2 or stop:3 ")
    b=int(input("Enter="))
    if(b==1):
        push()
    elif(b==2):
        pop_ele()
    elif(b==3):
        break
    else:
        print("Enter the correct operation or num to get output")"""


#the module method for getting stack
"""import collections
a=collections.deque()
to get input we use
append()
to take
pop()"""

"""import queue
a=queue.LifoQueue(4)
to get input we use
put()
to take
get()
we can use time when it get false
get(timeout=2)"""


