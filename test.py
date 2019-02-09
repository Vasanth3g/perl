import module 
import platform
import datetime
import json
import re

module.vasanth("here")
x = module.person1["age"]
print("Vasanth age is " , x)

print(platform.system())
print(platform.machine())


y = datetime.datetime.now()

print(y.year)
print(y.strftime("%A")) 



# a Python object (dict):
a = {
	"raja ":"sabari"
}

# convert into JSON:
z = json.dumps(a)

# the result is a JSON string:
print(z) 

w = "that is your name"

zy = re.sub("that","myname",w)
print(zy)