def merge_sorted_lists(list1, list2):
	list1.extend(list2)
	for i  in range(len(list1)):
		for ii in range(i+1, len(list1)):
			if list1[i] > list1[ii]:
				list1[i], list1[ii] = list1[ii], list1[i]
	sorting(list1)
	return list1

def sorting(list1):
	for i in list1:
		while list1.count(i) > 1:
			list1.remove(i)
	return list1

list1 = [1, 3, 3, 13, 5, 5]
list2 = [2, 4, 7, 9]
merged = merge_sorted_lists(list1, list2)
print(merged)
