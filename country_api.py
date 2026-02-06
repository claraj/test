import requests 

def get_country_name(country_code):
    try:
        url = create_url(country_code)
        json_response = make_api_request(url)
        name = get_name_from_response(json_response)
        return name
    except:
        return 'Error, could not get capital city'
        

def create_url(country_code):
    url = f'https://api.worldbank.org/v2/country/{country_code}?format=json'
    return url


def make_api_request(url):
    response = requests.get(url)
    response.raise_for_status()
    json = response.json()  
    return json


def get_name_from_response(json_response):
    # The response is a dictionary with a name key, in a list in a list. 
    name = json_response[1][0]['name']
    return name
