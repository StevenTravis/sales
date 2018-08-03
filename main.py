# main file


def readFile():
	try:
		sales = open("log.txt", "r")
		#print (sales.read())
		split_sales = sales.read()
		test = split_sales.split()
		print (test)
		print (test[7], test[13])
	except Exception as missing:
		print(missing)





readFile()
