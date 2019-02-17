import requests

def traffic():

    y = input('Enter the ATS ip with port : ')
    #z = ('http://%s', + x)
    z = int(input('Enter the number of requests: '))
    i=0

    try:
        while i < z:
            x = requests.get(y).elapsed.total_seconds()
            #if x >= 1:
            print("{} Traffic_server {} response close time of {}s" .format(i,y, x))
            i+=1
    except:
            print ("Closed the connection ..")


def Http():
    y = input('Enter the Httpd ip : ')
    z = int(input('Enter the number of requests: '))
    i=0

    try:
        while i < z:
        #y = "http://x.x.x.x"
            x = requests.get(y).elapsed.total_seconds()
        #if x >= 1:
            print("{} Http {} response close time of {}s" .format(i,y, x))
            i+=1
    except:
            print ("Closed the connection ..")


func_dict = {'ATS':traffic, 'HTTP':Http}
command = input("Enter server the type (ATS or HTTP)  > ")

func_dict.get(command)

try:

        if command == 'ATS':
            traffic()
    #           else:
    #        print("error enter valid input ..")
        if command == 'HTTP':
            Http()

except:
    print ("Please Enter Valid INPUT ")

#func_dict[command]()
#Http()
#traffic()
