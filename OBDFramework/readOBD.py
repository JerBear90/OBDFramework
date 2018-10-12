import obd

connection = obd.Async() # same constructor as 'obd.OBD()'
connection.watch(obd.commands.RPM) # keep track of the RPM
connection.start() # start the async update loop

def new_rpm(request):
	val = connection.query(obd.commands.RPM) # non-blocking, returns immediately
	print (val)
	# driver.refresh() # refresh webpage
	return render(request, 'home.html', {'val': val})