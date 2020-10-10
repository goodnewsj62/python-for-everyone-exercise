
#*names,phone,email = ('goodnews','john','osonwa','0903030303' ,'good@email.com')


#print(names)
#print(phone)
#print(email)

#records = [
#    ('foo',1,2),
#    ('bar','hello'),
#     ('foo',3,4)
#]

#def do_foo(x,y):
#    print('foo',x,y)

#def do_bar(s):
#    print('bar',s)


#for tag,*arg in records:
#    print(tag)
 #   print(arg)

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []
    def __repr__(self):
        return 'Node({!r})'.format(self._value)
    def add_child(self, node):
        self._children.append(node)
    def __iter__(self):
        return self._children.__iter__()
    def get_child(self):
        return self._children
# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    print(root.get_child())
    for c in root:
        print(c)
# Outputs