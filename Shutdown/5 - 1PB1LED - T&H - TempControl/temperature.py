import os 

# Return CPU temperature as a character string                                      
def getCPUtemperature():
	res = os.popen('vcgencmd measure_temp').readline()
	res = res.replace("temp=","").replace("'C\n","")
	return(int(float(res)))

teste = getCPUtemperature()

print teste

teste2 = float(teste)

print teste2

teste3 = int(teste2)

print teste3