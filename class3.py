'''
1. Set and its property
A set is a collection which is unordered, unchangeable*, and unindexed.
Note: Set items are unchangeable, but you can remove items and add new items.
Once a set is created, you cannot change its items, but you can add new items.
'''
set = {"A", "B", "C", "D", "E"}

while True:
    print("=================================================\n")
    print("This is set A: ", set)
    print("Set A data:")
    for r in set:
        print("Value: ",r)

    print("Find set A value")
    a = input("Value: ")
    print(a in set)
    print("\n")
    
    # Add items
    b = input("Add new item to set A: ")
    set.add(b)
    print("Set A new item: ", set)
    setb = {"1", "2", "3", "4"}
    print("Set B: ", setb)
    print("Adding set B to set A")
    set.update(setb)
    print("Combined set: ", set)

    # Remove set value
    '''Note: If the item to remove does not exist, remove() will raise an error.
    Note: If the item to remove does not exist, discard() will NOT raise an error.
    '''
    c = input("\nRemove value: ")
    set.remove(c)
    print("New set: ", set)
    c = input("\nDiscard value: ")
    set.discard(c)
    print("New set: ", set)

    '''
    2. Tuple and its property
    Tuples are used to store multiple items in a single variable.
    Tuple items are ordered, unchangeable, and allow duplicate values.
    Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
    '''
    tupleA = ("One", "Two", "Three", "Four")
    print("Tuple A: ", tupleA)

    '''
    Change Tuple Value
    Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
    But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
    '''
    tupleToList = list(tupleA)
    tupleToList.append("Five")
    tupleToList.append("Six")
    tupleA = tuple(tupleToList)
    print("Tuple B: ", tupleA)