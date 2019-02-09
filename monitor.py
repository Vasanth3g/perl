import psutil

def Cpu():
    no_cpu = psutil.cpu_count()
    cpu_freq = psutil.cpu_freq()
    #c = cpu_freq.current
    d = cpu_freq.max
    #percent = psutil.cpu_percent()
    print ("################CPU###################")
    print ("No . of CPU's : " , no_cpu)
    print ("Max Frequency in CPU's : " ,d,"freq" )
    print ("Currently Using CPU : ", psutil.cpu_percent(), "%")
    print ("#################MEMORY#######################")

def Mem():
    mem = psutil.virtual_memory()
    total = round(mem.total/1073741824)
    used = round(mem.used/1073741824)
    free = round(mem.free/1073741824)
    mem_percent = mem.percent
    print ("Total Memory : " ,total)
    print ("Used Memory  : " ,used)
    print ("Free Memory  : " ,free )
    print ("Used Memory Percent : " ,mem_percent )
    print ("#################DISK USAGE########################")

def Disk():
    disk = psutil.disk_usage('/')
    total = round(disk.total/1073741824)
    used = round(disk.used/1073741824)
    free = round(disk.free/1073741824)
    percent = disk.percent
    print ("Total Storage : " ,total)
    print ("Used Storage  : " ,used)
    print ("Free Storage  : " ,free )
    print ("Used Storage Percent : " ,percent )
    print ("##############################################")

Cpu()
Mem()
Disk()
