class Node:
    def __init__(store,data):
        store.data=data
        store.ref=None

class Linkedlist:
    def __init__(store):
        store.head=None
    def Head(store):
        if store.head is None:
            print("linked list is empty")
        else:
            n=store.head
            while n is not None:
                print(n.data,end="-->")
                n=n.ref
    def add_begin(store,data):
            new_node=Node(data)
            new_node.ref=store.head
            store.head=new_node
    def add_end(store,data):
        new_node=Node(data)
        if store.head is None:
            store.head=new_node
        else:
            n=store.head
            while n.ref is not None:
                n=n.ref
        n.ref=new_node
    def add_after(store,data,a):
        new_node=Node(data)
        if store.head is None:
            print("Linkedlist  is empty")
            return
        n=store.head
        while n.ref is not None:
            if n.data is a:
                break
            n=n.ref
        new_node.ref=n.ref
        n.ref=new_node
    def add_before(store,data,a):
        new_node=Node(data)
        if store.head is None:
            print("likedlist is empty")
            return
        if store.head.data is a:
            new_node.ref=store.head
            store.head=new_node
            return
        n=store.head
        while n.ref is not None:
            if n.ref.data is a:
                break
            n=n.ref
        new_node.ref=n.ref
        n.ref=new_node
    def delete(store,a):
        print()
        if store.head is None:
            print("linkedlist is empty")
        elif store.head.data is a:
            store.head=store.head.ref
        else:
            n=store.head
            while n is not None:
                if n.ref.data is a:
                    break
                n=n.ref
            n.ref=n.ref.ref


Data=Linkedlist()
Data.add_begin(10)
Data.add_begin(20)
Data.add_end(30)
Data.add_end(40)
Data.add_after(50,10)
Data.add_before(100,20)
Data.add_before(101,40)
Data.Head()
Data.delete(100)
Data.delete(10)
Data.Head()
