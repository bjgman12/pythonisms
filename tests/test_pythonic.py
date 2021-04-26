from pythonic import __version__

from pythonic.nisms import Node, LinkedList


def test_version():
    assert __version__ == '0.1.0'


def test_for_in():
    ll = LinkedList(Node('One'))
    ll.append('Two')
    temp = []

    for item in ll:
        temp.append(item)

    assert temp == ['One','Two']

def test_comprehension():
    ll = LinkedList(Node('One'))
    ll.append('Two')

    c_locked = [item.upper() for item in ll]

    assert c_locked == ['ONE','TWO']

def test_list_cast():
    
    nums = ['one','two']

    ll = LinkedList(nums)

    assert len(ll) == 2


