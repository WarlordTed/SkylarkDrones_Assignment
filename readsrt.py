from requirements import *


"""Reading SRT File and Converting it to CSV file format *srtdata.csv*"""
def read_srtfile():
    gps_lat = []
    gps_lon = []
    gps_alt = []

    print("Reading SRT file...")
    
    file = open("videos/DJI_0301.SRT", "r")
    while True:
        line = file.readline()
        line = file.readline()     
        line = file.readline()          # location
    
        if not line:
            break
    
        lon, lat, alt = line.split(',')
        lon, lat, alt = float(lon), float(lat), float(alt)    
    
        gps_lon.append(lon)
        gps_lat.append(lat)
        gps_alt.append(alt)
    
        line = file.readline()          # read blank line

    file.close()
    print("Writing into CSV file...")

    with open("srtdata.csv","w") as srt_csv:
        srtwriter = csv.writer(srt_csv)
        
        for i in range(0,len(gps_alt)):
            srtwriter.writerow([gps_lat[i], gps_lon[i], gps_alt[i]])

    srt_csv.close()
    print("Done!\n")