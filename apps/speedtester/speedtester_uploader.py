import speedtest

wifi = speedtest.Speedtest()
print("Wifi Download Speed is ", wifi.download())
print("Wifi Upload Speed is ", wifi.upload())
print(f"{wifi.closest}")
print(f"{wifi.config}")
print(f"{wifi.lat_lon}")
