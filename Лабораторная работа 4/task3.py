def delete(list_, index=None):
    if index == None:
        d = list_[:-1]
    elif index == 0:
        d = list_[1:]
    else:
        d1 = list_[:index]
        d2 = list_[index+1:]
        d = d1 + d2
    return d
print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
