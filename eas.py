import urllib3



eass1=('manifest.m3u8 video0-640x360_main_950.m3u8 video0-640x360_main_950_0.ts video0-640x360_main_950_1.ts video0-640x360_main_950_2.ts video0-640x360_main_950_3.ts video0-640x360_main_950_4.ts video0-640x360_main_950_5.ts video0-640x360_main_950_6.ts')

eass=eass1.split(" ")

def eas_url():
    #print('checking %d  maxxsouth pack1 channels in maxxsouth streamers' % len(maxx_var))
    #for maxx_channels in maxx_var:
    for x in range(0, 20):
        for urls in eass:
            connection = urllib3.PoolManager()

            input=('ip_address/dasdec_public/example/%s' % (urls))
            g=connection.request("GET", input)
            h=connection.request("HEAD", input)
            p=connection.request("POST", input)

            print('#################################')
            print(input)
            print('GET response code %s ' % g.status)
            print('HEAD response code %s ' % h.status)
            print('POST response code %s ' % p.status)

            #if r.status != 200:
            #    print('%s channel was problem not connecting ' % urls)

eas_url()
