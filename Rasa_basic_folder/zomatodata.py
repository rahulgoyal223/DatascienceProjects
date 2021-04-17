import pandas as pd

WeOperate = ['New Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']
ZomatoData = pd.read_csv('zomato.csv',encoding = 'ISO-8859-1')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
ZomatoData['City']= ZomatoData['City'].apply(lambda s:s.lower() if type(s) == str else s)
ZomatoData['Cuisines']= ZomatoData['Cuisines'].apply(lambda s:s.lower() if type(s) == str else s)
ZomatoData['City'] = ZomatoData['City'].apply(lambda s:'nashik' if s=='nasik' else s)
ZomatoData['Price_Range'] = ZomatoData['Average Cost for two'].apply(lambda x: 'low' if x<300 else ('mid' if 300<=x<700 else 'high'))

restaurants='r'

def get_restaurant():
    return restaurants

def city_check(city):
    # Function to check if a city is serviceable or not
    operate = list(map(str.lower,WeOperate))
    if city.lower() in operate:return True
    else:return False

def get_price(price):
    if price not in ['high','mid','low'] and price.isnumeric():
        price=int(price)
        if price <300:price='low'
        elif price>700:price='high'
        else: price='medium'
    return price
        
def restaurant_search(city,cuisine, price):
    price = get_price(price);
    data = ZomatoData.loc[(ZomatoData['City']==city) & (ZomatoData['Price_Range']==price) & (ZomatoData['Cuisines'].str.contains(cuisine)),['Restaurant Name','Address','Aggregate rating','Average Cost for two']].sort_values(by='Aggregate rating',ascending=False).head(5)
    global restaurants
    restaurants=''
    restaurant_data = data.values.tolist()
    if len(restaurant_data)==0:restaurants= "No results found!"
    else :
        for restaurant in restaurant_data:
            restaurants=restaurants + "----{} in {} has been rated {}--- \n\n".format(restaurant[0],restaurant[1],restaurant[2])
    print(restaurants)

#print(city_check('new delhi'))
#restaurant_search('new delhi','chinese','mid')
#print(get_restaurant())
