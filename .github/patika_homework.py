# 1- Bir listeyi düzleştiren (flatten) fonksiyon yazın

list1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flatten_list = []
def flatten(l):
    for sublist in l:
        if type(sublist) == list:
            flatten(sublist)
        else:
            flatten_list.append(sublist)
    return flatten_list

print(flatten(list1))

# ---------------------------------------------------
# 2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın.

list2 = [[1, 2], [3, 4], [5, 6, 7]]  

def reverse_list(l):
    l.reverse()
    for sublist in l:
        if type(sublist) == list:
            reverse_list(sublist)

reverse_list(list2)
print(list2)
