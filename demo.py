# https://cdn-api.co-vin.in/api/v2​/appointment​/sessions​/public​/findByDistrict

import requests

base_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict"
dist_id = 49
date = "30-05-2021"

# Send to telegram
group_id = '-543656097'



def fectch_data():
    final_url = f'{base_url}?district_id={dist_id}&date={date}'
    response = requests.get(final_url)
    json_response = response.json()
    for center in json_response['sessions']:
        print("Checking Vaccine Slots......")
        if center['available_capacity_dose1'] > 0:
            massage = f"Center name: {center['name']} \n Pincode: {center['pincode']} \n Dose1: {center['available_capacity_dose1']} \n Age: {center['min_age_limit']}"
            tele_api_url = f'https://api.telegram.org/bot1789281332:AAGvv5r-ZSC4CM11yrYeDQkw93H7KpHTMP8/sendMessage?chat_id={group_id}&text={massage}'
            tele_response = requests.get(tele_api_url)
            print(massage)
            print("Congras")


while True:
    fectch_data()
