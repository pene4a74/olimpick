n = int (input (""))
lst = []
lst_file_names = []
for i in range(0, n):
	file = input("")	
	s_file = file
	f_format = ""
	if file in lst_file_names:
		end_index = file.find(".")
		if end_index == -1:
			file = ''.join("("+str(lst_file_names.count(s_file))+")")
			lst.append (file)
			lst_file_names.append(s_file)
		else:
			lst_file_names.append(file)
			file_namme = file[0:end_index]
			f_format = s_file[end_index:len(s_file) ]
			file_name = ''.join("("+str(lst_file_names.count(file)-f)+")"+ f_format)
			lst.append (filename)
	else:
		lst.append(file)
		lst_file_names.append(file)
lst.sorted()
print (lst)