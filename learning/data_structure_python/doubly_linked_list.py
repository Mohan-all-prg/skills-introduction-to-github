class Node:
    def __init__(store,data):
        store.data=data
        store.nref=None
        store.pref=None

class doubly_linked_list:
    def __init__(store):
        store.head=None
    def Head_reverse(store):
        if store.head is None:
            print("linke list is empty")
        else:
            n=store.head
            while n is not None:
                print(n.data,end="-->")
                n=n.nref

    def Head(store):
        print()
        if store.head is None:
            print("linke list is empty")
        else:
            n=store.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data,end="-->")
                n=n.pref
    def add_begin(store,data):
        new_node=Node(data)
        if store.head is None:
            store.head = new_node
        else:
            new_node.nref=store.head
            store.head.pref=new_node
            store.head=new_node
    def add_end(store,data):
        new_node=Node(data)
        if store.head is None:
            store.head=new_node
        else:
            n=store.head
            while n.nref is not None:
                n=n.nref
            n.nref=new_node
            new_node.pref=n
    def add_after(store,data,a):
        new_node=Node(data)
        if store.head is None:
            print("linkedlist is empty")
            return
        n=store.head
        while n is not None: 
             if n.data is a:
                 break
             n=n.nref
             n.nref=new_node
        new_node.pref=n.pref

        


Data=doubly_linked_list()
Data.add_begin(10)
Data.add_begin(20)
Data.add_begin(40)
Data.add_end(30)
Data.add_after(100,20)
Data.Head_reverse()
Data.Head()

