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
## 2 variables: Location, Cuisine affirm email
* greet
    - utter_greet
* restaurant_search{"location": "delhi","cuisine": "chinese"}
    - slot{"location": "delhi","cuisine": "chinese"}
	- utter_ask_price
    - slot{"price": "mid"}
	- action_search_restaurants
	- utter_check_email_results
* affirm
    - utter_ask_email
* enter_email
    - slot{"email": "test@gmail.com"}
    - action_send_email
	- utter_goodbye
## 2 variables: Location, Cuisine deny email
* greet
    - utter_greet
* restaurant_search{"location": "delhi","cuisine": "chinese"}
    - slot{"location": "delhi","cuisine": "chinese"}
	- utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
	- action_search_restaurants
	- utter_check_email_results
* deny
    - utter_goodbye
    - action_slot_reset	
## 2 variables: Location, Price affirm email
* greet
    - utter_greet
* restaurant_search{"location": "delhi","price": "high"}
    - slot{"location": "delhi","price": "high"}
	- utter_ask_cuisine
    - slot{"cuisine": "chinese"}
	- action_search_restaurants
	- utter_check_email_results
* affirm
    - utter_ask_email
* enter_email
    - slot{"email": "test@gmail.com"}
    - action_send_email
	- utter_goodbye
	- action_slot_reset
## 2 variables: Location, Price deny email
* greet
    - utter_greet
* restaurant_search{"location": "delhi","price": "high"}
    - slot{"location": "delhi","price": "high"}
	- utter_ask_cuisine
    - slot{"cuisine": "chinese"}
	- action_search_restaurants
	- utter_check_email_results
* deny
    - utter_goodbye
    - action_slot_reset
## 2 variables: Cuisine, Price affirm email
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese","price": "high"}
    - slot{"cuisine": "chinese","price": "high"}
	- utter_ask_location
    - slot{"location": "delhi"}
	- action_search_restaurants
	- utter_check_email_results
* affirm
    - utter_ask_email
* enter_email
    - slot{"email": "test@gmail.com"}
    - action_send_email
	- utter_goodbye
	- action_slot_reset
## 2 variables: Cuisine, Price deny email
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese","price": "high"}
    - slot{"cuisine": "chinese","price": "high"}
	- utter_ask_location
    - slot{"location": "delhi"}
	- action_search_restaurants
	- utter_check_email_results
* deny
    - utter_goodbye
    - action_slot_reset
## 1 variable: Cuisine affirm email
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_location
    - slot{"location": "delhi"}
    - utter_ask_price
    - slot{"price": "high"}
	- action_search_restaurants
	- utter_check_email_results
* affirm
    - utter_ask_email
* enter_email
    - slot{"email": "test@gmail.com"}
    - action_send_email
	- utter_goodbye
	- action_slot_reset
## 1 variable: Cuisine deny email
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_location
    - slot{"location": "delhi"}
    - utter_ask_price
    - slot{"price": "high"}
	- action_search_restaurants
	- utter_check_email_results
* deny
    - utter_goodbye
    - action_slot_reset
## No variable: affirm email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_cuisine
    - slot{"cuisine": "chinese"}
* restaurant_search
	- utter_ask_location
    - slot{"location": "delhi"}
* restaurant_search
    - utter_ask_price
    - slot{"price": "high"}
	- action_search_restaurants
* affirm
    - utter_ask_email
* enter_email
    - slot{"email": "test@gmail.com"}
    - action_send_email
	- utter_goodbye
## No variable: deny email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_cuisine
    - slot{"cuisine": "chinese"}
	- utter_ask_location
    - slot{"location": "delhi"}
    - utter_ask_price
    - slot{"price": "high"}
	- action_search_restaurants
	- utter_check_email_results
* deny
    - utter_goodbye
    - action_slot_reset