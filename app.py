from requirements import *
import getdata, readsrt, result, generatekml

if __name__ == "__main__":
    
    exifdata = getdata.get_exifdata()
    getdata.get_coord(exifdata)
    
    readsrt.read_srtfile()
    
    result.get_result()
    
    print("Please Check the results in \n| assets_poi_50m.csv |\n| image_with_dist_35.csv |\n")
    
    generatekml.get_kml()