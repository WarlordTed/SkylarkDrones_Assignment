from requirements import *


"""Calculating distance between 2 latitude and longitude points"""
def haversine(lat1, lon1, lat2, lon2):
    earth_radius = 6371                 #KM

    lat1 = radians(float(lat1))         #Convert Decimal to Radians
    lon1 = radians(float(lon1))
    lat2 = radians(float(lat2))
    lon2 = radians(float(lon2))

    dist_lon = lon2 - lon1
    dist_lat = lat2 - lat1

    hav_formula = (sin(dist_lat / 2)**2) + (cos(lat1) * cos(lat2) * sin(dist_lon / 2)**2) #Haversine formula
    distance = 2 * earth_radius * atan2(sqrt(hav_formula),sqrt(1-hav_formula)) * 1000     #M

    return distance


def get_result():
    """Reading CSV Files"""
    #Image Data
    imagename = []
    latdata = []
    londata = []

    #SRT Data
    latdata_srt = []
    londata_srt = []

    #Assets Data
    lat_asset = []
    lon_asset = []

    with open("imagedata.csv","r") as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        
        for row in data:
            imagename.append(row[0])
            latdata.append(row[1])
            londata.append(row[2])

    with open("srtdata.csv","r") as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        
        for row in data:
            latdata_srt.append(row[0])
            londata_srt.append(row[1])

    with open("assets.csv","r") as csvfile:
        data = csv.reader(csvfile)
        
        for row in data:
            lat_asset.append(row[2])
            lon_asset.append(row[1])


    image = {}

    """Calculating Distance from the Drone location to the Images"""
    for i in range(0,len(latdata_srt)):        #SRT_LOOP
        image[i] = []
        
        for j in range(0,len(imagename)):      #IMAGEDATA_LOOP
            x = haversine(latdata_srt[i],londata_srt[i],latdata[j],londata[j])
            
            if x < 35:                         #Within 35m distance
                image[i].append(imagename[j])

    print("Getting Images with 35m radius...")
    print("Writing into CSV file...")

    with open("image_with_dist_35.csv","w") as resultcsv:
        data = csv.writer(resultcsv)
        
        for key, val in image.items():
            data.writerow([key,val])

    print("Done!\n")


    points = {}

    """Calculating Distance from the Area of Interest to the Images"""
    for i in range(1,len(lat_asset)):          #SRT_LOOP
        points[i] = []
        
        for j in range(0,len(imagename)):                   #IMAGEDATA_LOOP
            x = haversine(lat_asset[i],lon_asset[i],latdata[j],londata[j])
            
            if x < 50:                         #Within 35m distance
                points[i].append(imagename[j])

    print("Getting Images with 50m radius...")
    print("Writing into CSV file...")

    with open("assets_poi_50m.csv", "w") as resultcsv:
        data = csv.writer(resultcsv)
        
        for key,val in points.items():
            data.writerow([key,val])

    print("Done!\n")