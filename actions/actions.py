
from rasa_sdk.events import AllSlotsReset
# class ActionRestart(Action):
# def name(self):
#     return 'action_restart'

# def run(self, dispatcher, tracker, domain):
from typing import Dict, Text, Any, List, Union, Optional
from database_connectivity import DataUpdate

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk import Action

from rasa_sdk.forms import FormAction
from rasa_sdk.events import Restarted 

from rasa_sdk.events import AllSlotsReset

class ActionHelloWorld(Action):

     def name(self) -> Text:
            return "action_restart"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message("THANK YOU FOR USING SHADE6 ESTATES BOT!")

         return [AllSlotsReset()]

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []



from typing import Dict, Text, Any, List, Union, Optional
from database_connectivity import DataUpdate

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk import Action
import pymysql


class BuyHomeForm(Action):
    def name(self):
        return "db_form"
    def required_slots(self,tracker) -> List[Text]:
        return ["location","type","range"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "location": [
                self.from_text(),
            ],
            "type": [
                self.from_text(),
            ],
            "range": [
                self.from_text(),
            ],
            
            
        }
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_template(tracker)    
        # DataUpdate(name=tracker.get_slot(text="name"),type=tracker.get_slot(text="type"),phone=tracker.get_slot(text="number"),pincode=tracker.get_slot(text="pincode"))

        return []


#***********************************************************************************
# from rasa_sdk.interfaces import Action

# class ActionGreet(Action):
#     def name(self):
#         return 'action_fullview'

#     def run(self, dispatcher, tracker, domain):
#         dispatcher.utter_message(template="action_fullview")
#         return []


    # def name(self):
    #     return "buy_form"
        
    # def required_slots(self,tracker) -> List[Text]:
    #     return ["name","number","pincode"]
    # def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
    #     return {
    #         "name": [
    #             self.from_entity(entity='name'),
    #             self.from_text(),
    #         ],
    #         "number": [
    #             self.from_entity(entity='number' ),
    #             self.from_text(),
    #         ],
            
    #         # "location": [
    #         #     self.from_text(),
    #         # ],
    #         "pincode": [
    #             self.from_entity(entity='pincode'),
    #             self.from_text(),
    #         ],
    #         # "type": [
    #         #     self.from_text(),
    #         # ],
    #         # "pincode": [
    #         #     self.from_text(),
    #         # ],
    #         # "type": [
    #         #     self.from_text(),
    #         # ],
    #     }
    # def submit(
    #     self,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: Dict[Text, Any],
    # ) -> List[Dict]:
    #     dispatcher.utter_template("utter_submit", tracker)    
    #     # DataUpdate(name=tracker.get_slot(text="name"),type=tracker.get_slot(text="type"),phone=tracker.get_slot(text="number"),pincode=tracker.get_slot(text="pincode"))

    #     return []

import mysql.connector

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_core_sdk.events import Restarted
import pymysql
import geocoder
# from location import c,d


