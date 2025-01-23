import copy

site = {
'html': {
'head': {
'title': 'Куплю/продам телефон недорого'
},
'body': {
'h2': 'У нас самая низкая цена на телефоны',
'div': 'Купить',
'p': "Продать"
}
}
}
def find_key(dict_1, key):
	if key in dict_1:
		dict_1[key] = new_prod
	for i_value in dict_1.values():
		if isinstance(i_value, dict):
			result = find_key(i_value, key)
			if result:
				break
	else:
		result = None

	return result

def make_site():
	sites = []
	new_site = find_key(copy.deepcopy(site), 'title')
	sites.append(new_site)




quant_product = 2
new_product = ["Samsung", "Iphone"]
make_site(site, new_product, quant_product)
