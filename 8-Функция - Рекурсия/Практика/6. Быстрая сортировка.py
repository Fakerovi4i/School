def fast_sort(li_st):
	if len(li_st) < 2:
		return li_st
	else:
		base = li_st[0]
		middle = [i for i in li_st if i == base]
		less = [i for i in li_st[0:] if i < base]
		grater = [i for i in li_st[0:] if i > base]

	return fast_sort(less) + middle + fast_sort(grater)

orig_list = [5, 8, 9, 4, 2, 9, 1, 8]

print(fast_sort(orig_list))