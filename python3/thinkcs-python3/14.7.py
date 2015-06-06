#14.7
'''
Lets assume we have two sorted lists. Exercise your algorithmic skills by adapting the merging algorithm pattern for each of these cases:

Return only those items that are present in both lists.
Return only those items that are present in the first list, but not in the second.
Return only those items that are present in the second list, but not in the first.
Return items that are present in either the first or the second list.
Return items from the first list that are not eliminated by a matching element in the second list. In this case, an item in the second list “knocks out” just one matching item in the first list. This operation is sometimes called bagdiff. For example bagdiff([5,7,11,11,11,12,13], [7,8,11]) would return [5,11,11,12,13]
'''

def merge_present_both(list1, list2):
    result = []
    l1i = 0
    l2i = 0
    while True:
        if list1[l1i] == list2[l2i]:
            result.append(list1[l1i])
            l1i += 1
            l2i += 1
        elif list1[l1i] < list2[l2i]:
            l1i += 1
        else:
            l2i += 1

        if l1i >= len(list1):
            return result
        if l2i >= len(list2):
            return result

def merge_present_first_not_second(list1, list2):
    result = []
    l1i = 0
    l2i = 0
    while True:
        if list1[l1i] == list2[l2i]:
            l1i += 1
            l2i += 1
        elif list1[l1i] < list2[l2i]:
            result.append(list1[l1i])
            l1i += 1
        else:
            #result.append(list2[l2i])
            l2i += 1

        if l1i >= len(list1):
            #result.extend(list2[l2i:])
            return result
        if l2i >= len(list2):
            result.extend(list1[l1i:])
            return result

def merge_present_second_not_first(list1, list2):
    result = []
    l1i = 0
    l2i = 0
    while True:
        if list1[l1i] == list2[l2i]:
            l1i += 1
            l2i += 1
        elif list1[l1i] < list2[l2i]:
            l1i += 1
        else:
            result.append(list2[l2i])
            l2i += 1

        if l1i >= len(list1):
            result.extend(list2[l2i:])
            return result
        if l2i >= len(list2):
            return result

def merge_present_first_or_second(list1, list2):
    result = []
    l1i = 0
    l2i = 0
    while True:
        if list1[l1i] == list2[l2i]:
            result.append(list1[l1i])
            l1i += 1
            l2i += 1

        if list1[l1i] < list2[l2i]:
            result.append(list1[l1i])
            l1i += 1
        else:
            result.append(list2[l2i])
            l2i += 1

        if l1i >= len(list1):
            result.extend(list2[l2i:])
            return result
        if l2i >= len(list2):
            result.extend(list1[l1i:])
            return result

def bagdiff(list1, list2):
    result = []
    l1i = 0
    l2i = 0
    while True:
        if list1[l1i] == list2[l2i]:
            l1i += 1
            l2i += 1
        if list1[l1i] < list2[l2i]:
            result.append(list1[l1i])
            l1i += 1
        else:
            l2i += 1
        if l1i >= len(list1):
            return result
        if l2i >= len(list2):
            result.extend(list1[l1i:])
            return result

list1 = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,40]
list2 = [3,6,9,12,15,18,21,24,27,30,33,36,39]

print(merge_present_both(list1, list2))
print(merge_present_first_not_second(list1, list2))
print(merge_present_second_not_first(list1, list2))
print(merge_present_first_or_second(list1,list2))
print(bagdiff(list1,list2))