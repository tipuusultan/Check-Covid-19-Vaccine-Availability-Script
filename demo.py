# https://cdn-api.co-vin.in/api/v2​/appointment​/sessions​/public​/findByDistrict

import requests


# Send to telegram
group_id = '-543656097'



def fectch_data():
    tele_api_url = f'https://api.telegram.org/bot1789281332:AAEcL55TaDKQs3pSiQYN1h_FoRDmB-kdIOo/sendMessage?chat_id={group_id}&text="massage"'        
    tele_response = requests.get(tele_api_url)
    print("ok")

while True:
    fectch_data()
