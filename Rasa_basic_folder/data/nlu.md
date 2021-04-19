## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- cool

## intent:deny
- no
- not interested
- dismiss
- disapprove
- nah
- n

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- namaste
- Hi

## intent:enter_email
- [test@yahoo.com](email)
- email: [test@gmail.com](email)
- email address: [test@live.com](email)
- My email address is [test@gmail.com](email)
- email [test@gmail.com](email)
- [sumiran2603@gmil.com](email)

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [New Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [Delhi]{"entity": "location", "value": "New Delhi"}
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [North Indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking a restaurant in [455462](location)
- I am looking a restaurant in [455452](location)
- I am looking a restaurant in [658555](location)
- I am looking a restaurant in [812444](location)
- I am looking a restaurant in [951242](location)
- I am looking a restaurant in [142416](location)
- I am looking a restaurant in [248275](location)
- I am looking a restaurant in [399689](location)
- I am looking for [asian fusion](cuisine) food
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate]{"entity": "price", "value": "mid"} price range with [british](cuisine) food for [four]{"entity": "people", "value": "4"} people
- can you book a table in [Delhi](location) in a [low](price) price range with [Italian](cuisine) food
- can you book a table in [Bangalore](location) in a [high](price) price range with [Mexican](cuisine) food
- can you book a table in [Bangalore](location) in a [mid](price) price range with [Mexican](cuisine) food
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurant in [bangalore](location)
- [mumbai](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- please find [mid](price) [Mexican](cuisine) restaurant in [delhi](location)
- [Bengaluru]{"entity": "location", "value": "Bangalore"}
- [Banglore]{"entity": "location", "value": "Bangalore"}
- please find me a [posh]{"entity": "price", "value": "high"} [Mexican](cuisine) restaurant
- please find me a [cheap]{"entity": "price", "value": "low"} [South Indian](cuisine) restaurant
- can you book a table in [Bangalore](location) in a [affordable]{"entity": "price", "value": "mid"} price range with [Italian](cuisine) food
- Find me a restaurant
- Find a restaurant in [Nagaland](location)
- [Mexican](cuisine)
- [mid](price)
- Find me a restaurant in [Nagaland](location)
- [high](price)
- Find me  [Chinese]{"entity": "cuisine", "value": "chinese"} restaurant in Assam
- Find me an [Italian](cuisine) restaurant in [Mumbai](location)
- [high](price)

## intent:out_of_scope
- What is 2 + 2?
- Who's the US President?

## synonym:1
- one

## synonym:2
- two

## synonym:3
- three

## synonym:4
- four

## synonym:5
- five

## synonym:6
- six

## synonym:7
- seven

## synonym:8
- eight

## synonym:9
- nine

## synonym:Allahabad
- Alahabad

## synonym:Bangalore
- Bengaluru
- Banglore

## synonym:Chennai
- Madras

## synonym:Coimbatore
- Kovai

## synonym:Dehradun
- Deradun

## synonym:Gurgaon
- Gurugram
- Gudgaon
- Gurgao
- Gudgawa

## synonym:Guwahati
- Guwhati

## synonym:Jaipur
- Pink City

## synonym:Kanpur
- Kanpoor
- Cawnpore

## synonym:Kochi
- Cochin
- Ernakulam
- Eranakulam

## synonym:Kolkata
- Calcutta
- Calcuta

## synonym:Ludhiana
- Ludiana
- Ludhiyana
- Ludiyana

## synonym:Mangalore
- Mangaluru

## synonym:Mumbai
- Bombay
- Bambai

## synonym:Mysore
- Mysuru

## synonym:Nashik
- Nasik

## synonym:New Delhi
- Delhi

## synonym:Puducherry
- Pondicherry
- Pondi
- Puduchery

## synonym:Pune
- Puna

## synonym:Shimla
- Simla
- Shyamala

## synonym:Vadodara
- Baroda

## synonym:Varanasi
- Banaras

## synonym:Vizag
- Vishakhapatnam
- Visakhapatnam
- Vishakapatnam

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:high
- posh
- expensive
- highend
- luxurious
- fancy

## synonym:low
- cheap

## synonym:mid
- moderate
- affordable
- medium

## synonym:vegetarian
- veggie
- vegg
- vegan

## regex:enter_email
- ^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$

## regex:greet
- hey[^\s]*

## regex:location
- [0-9]{6}
