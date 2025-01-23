import copy
site = {
'html': {
'head': {
'title': 'Куплю/продам {} недорого'
},
'body': {
'h2': 'У нас самая низкая цена на {}',
'div': 'Купить',
'p': "Продать"
}
}
}
def change_key(dict_1, key, new_prod="НАЗВАНИЕ"):
	if key in dict_1:
		dict_1[key] = dict_1[key].format(new_prod)
	for i_value in dict_1.values():
		if isinstance(i_value, dict):
			change_key(i_value, key, new_prod)
	
def make_site(site, quant_product):
  sites = []
  names_sites = []
  for ind_x in range(quant_product):
    new_product = input("Ваедите название продукта: ")
    keys = ['title',"h2"]
    new_site = copy.deepcopy(site)
    for i_keys in range(2):
      change_key(new_site, keys[i_keys], new_prod=new_product)
    sites.append(new_site)
    names_sites.append(new_product)
    
    for i_site, site_dict in zip(names_sites, sites):
      print("Сайт для {}:".format(i_site))
      print(site_dict)
	
quant_product = int(input("Сколько сайтов?: "))
make_site(site, quant_product)
