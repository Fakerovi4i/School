text = "питон - это хорошо"
up = 0
low = 0

for i in text:
	if i.isupper():
		up += 1
	elif i.islower():
		low += 1

if up > low:
	print(text.upper())
else:
	print(text.lower())