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
## All 3 variables deny email
* greet
    - utter_greet
* restaurant_search{"location": "delhi","cuisine": "chinese","price":"mid"}
    - slot{"location": "delhi","cuisine": "chinese","price":"mid"}
    - action_search_restaurants
	- utter_check_email_results
* deny
    - utter_goodbye
## 2 variables: Location, Cuisine affirm email
* greet
    - utter_greet
* restaurant_search{"location": "delhi","cuisine": "chinese"}
    - slot{"location": "delhi","cuisine": "chinese"}
	- utter_ask_price
* restaurant_search{"price": "mid"}
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
## location specified
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* affirm
    - utter_goodbye
    - export

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_goodbye

## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* goodbye
    - utter_goodbye

## complete path 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - export


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* stop

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "mumbai"}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye
    
    
## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* affirm
    - utter_goodbye


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye
