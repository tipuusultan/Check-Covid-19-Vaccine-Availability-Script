from typing import final
import requests
from datetime import datetime




base_url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict'
get_time = datetime.now()
today_date = get_time.strftime("%d-%m-%Y")

telegram_api_url = 'http://api.telegram.org/bot1897518131:AAFfgUKGqsiZemRydjyOnDfD8KxKz9oKZmo/getUpdates'
telegram_chat_id = '-277765079'

while True:
    def fetch_data_from_api(district_id):
        query_param = '?district_id={}&date={}'.format(district_id, today_date)
        final_url = base_url+query_param
        base_request_header = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            }
        r = requests.get(final_url , headers=base_request_header)
        print(f"Checking Availability.......")
        check_availablity(r)


    def check_availablity(r):
        json_response = r.json()
        for j in json_response['sessions']:
            if j['available_capacity_dose1'] > 0:
                massage = "Pincode:{} , Name:{} , Slots:{} , Minimum Age:{}".format( 
                j['pincode'] , j['name'] , j['available_capacity_dose1'] , j["min_age_limit"] )
                print(massage)
                # send massage to telegram
                send_to_group = f'https://api.telegram.org/bot1897518131:AAFfgUKGqsiZemRydjyOnDfD8KxKz9oKZmo/sendMessage?chat_id={telegram_chat_id}&text={massage}'
                r = requests.get(send_to_group)
        
    if __name__ == "__main__":
        fetch_data_from_api(52)
