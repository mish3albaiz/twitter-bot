# Python program to get a google map
# image of specified location using
# Google Static Maps API

# importing required modules
import requests
import loginfo

# Enter your api key here
api_key = loginfo.google_maps_api_key

# url variable store url
url = "https://maps.googleapis.com/maps/api/staticmap?"

# center defines the center of the map,
# equidistant from all edges of the map.
def map_image(location):

    center = location

    # zoom defines the zoom
    # level of the map
    zoom = 13

    # get method of requests module
    # return response object
    r = requests.get(url + "center=" + center + "&zoom=" +
                       str(zoom) + "&size=640x500" + "&format=png&markers=" + center + "&key=" +
                                 api_key )



    # wb mode is stand for write binary mode
    f = open('map.png', 'wb')

    # r.content gives content,
    # in this case gives image
    f.write(r.content)

    # close method of file object
    # save and close the file
    f.close()
