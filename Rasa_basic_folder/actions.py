from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import json

ZomatoData = pd.read_csv('zomato.csv')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate = ['New Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']
ZomatoData['Price_Range'] = ZomatoData['Average Cost for two'].apply(lambda x: 'low' if x<300 else ('mid' if 300<=x<700 else 'high'))  

def Citycheck(City):
    # Function to check if a city is serviceable or not
    if City.lower in list(map(str.lower,WeOperate)):
        return True
    else:
        return False

def RestaurantSearch(City,Cuisine, Price):
	TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (ZomatoData['City'].apply(lambda x: City.lower() in x.lower())) & (ZomatoData['Price_Range'].apply(lambda x: Price.lower() in x.lower()))]
	return TEMP[['Restaurant Name','Address','Average Cost for two','Aggregate rating']]

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		#config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
        price_range = tracker.get_slot('price')
		#Function city_check has been added to check the serviceability of a city
        city_check = Citycheck(City = loc)
        
        if city_check:    
            results = RestaurantSearch(City=loc,Cuisine=cuisine,Price = price_range)
            response=""
            if results.shape[0] == 0:
                response= "no results"
            else:
                for restaurant in RestaurantSearch(loc,cuisine,price_range).iloc[:5].iterrows():
                    restaurant = restaurant[1]
                    response=response + F"Found {restaurant['Restaurant Name']} in {restaurant['Address']} rated {restaurant['Address']} with avg cost {restaurant['Average Cost for two']} \n\n"
        else:
            response = "Sorry, this city is not serviceable."				
		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc)]

class ActionSendMail(Action):
	def name(self):
		return 'action_send_mail'

	def run(self, dispatcher, tracker, domain):
		MailID = tracker.get_slot('mail_id')
		sendmail(MailID,response)
		return [SlotSet('mail_id',MailID)]