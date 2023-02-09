# Reference : https://www.youtube.com/watch?v=vTFn9gWEtPA
import os
import pandas
import googlemaps

def get_geometric(inAddress):
    try:
        goBack = []

        GOOGLE_MAPS_API_KEY = 'AIzaSyDQShqrTds5KMCQyZ1U7dQdiL4gCDXRPGE'
        
        gmap_client = googlemaps.Client(GOOGLE_MAPS_API_KEY);

        result = gmap_client.geocode(inAddress)

        goBack.append(result[0]['geometry']['location']['lat'])
        goBack.append(result[0]['geometry']['location']['lng'])
    except:
        goBack.append(0.0)
        goBack.append(0.0)
        
    return(goBack)


# def main():
#     myList = []
#     myList = get_geometric('Nothing')
#     for x in myList:
#         print(x)

# main()

