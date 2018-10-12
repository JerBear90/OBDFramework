from django.shortcuts import render
import obd

# Connect Async
connection = obd.Async() # same constructor as 'obd.OBD()'

# Watch Commands
# Commands current watching:
# RPM
# SPEED
# FUEL_STATUS
# FUEL_LEVEL
connection.watch(obd.commands.RPM) # keep track of the RPM
connection.watch(obd.commands.SPEED) # keep track of the SPEED
connection.watch(obd.commands.FUEL_STATUS) # keep track of the FUEL_STATUS
connection.watch(obd.commands.FUEL_LEVEL) # keep track of the FUEL_LEVEL

connection.start() # start the async update loop

def home(request):
	a = 0
	return render(request, 'home.html')
	
def rpm(request):
	# setting all variable to 0 for start

	speed = 0
	fuel_status = 0
	fuel_level = 0
	rpm = 10

	# for rpm in range(0,10):
	# 	print(rpm)
	# Query grabbed commands
	rpm = connection.query(obd.commands.RPM)
	speed = connection.query(obd.commands.SPEED)
	fuel_status = connection.query(obd.commands.FUEL_STATUS)
	fuel_level = connection.query(obd.commands.FUEL_LEVEL)

	# Print them to the console
	print (rpm)
	print (speed)
	print (fuel_status)
	print (fuel_level)

	# render our variables to the page
	return render(request, 'rpm.html', {'rpm': rpm, 'speed': speed, 'fuel_status': fuel_status, 'fuel_level': fuel_level})