class ActionRasa(Action): 
# search based on cuisine -> zip
    def name(self) -> Text: 
        #Unique identifier of the form
        return "action_fullview"

    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
        import geocoder
        city = tracker.get_slot("location")
        range1 = tracker.get_slot("range")
        g = geocoder.arcgis(city)
        b=g.latlng
        Lat=float(b[0])
        Lon=float(b[1])
        #city = tracker.get_slot("location")
        print(Lat)
        print(Lon) 
        print(city)
        print(range1)
        conn = pymysql.connect(
            host="206.189.142.4", 
            user="root", 
            password="Tech$321", 
            database="realestate" 
        )
        cur = conn.cursor()
        sql = "SELECT *, (6371 * acos (cos ( radians({0}) ) * cos( radians( Lat ) ) * cos( radians( Lon ) - radians({1}) ) + sin ( radians({0}) ) * sin( radians( Lat )))) AS distance FROM propertyDetails HAVING distance < {2} ORDER BY distance LIMIT 0 , 20;".format(Lat, Lon,range1)
        # sql = "SELECT *, (6371 * acos (cos ( radians(13.0836) ) * cos( radians( Lat ) ) * cos( radians( Lon ) - radians(80.2825) ) + sin ( radians(13.0836) ) * sin( radians( Lat )))) AS distance FROM propertyDetails HAVING distance < 1475 ORDER BY distance LIMIT 0 , 20;"
        # sql = 'SELECT * FROM propertyDetails WHERE city LIKE "%{}%" AND category LIKE "%{}%"'.format(city, category)
        # sql = "SELECT *, (6371 * acos (cos ( radians({0}) ) * cos( radians( Lat ) ) * cos( radians( Lon ) - radians({1}) ) + sin ( radians({0}) ) * sin( radians( Lat )))) AS distance FROM propertyDetails HAVING distance < 10000 ORDER BY distance LIMIT 0 , 20;".format(Lat, Lon) 
        # sql = "SELECT propId, 	customerId, 	name,description ,builderName ,price ,area ,city ,state ,country ,locality ,pincode ,Lat ,Lon ,type ,category ,listingType ,furnishing ,propType ,houseType ,propAge, (6371 * acos (cos ( radians("%{}%") ) * cos( radians( Lat ) ) * cos( radians( Lon ) - radians("%{}%") ) + sin ( radians("%{}%") ) * sin( radians( Lat )))) AS distance FROM propertyDetails HAVING distance < 100000 ORDER BY distance LIMIT 0 , 20".format(Lat, Lon, Lat)
        # sql =  "SELECT description,name, (6371 * acos (cos ( radians("%{Lat}%") ) * cos( radians( Lat ) ) * cos( radians( Lon ) - radians("%{Lon}%") ) + sin ( radians("%{Lat}%") ) * sin( radians( Lat )))) AS distance FROM propertyDetails HAVING distance < 1800 ORDER BY distance LIMIT 0 , 20".format(Lat, Lon)

        # sql = 'SELECT * FROM propertyDetails'
        cur.execute(sql)
        result = cur.fetchall()
        if len(result) > 0:
            dispatcher.utter_message("____ FULL PROPERTY DETAILS ____")
            for row in result:
                # print('id: ', row[0])
                userid = row[0]
                a = row[1]
                alpha = row[2]
                b = row[3]
                c = row[4]
                d = row[5]
                e = row[6]
                f = row[7]
                g = row[8]
                h = row[9]
                i = row[10]
                j = row[11]
                k = row[12]
                l = row[13]
                m = row[14]
                n = row[15]
                o = row[16]
                p = row[17]
                q = row[18]
                r = row[19]
                s = row[20]
                # t = row[21]
                
                dispatcher.utter_message("__ PROPERTY DETAIL __ \n\nProperty image:",userid)     
                # dispatcher.utter_message("PROPERTY DETAIL_________",userid,"Property image\n")               
                dispatcher.utter_message("Name:{}\nDescription:{}\nLocality:{}\nCity:{}\nLat:{}\nLon:{}\nBuilderName:{}\nPrice:{}\nArea:{}\nState:{}\nCountry:{}\nPincode:{}\nType:{}\nCategory:{}\nListingType:{}\nFurnishing:{}\nPropType:{}\nPropAge:{}\nBedrooms:{}\nBathrooms:{}\n\n\n".format(a,alpha, b, c, d, e,f,g,h,i,j,k,l,m,n,o,p,q,r,s))
                # dispatcher.utter_message(" \n\n\nHere is the information..\npropId:{}\ncustomerId:{}\nname:{}\ndescription:{}\nbuilderName:{}\nprice:{}\narea:{}\ncity:{}\nstate:{}\ncountry:{}\nlocality:{}\npincode:{}\nlat:{}\nlon:{}\ntype:{}\ncategory:{}\nlistingType:{}\nfurnishing:{}\npropType:{}\nhouseType:{}\npropAge:{}\n\n\n".format(userid,a, b, c, d, e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t))
                # dispatcher.utter_message("Here is the information	name:{}\n 	description: {}\n 	\n\n\n".format(userid,a))

        else:
            dispatcher.utter_message("No data found in the database, please try again.")
        conn.close()
        return []





