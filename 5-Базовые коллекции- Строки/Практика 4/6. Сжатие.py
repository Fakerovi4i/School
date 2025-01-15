text = "aaAAbbсaaaA"
count = 1
text_list = ""
for sym_i in range(len(text)):
	if sym_i == len(text)-1:
		text_list = ''.join([text_list, text[sym_i]])
		text_list = ''.join([text_list, str(count)])
		# text_list += text[sym_i]
		# text_list+= str(count)
		break
	if text[sym_i] == text[sym_i+1]:
		count += 1
	else:
		text_list = ''.join([text_list, text[sym_i]])
		text_list = ''.join([text_list, str(count)])
		# text_list += text[sym_i]
		# text_list += str(count)
		count = 1

print(text_list)
#print(''.join(text_list))