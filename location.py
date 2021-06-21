# import geocoder
# t=input("enter the location:")
# g = geocoder.arcgis(t)
# b=g.latlng
# c=b[0]
# d=b[1]
# # for ele in b:
# #     print(ele)
# # a=g.address
# print(c)
# # print(g)



import geocoder

def Location(city):
    g = geocoder.arcgis(city)
    b=g.latlng
    c=float(b[0])
    d=float(b[1])
    print(c,d)
if __name__ =="__main__":
    Location("chennai")




# import requests

# def Weather(city):
#     api_ = "http://api.openweathermap.org/data/2.5/weather?appid=create you own API for and enter here&q="

#     url_ = api_ + 'city'
#     json_data = requests.get(url_).json()
#     format_add = json_data['main']

#     return format_add








# import requests

# key = "PCaAVkcxQxBLADGMabJgBL0wT8buL6BK"
# url = 'http://www.mapquestapi.com/geocoding/v1/address?key='
# loc = input("Enter place : ")
# main_url = url+key+ "&location=" +loc
# r=requests.get(main_url)
# data=r.json()['results'][0]
# location = data['locations'][0]


# city = location['adminArea5']
# state = location['adminArea3']
# country = location['adminArea1']
# zipcode = location['postalCode']
# lat = location['latLng']['lat']
# lon = location['latLng']['lng']


# print('City: ',city)
# print('State: ',state)
# print('Country: ',country)
# print('Postal Code: ',zipcode)
# print('Latitude: ',lat)
# print('Longitude: ',lon)









# # import module
# from geopy.geocoders import Nominatim

# # initialize Nominatim API
# geolocator = Nominatim(user_agent="geoapiExercises")

# # place input by geek
# place = "boaring road patna"
# location = geolocator.geocode(place)

# # traverse the data
# data = location.raw
# loc_data = data['display_name'].split()
# print("Full Location")
# print(loc_data)
# print("Zip code : ",loc_data[-2])
