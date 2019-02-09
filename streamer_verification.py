import urllib3
pack1=( 'ABC DEF GHI' )

pack_var=maxx_pack1.split(" ")

buck_pack2=('JKL MNO PQR ')

pack2=buck_pack2.split(" ")


sss_pack1=('WXY ZWA MMM')

ssss_pack1=buck_pack1.split(" ")

ips={'z.z.z.z w.w.w.w'}

def south_channels():
    print('checking %d  eeee pack1 channels in maxxsouth streamers' % len(pack_var))
    for vvv_channels in pack_var:
        for ip in ips:
            connection = urllib3.PoolManager()

            input=('%s:8006/EvoLive/%s/STB.m3u8' % (ip,vvv_channels))
            r=connection.request("GET", input)
            #print(r.status)
            if r.status != 200:
                print('%s channel was problem not connecting ' % maxx_channels)


def eye_channels():
    print('checking %d  dddd pack1 channels in maxxsouth streamers' % len(pack2))
    for vvv_channels_1 in pack2:
        for ip in ips:
            connection = urllib3.PoolManager()
            input=('%s:8006/EvoLive/%s/STB.m3u8' % (ip,pack2))
            r=connection.request("GET", input)
            #print(r.status)
            if r.status != 200:
                print('%s channel was problem not connecting' % vvv_channels_1 )

def uckye_channels2():
    print('checking %d  cccc pack2 channels in maxxsouth streamers' % len(ssss_pack1))
    for buck_channels_2 in ssss_pack1:
        for ip in ips:
            connection = urllib3.PoolManager()

            input=('%s:8006/EvoLive/%s/STB.m3u8' % (ip,buck_channels_2))
            r=connection.request("GET", input)
            if r.status != 200:
                print('%s channel was problem not connecting ' % buck_channels_2)

#
#south_channels()
#eye_channels()
#uckye_channels2()
