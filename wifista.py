def connect():
    import network
    
    ip        = '192.168.1.110'
    subnet    = '255.255.255.0'
    gateway   = '192.168.1.1'
    dns       = '8.8.8.8'
    ssid      = "Livebox-08B0"
    password  =  "G79ji6dtEptVTPWmZP"
 
    station = network.WLAN(network.STA_IF)

    if station.isconnected() == True:
        print("Already connected")
        return
 
    station.active(True)
    # station.ifconfig((ip,subnet,gateway,dns))  # uncomment to set static IP
    station.connect(ssid,password)
 
    while station.isconnected() == False:
        pass
 
    print("Connection successful")
    print(station.ifconfig())

def disconnect():
    import network
    station = network.WLAN(network.STA_IF)
    station.disconnect()
    station.active(False)
    

 connect()
 