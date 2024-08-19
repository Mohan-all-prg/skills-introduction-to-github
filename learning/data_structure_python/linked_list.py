"""#to get data in the begining
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class Linkedlist:
    def __init__(self):
        self.head=None
    def Head(self):
        if self.head is None:
            print("no value inside the node")
        else:
            n=self.head
            while n is not None:
                print(n.data,end="&")
                n=n.ref
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
    def add_after(self,data,a):
        n=self.head
        while n is not None:
            if a==n.data:
                break
            n=n.ref
        if n is None:
            print("node is not present")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
        

Data=Linkedlist()
Data.add_end(100)
Data.add_begin(20)
Data.add_begin(30)
Data.add_after(200,30)
Data.Head()"""


class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class Linkedlist:
    def __init__(self):
        self.head=None
    def Head(self):
        if self.head is None:
            print("no value inside the Node")
        else:
            n=self.head
            while n is not None:
                print(n.data,end="-->")
                n=n.ref
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
           n=self.head
           while n.ref is not None:
               n=n.ref
        n.ref=new_node
    def add_after(self,data,a):
        n=self.head
        while n is not None:
            if a==n.data:
                 break
            n=n.ref
        if n is None:
            print("Node is empty")
        else:
          new_node=Node(data)
          new_node.ref=n.ref
          n.ref=new_node
    def add_before(self,data,b):
        if self.head is None:
            print("no value in the Node")
            return
        if self.head.data is b:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data is b:
                break
            n=n.ref
        if n.ref is None:
            print("Node is empty")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
    def delete(self):
        if self.head is None:
            print("linkedlist is empty")
            return
        print("\nto delete first node press 1 or to delete any node after first node press 2")
        b=int(input())
        if b is 2:
           a=int(input("enter node to delete="))
           n=self.head
           while n.ref is not None:
                  if n.ref.data is a:
                      break
                  n=n.ref
           if n.ref is None:
               print("nnot")
           else:
             n.ref=n.ref.ref
        if b is 1:
            c=int(input("enter the first node to delete="))
            if self.head.data is c:
               self.head=self.head.ref

        
Data=Linkedlist()
Data.add_begin(10)
Data.add_begin(20)
Data.add_begin(30)
Data.add_end(40)
Data.add_end(50)
Data.add_before(100,30)
Data.Head()
Data.delete()
Data.Head()














            
            






































