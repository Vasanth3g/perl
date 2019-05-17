import urllib3
pack1=( 'ABC DEF GHI' )

pack_var=maxx_pack1.split(" ")

busss_pack2=('JKL MNO PQR ')

pack2=busss_pack2.split(" ")


sss_pack1=('WXY ZWA MMM')

ssss_pack1=sss_pack1.split(" ")

ips={'z.z.z.z w.w.w.w'}

def south_channels():
    print('checking %d  eeee pack1 channels in  streamers' % len(pack_var))
    for vvv_channels in pack_var:
        for ip in ips:
            connection = urllib3.PoolManager()

            input=('%s:8006/Live/%s/STB.m3u8' % (ip,vvv_channels))
            r=connection.request("GET", input)
            #print(r.status)
            if r.status != 200:
                print('%s channel was problem not connecting ' % maxx_channels)


def my_channels():
    print('checking %d  dddd pack1 channels in  streamers' % len(pack2))
    for vvv_channels_1 in pack2:
        for ip in ips:
            connection = urllib3.PoolManager()
            input=('%s:8006/Live/%s/STB.m3u8' % (ip,pack2))
            r=connection.request("GET", input)
            #print(r.status)
            if r.status != 200:
                print('%s channel was problem not connecting' % vvv_channels_1 )

def my_channels2():
    print('checking %d  cccc pack2 channels in  streamers' % len(ssss_pack1))
    for bu_channels_2 in ssss_pack1:
        for ip in ips:
            connection = urllib3.PoolManager()

            input=('%s:8006/Live/%s/STB.m3u8' % (ip,bu_channels_2))
            r=connection.request("GET", input)
            if r.status != 200:
                print('%s channel was problem not connecting ' % bu_channels_2)

#
#south_channels()
#my_channels()
#my_channels2()
