
class bs(object):
    """description of class"""

    list = [3, 2, 4, 1, 5, 45, 21, 9, 8, 10, 11, 34, 100, 98, 22, 17]           

    print("Before sort")
    print list

    for w in range(len(list)-1):
        for y in range(len(list)-1):            
            if list[y] > list[y+1]:
                temp = list[y]
                list[y] = list[y+1]
                list[y+1] = temp       

    print("After sort")
    print list

    input = raw_input("done")