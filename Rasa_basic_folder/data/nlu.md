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
- thanks

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
- hi
- hi
- hello
- namaste

## intent:enter_email
- [test@yahoo.com](email)
- email: [test@gmail.com](email)
- email address: [test@live.com](email)
- My email address is [test@gmail.com](email)

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines](cuisine:chinese) restaurants in the [New Delhi](location:Delhi)
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
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
- [Chinese](cuisine:chinese)
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate](price:mid) price range with [british](cuisine) food for [four](people:4) people
- can you book a table in [Delhi](location) in a [low](price) price range with [Italian](cuisine) food
- can you book a table in [Bangalore](location) in a [high](price) price range with [Mexican](cuisine) food
- can you book a table in [Bangalore](location) in a [mid](price) price range with [Mexican](cuisine) food
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- [Chinese](cuisine:chinese)
- show me restaurants
- [mumbai](location)
- [Italian](cuisine)
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)

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

## synonym:Delhi
- New Delhi

## synonym:Bangalore
- Bengaluru
- Banglore

## synonym:Gurgaon
- Gurugram
- Gudgaon
- Gurgao
- Gudgawa

## synonym:Allahabad
- Alahabad

## synonym:Mangalore
- Mangaluru

## synonym:Mumbai
- Bombay
- Bambai

## synonym:Mysore
- Mysuru

## synonym:Puducherry
- Pondicherry
- Pondi
- Puduchery

## synonym:Varanasi
- Banaras

## synonym:Vadodara
- Baroda

## synonym:Dehradun
- Deradun

## synonym:Vizag
- Vishakhapatnam
- Visakhapatnam
- Vishakapatnam

## synonym:Ludhiana
- Ludiana
- Ludhiyana
- Ludiyana

## synonym:Kanpur
- Kanpoor
- Cawnpore

## synonym:Kochi
- Cochin
- Ernakulam
- Eranakulam

## synonym:Indore
- Indoor

## synonym:Ahmedabad
- Amedabad

## synonym:Coimbatore
- Kovai

## synonym:Chennai
- Madras

## synonym:Guwahati
- Guwhati	
	
## synonym:Jaipur
- Pink City

## synonym:Pune
- Puna

## synonym:Kolkata
- Calcutta
- Calcuta

## synonym:Shimla
- Simla
- Shyamala

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:mid
- moderate
- medium
- affordable

## synonym:low
- cheap

## synonym:high
- expensive
- highend
- posh
- luxurious
- fancy

## synonym:vegetarian
- veggie
- vegg
- vegan

## regex:greet
- hey[^\s]*

## regex:location
- [0-9]{6}

## regex:enter_email
- [\w]+@[\w]+\.[\w]+