from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_core_sdk.events import Restarted
import pymysql
import geocoder
# from location import c,d


# class ActionCuisineC(Action): 
# # search based on cuisine -> zip
#     def name(self) -> Text: 
#         #Unique identifier of the form
#         return "action_response"

#     def run(self, dispatcher: CollectingDispatcher, 
#             tracker: Tracker, 
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
        
#         import geocoder
#         # t=input("enter the location:")
#         city = tracker.get_slot("location")
#         g = geocoder.arcgis(city)
#         b=g.latlng
#         Lat=float(b[0])
#         Lon=float(b[1])
#         # city = tracker.get_slot("location")
#         # category = tracker.get_slot("type")

#         conn = pymysql.connect(
#             host="206.189.142.4", 
#             user="root", 
#             password="Tech$321", 
#             database="realestate" 
#         )
#         cur = conn.cursor()
#         # sql = 'SELECT * FROM propertyDetails WHERE city LIKE "%{}%" AND category LIKE "%{}%"'.format(city, category)
#         # sql="SELECT PrimaryImages,name,description,Lat,Lon FROM propertyDetails WHERE dbo.udf_Haversine(latitude, longitude, {0}, {1}) < 5".format(Lat, Lon) 
#         sql = "SELECT PrimaryImages,name,description,Lat,Lon, (6371 * acos (cos ( radians(13.0836) ) * cos( radians( Lat ) ) * cos( radians( Lon ) - radians(80.2825) ) + sin ( radians(13.0836) ) * sin( radians( Lat )))) AS distance FROM propertyDetails HAVING distance < 1475 ORDER BY distance LIMIT 0 , 20;"#.format(Lat, Lon) 
#         # sql = "SELECT propId, 	customerId, 	name,description ,builderName ,price ,area ,city ,state ,country ,locality ,pincode ,Lat ,Lon ,type ,category ,listingType ,furnishing ,propType ,houseType ,propAge, (6371 * acos (cos ( radians("%{}%") ) * cos( radians( Lat ) ) * cos( radians( Lon ) - radians("%{}%") ) + sin ( radians("%{}%") ) * sin( radians( Lat )))) AS distance FROM propertyDetails HAVING distance < 100000 ORDER BY distance LIMIT 0 , 20".format(Lat, Lon, Lat)
#         # sql =  "SELECT description,name, (6371 * acos (cos ( radians("%{Lat}%") ) * cos( radians( Lat ) ) * cos( radians( Lon ) - radians("%{Lon}%") ) + sin ( radians("%{Lat}%") ) * sin( radians( Lat )))) AS distance FROM propertyDetails HAVING distance < 1800 ORDER BY distance LIMIT 0 , 20".format(Lat, Lon)

#         # sql = 'SELECT * FROM propertyDetails'
#         cur.execute(sql)
#         result = cur.fetchall()
#         if len(result) > 0:
#             for row in result:
#                 # print('id: ', row[0])
#                 userid = row[0]
#                 a = row[1]
#                 b = row[2]
#                 c = row[3]
#                 d = row[4]
#                 # e = row[5]
#                 # f = row[6]
#                 # g = row[7]
#                 # h = row[8]
#                 # i = row[9]
#                 # j = row[10]
#                 # k = row[11]
#                 # l = row[12]
#                 # m = row[13]
#                 # n = row[14]
#                 # o = row[15]
#                 # p = row[16]
#                 # q = row[17]
#                 # r = row[18]
#                 # s = row[19]
#                 # t = row[20]
#                 # t = row[21]
                
