from requirements import *


def get_kml():
    print("Generating KML")
    file = csv.reader(open('srtdata.csv','r'))
    kml = simplekml.Kml()                   #Initiating Kml file

    for row in file:
        kml.newpoint(name = 'GpsData', 
            description = 'Drone Location by using SRT File', 
            coords = [(row[1],row[0])])     #KML takes lon and lat so row[1],row[0]

    kml.save('drone_loc.kml')
    print("Done!\n")