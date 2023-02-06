ent1 = input()
ent2 = input()
ent3 = input()
result = ("")
for i in ent3:
	if i in ent2:
		var = ent2.find(i)
		result+=ent1[var]
	else:
		result+=(".")
print(result)