#                 attachment = {"\nPropertyImages:\n":userid}
#                 dispatcher.utter_custom_json(attachment)
#                 dispatcher.utter_message("Here is the information\n\nPropertyImages:{0}\nname:{1}\ndescription:{2}\nLat:{3}\nLon:{4}\n\n\n".format(userid,a, b, c, d))
#                 # dispatcher.utter_message(text="View Property", buttons=[{ "payload": "/action_fullview"}])

#                 # dispatcher.utter_message("Here is the information	name:{}\n 	description: {}\n 	\n\n\n".format(userid,a))

#         else:
#             dispatcher.utter_message("No data found in the database, please try again.")
#         conn.close()
#         return []

















from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_core_sdk.events import Restarted
import pymysql
import geocoder
# from location import c,d


class ActionCuisineC(Action): 
# search based on cuisine -> zip
    def name(self) -> Text: 
        #Unique identifier of the form
        return "action_response"

    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 

        #############################################

        # buttons = [{ "title": "View Properties", "payload": "/action_fullview"}]
               
        ##################################################
        import geocoder
        city = tracker.get_slot("location")
        range1 = tracker.get_slot("range")
        g = geocoder.arcgis(city)
        b=g.latlng
        Lat=float(b[0])
        Lon=float(b[1])
        #city = tracker.get_slot("location")
        print(Lat)
        print(Lon) 
        print(city)
        print(range1)
        conn = pymysql.connect(
            host="206.189.142.4", 
            user="root", 
            password="Tech$321", 
            database="realestate" 
        )
        cur = conn.cursor()
        # sql = 'SELECT * FROM propertyDetails WHERE city LIKE "%{}%" AND category LIKE "%{}%"'.format(city, category)
        # sql = "SELECT PrimaryImages,name,description,builderName,price, (6371 * acos (cos ( radians({0}) ) * cos( radians( Lat ) ) * cos( radians( Lon ) - radians({1}) ) + sin ( radians({0}) ) * sin( radians( Lat )))) AS distance FROM propertyDetails HAVING distance <1000 ORDER BY distance LIMIT 0 , 5;".format(Lat, Lon,range1) 
        sql = "SELECT PrimaryImages,name,description,locality,city, (6371 * acos (cos ( radians({0}) ) * cos( radians( Lat ) ) * cos( radians( Lon ) - radians({1}) ) + sin ( radians({0}) ) * sin( radians( Lat )))) AS distance FROM propertyDetails HAVING distance < {2} ORDER BY distance LIMIT 0 , 20;".format(Lat, Lon, range1) 
        # sql = "SELECT propId, 	customerId, 	name,description ,builderName ,price ,area ,city ,state ,country ,locality ,pincode ,Lat ,Lon ,type ,category ,listingType ,furnishing ,propType ,houseType ,propAge, (6371 * acos (cos ( radians("%{}%") ) * cos( radians( Lat ) ) * cos( radians( Lon ) - radians("%{}%") ) + sin ( radians("%{}%") ) * sin( radians( Lat )))) AS distance FROM propertyDetails HAVING distance < 100000 ORDER BY distance LIMIT 0 , 20".format(Lat, Lon, Lat)
        # sql =  "SELECT description,name, (6371 * acos (cos ( radians("%{Lat}%") ) * cos( radians( Lat ) ) * cos( radians( Lon ) - radians("%{Lon}%") ) + sin ( radians("%{Lat}%") ) * sin( radians( Lat )))) AS distance FROM propertyDetails HAVING distance < 1800 ORDER BY distance LIMIT 0 , 20".format(Lat, Lon)

        # sql = 'SELECT * FROM propertyDetails'
        cur.execute(sql)
        result = cur.fetchall()
        if len(result) > 0:
            buttons = []
            payload = "/propertydetails"
            buttons.append({"title": "Full Property View", "payload": payload})
            message = "Please click here for FullView"
            for row in result:
                # print('id: ', row[0])
                userid = row[0]
                a = row[1]
                alpha = row[2]
                b = row[3]
                c = row[4]
                # d = row[5]
                # e = row[6]
                # f = row[7]
                # g = row[8]
                # h = row[9]
                # i = row[10]
                # j = row[11]
                # k = row[12]
                # l = row[13]
                # m = row[14]
                # n = row[15]
                # o = row[16]
                # p = row[17]
                # q = row[18]
                # r = row[19]
                # s = row[20]
                # t = row[21]
                


                # img = userid
                
                dispatcher.utter_message("____ PROPERTY DETAIL ____ \n\nProperty image:",userid)     
                dispatcher.utter_message("Name:{0}\nDescription:{1}\nLocality:{2}\nCity:{3}\n\n\n".format(a,alpha, b, c))

                
                # update rasa core version for configurable `button_type`
                dispatcher.utter_button_message(message, buttons)
                # dispatcher.utter_button_message(buttons,tracker)
                # dispatcher.utter_message(text="View Property", buttons=[{ "payload": "/action_fullview"}])
                # dispatcher.utter_message(" \n\n\nHere is the information..\npropId:{}\ncustomerId:{}\nname:{}\ndescription:{}\nbuilderName:{}\nprice:{}\narea:{}\ncity:{}\nstate:{}\ncountry:{}\nlocality:{}\npincode:{}\nlat:{}\nlon:{}\ntype:{}\ncategory:{}\nlistingType:{}\nfurnishing:{}\npropType:{}\nhouseType:{}\npropAge:{}\n\n\n".format(userid,a, b, c, d, e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t))
                # dispatcher.utter_message("Here is the information	name:{}\n 	description: {}\n 	\n\n\n".format(userid,a))

        else:
            dispatcher.utter_message("No data found in the database, please try again.")
        conn.close()
        
        return []
    # def name(self):
    #     return 'action_insert_db'

    # def run(self, dispatcher: CollectingDispatcher, 
    #         tracker: Tracker, 
    #         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    #     mydb = mysql.connector.connect( host="206.189.142.4", user="root", passwd="Tech$321", database="realestate") 
    #     name = tracker.get_slot("name")
    #     type = tracker.get_slot("type") 
    #     phone = tracker.get_slot("number")
    #     pincode = tracker.get_slot("pincode")
    #     mycursor = mydb.cursor() 
    #     sql='INSERT INTO users (name, type, phone,pincode) VALUES ("{0}","{1}", "{2}","{3}");'.format(name, type ,phone,pincode) 
    #     mycursor.execute(sql) 
    #     mydb.commit()
    #     mydb.close()
    #     return []

