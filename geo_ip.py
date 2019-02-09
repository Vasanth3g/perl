import geoip2.database
import socket

domain = input("Enter your domain address :" )

con_ip = socket.gethostbyname(domain)
db = geoip2.database.Reader('GeoLite2-City.mmdb')
data = db.city(con_ip)

longitude = data.location.longitude
latitude = data.location.latitude
city_name = data.city.name
state = data.subdivisions.most_specific.name
country  = data.country.names['en']
postal_code = data.postal.code
country_code  = data.country.iso_code
#country  = data.country.name

db.close()

print ("IP : %s" % con_ip)
print ("Cordinates Longitude %.2f , Latitude %.2f" % (round(longitude),round(latitude)))
print ("City Name : %s" % data.city.name)
print ("State Name: %s" % data.subdivisions.most_specific.name )
print ("Country Name: %s" % data.country.names['en'] )
print ("Postal Code: %s" % data.postal.code)
print("Country Code: %s" % data.country.iso_code)
