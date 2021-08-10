from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
import zomatodata as data
import sendemail as emailutility
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import json
from rasa_sdk.events import AllSlotsReset

class ActionSearchRestaurants(Action):
    
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        price_range = tracker.get_slot('price')

        dispatcher.utter_message("location: {} cuisine: {} price_range: {}".format(loc,cuisine,price_range))
        if data.city_check(loc):
            data.restaurant_search(city=loc.lower(),cuisine=cuisine.lower(),price = price_range.lower())
            dispatcher.utter_message(data.restaurant_data(data.get_restaurant(),5))
        else:
            dispatcher.utter_message("Sorry, this city is not serviceable.")
            return[SlotSet('email',None),SlotSet('cuisine',None),SlotSet('location',None),SlotSet('price',None)]

class ActionSendMail(Action):
    
    def name(self):
        return 'action_send_email'
        
    def run(self,dispatcher,tracker,domain):
        print('Sending email')
        mail_id = tracker.get_slot('email')
        dispatcher.utter_message(data.get_restaurant())
        dispatcher.utter_message(mail_id)
        emailutility.send_email(mail_id,data.restaurant_data(data.get_restaurant(),10))
        dispatcher.utter_message('Message sent successfully')
        return[AllSlotsReset()]

class AllSlotsReset(Action):
	def name(self):
		return 'action_slot_reset'
	def run(self, dispatcher, tracker, domain):
        return[SlotSet('email',None),SlotSet('cuisine',None),SlotSet('location',None),SlotSet('price',None)]