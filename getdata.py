from requirements import *


"""Getting Name of the Images"""
def filename():
    imgname = []
    for img in glob.iglob('images' + '/*.JPG'):
        im = Image.open(img).filename.strip("images/")
        imgname.append(im)

    return imgname


"""Extracting EXIF Data from the Images"""
def get_exifdata():
    imgdata = []
    for img in glob.iglob('images/*.JPG'):
        if img is None:
            print("Can't load the image")
            sys.exit(1)
        else:
            try:
                im = Image.open(img)
                exif_data = im._getexif()[0x8825]              #EXIFTag for GPS Info
            except:
                print("GPS Info Not found for",im.filename.strip("images/"))
            imgdata.append(exif_data)

    return imgdata


"""Converting Latitude Longitude EXIF Format Data to Degrees"""
def _convert_to_degress(value):
    d0 = value[0][0]
    d1 = value[0][1]
    d = float(d0) / float(d1)

    m0 = value[1][0]
    m1 = value[1][1]
    m = float(m0) / float(m1)

    s0 = value[2][0]
    s1 = value[2][1]
    s = float(s0) / float(s1)

    return d + (m / 60.0) + (s / 3600.0)


"""Converting Latitude Longitude EXIF Format Data to Degrees"""
def _convert_altitude_to_degrees(value):
    alt0 = value[0]
    alt1 = value[1]
    alt = float(alt0) / float(alt1)

    return alt


"""Getting Coordinates and Writing it in *imagedata.csv*"""
def get_coord(exif_data):
    n = len(exif_data)
    fname = filename()
    
    print("Writing into CSV...")

    with open('imagedata.csv','w') as file:
        writer = csv.writer(file)
    
        for i in range(1,n):
            get_lat_ref = exif_data[i][1]
            get_lat = exif_data[i][2]
            get_lon_ref = exif_data[i][3]
            get_lon = exif_data[i][4]
            get_alt_ref = exif_data[i][5]
            get_alt = exif_data[i][6]

            if get_lat and get_lat_ref and get_lon and get_lon_ref and get_alt and get_alt_ref:
                lat = _convert_to_degress(get_lat)
                if get_lat_ref != 'N':
                    lat = 0 - lat

                lon = _convert_to_degress(get_lon)
                if get_lon_ref != 'E':
                    lon = 0 - lon

                alt = _convert_altitude_to_degrees(get_alt)
                if get_alt_ref == 0:
                    alt = 0 - alt

            writer.writerow([fname[i], lat, lon, alt])
    
    file.close()
    print("Done!\n")