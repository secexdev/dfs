import requests

OPENDNS_API_URL = 'https://api.opendns.com/v1/domains'

# Function to fetch category for a domain from OpenDNS
def get_domain_category(domain):
    response = requests.get(f'{OPENDNS_API_URL}/{domain}')
    if response.status_code == 200:
        data = response.json()
        return data.get('category', 'General')
    return 'General'