# propId 	customerId 	name 	description 	builderName 	price 	area 	city 	state 	country 	locality 	pincode 	lat 	lon 	type 	category 	listingType 	furnishing 	propType 	houseType 	propAge 



 # This files contains your custom actions which can be used to run
# custom Python code.

# from typing import Any, Text, Dict, List, Union

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.forms import FormAction
# from rasa_core_sdk.events import Restarted
# import pymysql

# class ActionCuisineC(Action): 
# # search based on cuisine -> zip
#     def name(self) -> Text: 
#         #Unique identifier of the form
#         return "action_search_cuisine_zip"

#     def run(self, dispatcher: CollectingDispatcher, 
#             tracker: Tracker, 
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 

#         cuisine = tracker.get_slot("cuisine")
#         zip = tracker.get_slot("zip")

#         conn = pymysql.connect(
#             host="206.189.142.4", 
#             user="root", 
#             password="Tech$321", 
#             database="realestate"
#         )
#         cur = conn.cursor()
#         sql = 'SELECT * FROM loc_data WHERE foodtype LIKE "%{}%" AND zipcode LIKE "%{}%"'.format(cuisine, zip)
#         cur.execute(sql)
#         result = cur.fetchall()
#         if len(result) > 0:
#             for row in result:
#                 print('id: ', row[0])
#                 userid = row[1]
#                 a = row[2]
#                 b = row[3]
#                 c = row[4]
#                 d = row[5]
#                 e = row[6]
#                 f = row[7]

