## All 3 variables affirm email
* greet
    - utter_greet
* restaurant_search{"location": "delhi","cuisine": "chinese","price":"mid"}
    - slot{"location": "delhi","cuisine": "chinese","price":"mid"}
    - action_search_restaurants
	- utter_check_email_results
* affirm
    - utter_ask_email
* enter_email
    - slot{"email": "test@gmail.com"}
    - action_send_email
	- utter_goodbye
	- action_slot_reset
## All 3 variables deny email
* greet
    - utter_greet
* restaurant_search{"location": "delhi","cuisine": "chinese","price":"mid"}
    - slot{"location": "delhi","cuisine": "chinese","price":"mid"}
    - action_search_restaurants
	- utter_check_email_results
* deny
    - utter_goodbye
    - action_slot_reset
## Not Serviceable Location
* greet
    - utter_greet
* restaurant_search{"location": "Nagaland"}
    - slot{"location": "Nagaland"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"email": null}
    - slot{"cuisine": null}
    - slot{"location": null}
    - slot{"price": null}
    - utter_ask_howcanhelp

## Cuisine and Location & affirm email
* restaurant_search{"cuisine": "Italian", "location": "Mumbai"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Mumbai"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_check_email_results
* affirm
    - utter_ask_email
* enter_email{"email": "test@gmil.com"}
    - slot{"email": "test2603@gmil.com"}
    - action_send_email
    - utter_goodbye
    - action_slot_reset
    - slot{"email": null}
    - slot{"cuisine": null}
    - slot{"location": null}
    - slot{"price": null}
