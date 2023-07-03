"""
Could not access Zillow API. Attempted to use RentCast, but reached free limit.
The API get and key do work though.
"""
#from requests import get
#
#API_KEY = '04cd46b6dbcd4e0d9f21ad86cb6bcdde'
#
#headers = {
#    'Accept': 'application/json',
#    'X-Api-Key': f'{API_KEY}',
#}
#
#params = {
#    'city': 'Austin',
#    'state': 'TX',
#    'limit': '20',
#}
#
#response = get('https://api.rentcast.io/v1/properties', params=params, headers=headers)
#
#print(response.json())
#
#class House():
#    var = 0