#                 dispatcher.utter_message("Here is the information\nname: {}\nAddress: {}\nZip: {}\nCity: {}\nState: {}\n\n".format(a, b, c, d, e))
#         else:
#             dispatcher.utter_message("No data found in the database, please try again.")
#         conn.close()
#         return []

# class ActionCuisineB(Action): 
# # search based on cuisine -> city
#     def name(self) -> Text: 
#         #Unique identifier of the form
#         return "action_search_cuisine_city"

#     def run(self, dispatcher: CollectingDispatcher, 
#             tracker: Tracker, 
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 

#         cuisine = tracker.get_slot("cuisine")
#         city = tracker.get_slot("city")

#         conn = pymysql.connect(
#             host="206.189.142.4", 
#             user="root", 
#             password="Tech$321", 
#             database="realestate"
#         )
#         cur = conn.cursor()
#         sql = 'SELECT * FROM loc_data WHERE foodtype LIKE "%{}%" AND city LIKE "%{}%"'.format(cuisine, city)
#         cur.execute(sql)
#         result = cur.fetchall()
#         if len(result) > 0:
#             for row in result:
#                 print('id: ', row[0])
#                 userid = row[1]
#                 a = row[2]
#                 b = row[3]
#                 c = row[4]
#                 d = row[5]
#                 e = row[6]
#                 f = row[7]

#                 dispatcher.utter_message("Here is the information\nname: {}\nAddress: {}\nZip: {}\nCity: {}\nState: {}\n\n".format(a, b, c, d, e))
#         else:
#             dispatcher.utter_message("No data found in the database, please try again.")
#         conn.close()
#         return []


# class ActionCuisineA(Action): 
# # search based on cuisine -> state
#     def name(self) -> Text: 
#         #Unique identifier of the form
#         return "action_search_cuisine_state"

#     def run(self, dispatcher: CollectingDispatcher, 
#             tracker: Tracker, 
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 

#         cuisine = tracker.get_slot("cuisine")
#         state = tracker.get_slot("state")

#         conn = pymysql.connect(
#             host="206.189.142.4", 
#             user="root", 
#             password="Tech$321", 
#             database="realestate"
#         )
#         cur = conn.cursor()
#         sql = 'SELECT * FROM loc_data WHERE foodtype LIKE "%{}%" AND state LIKE "%{}%"'.format(cuisine, state)
#         cur.execute(sql)
#         result = cur.fetchall()
#         if len(result) > 0:
#             for row in result:
#                 print('id: ', row[0])
#                 userid = row[1]
#                 a = row[2]
#                 b = row[3]
#                 c = row[4]
#                 d = row[5]
#                 e = row[6]
#                 f = row[7]

#                 dispatcher.utter_message("Here is the information\nname: {}\nAddress: {}\nZip: {}\nCity: {}\nState: {}\n\n".format(a, b, c, d, e))
#         else:
#             dispatcher.utter_message("No data found in the database, please try again.")
#         conn.close()
#         return []


# class ActionCuisine(Action): 
# # search based on cuisine -> state and zip
#     def name(self) -> Text: 
#         #Unique identifier of the form
#         return "action_search_cuisine_state_zip"

#     def run(self, dispatcher: CollectingDispatcher, 
#             tracker: Tracker, 
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 

#         cuisine = tracker.get_slot("cuisine")
#         state = tracker.get_slot("state")
#         zip = tracker.get_slot("zip")

#         print(cuisine, state, zip)

#         conn = pymysql.connect(
#             host="206.189.142.4", 
#             user="root", 
#             password="Tech$321", 
#             database="realestate"
#         )
#         cur = conn.cursor()
#         sql = 'SELECT * FROM loc_data WHERE foodtype LIKE "%{}%" AND state LIKE "%{}%" AND zipcode = "{}"'.format(cuisine, state, zip)
#         cur.execute(sql)
#         result = cur.fetchall()
#         if len(result) > 0:
#             for row in result:
#                 print('id: ', row[0])
#                 userid = row[1]
#                 a = row[2]
#                 b = row[3]
#                 c = row[4]
#                 d = row[5]
#                 e = row[6]
#                 f = row[7]

