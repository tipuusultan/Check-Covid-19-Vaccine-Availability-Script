# https://cdn-api.co-vin.in/api/v2​/appointment​/sessions​/public​/findByDistrict

import requests

base_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict"
dist_id = 49
date = "31-05-2021"

# Send to telegram
group_id = '-543656097'




base_request_header = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
        }
final_url = f'{base_url}?district_id={dist_id}&date={date}'
response = requests.get(final_url , headers=base_request_header)
print(response)
print(final_url)
print(response.text