#                 dispatcher.utter_message("Here is the information\nname: {}\nAddress: {}\nZip: {}\nCity: {}\nState: {}\n\n".format(a, b, c, d, e))
#         else:
#             dispatcher.utter_message("No data found in the database, please try again.")
#         conn.close()
#         return []
        

# class ActionSearch(Action): 

#     def name(self) -> Text: 
#         #Unique identifier of the form
#         return "action_search_user"

#     def run(self, dispatcher: CollectingDispatcher, 
#             tracker: Tracker, 
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
            
#         Name = tracker.get_slot("name")
#         Gender = tracker.get_slot("gender")

#         conn = pymysql.connect(
#             host="206.189.142.4", 
#             user="root", 
#             password="Tech$321", 
#             database="realestate" 
#         )
#         cur = conn.cursor()
#         sql = 'SELECT * FROM user_info WHERE name ="{}"'.format(Name)
#         cur.execute(sql)
        
#         result = cur.fetchall()
#         dispatcher.utter_message("Here is the information {}\n".format(result))

#         conn.close()
#         return []

# class ActionSubmit(Action): 

#     def name(self) -> Text: 
#         #Unique identifier of the form
#         return "utter_submit"

#     def run(self, dispatcher: CollectingDispatcher, 
#             tracker: Tracker, 
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
            
#         name = tracker.get_slot("name")
#         type = tracker.get_slot("type") 
#         phone = tracker.get_slot("number")
#         pincode = tracker.get_slot("pincode")
        
        

#         conn = pymysql.connect(
#             host="206.189.142.4", 
#             user="root", 
#             password="Tech$321", 
#             database="realestate" 
#         )
#         cur = conn.cursor()
#         sql='INSERT INTO users (name, type, phone,pincode) VALUES ("{0}","{1}", "{2}","{3}");'.format(name, type, phone,pincode) 
#         # sql='INSERT INTO user_info (name, gender) VALUES ("{}","{}","{}","{}");'.format(Name, Gender) 
#         #sql='INSERT INTO user_info (name, gender, age, phonenumber) VALUES ("Ali","male","22","123");'
#         cur.execute(sql) 
#         conn.commit()
#         # some other statements  with the help of cursor
#         conn.close()
#         print("Success!")
#         dispatcher.utter_message("Thanks for the valuable feedback. ") 
#         return []

import mysql.connector
# from .database_connectivity import DataUpdate
from database_connectivity import DataUpdate
class UserForm(FormAction):
    """Custom form action to fill all slots required to find specific type
    of healthcare facilities in a certain city or zip code."""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "buy_form"
    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["name","number","pincode"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {
             "name": [self.from_entity(intent=user_details), self.from_text()],
             "number": [self.from_entity(intent=user_details), self.from_text()],
             "pincode": [self.from_text(intent=user_details), self.from_text()]
            #  "location": [self.from_entity(entity="location", intent="inform"), self.from_text()]
              }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],) -> List[Dict]:
        try:
            
            print("name:", tracker.get_slot('name'))
            print("number:", tracker.get_slot('number'))
            print("pincode:", tracker.get_slot('pincode'))
            # print("location:"+ tracker.get_slot('location'))
            # name = tracker.get_slot("name")
            # type = tracker.get_slot("type") 
            # phone = tracker.get_slot("number")
            # pincode = tracker.get_slot("pincode")
            # dispatcher.utter_template("utter_submit", tracker)  
            DataUpdate(tracker.get_slot("name") , tracker.get_slot("number"),tracker.get_slot("pincode"))
            dispatcher.utter_message("Thank you for providing all the details! we'll contact you soon")
        except:
            dispatcher.utter_message("Sorry! some internal error has occoured!")
        
        return []