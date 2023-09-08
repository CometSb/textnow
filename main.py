import requests
import datetime
import requests
import datetime
import time
import random
import string

def generate_random_string(length):
    letters_and_digits = string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

def send_message():
    url = "https://www.textnow.com/api/users/USERNAME GOES HERE/messages"
    current_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Content-Length": "275",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "PUT COOKIE HERE",
    "Origin": "https://www.textnow.com",
    "Pragma": "no-cache",
    "Sec-Ch-Ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "X-Csrf-Token": "PUT HERE",
    "X-Requested-With": "XMLHttpRequest",
    }
    success_count = 0
    while True:
        random_string1 = generate_random_string(3)
        random_string2 = generate_random_string(4)
        phone_number = f"850{random_string1}{random_string2}"
        current_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        message = "Sick Of Paying For Storage To Backup Your Pictures?\nWant A Free Way To Store Your Family Photos?\n\nMake An Account Here > https://cometbot.info\nOr If Your A Nerd Join Our Discord! > https://discord.gg/FASNfhRrXB"
        data = {
            "from_name": "",
            "has_video": False,
            "contact_value": f"+1{phone_number}",
            "message": f"{message}",
            "message_direction": 2,
            "message_type": 1,
            "read": 1,
            "new": True,
            "date": current_time
        }
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            success_count += 1
            print(f"Sent Message To {phone_number}\nTotal Successful Messages Sent: {success_count}")
        else:
            print(f"Non Working Number > {phone_number}")
        time.sleep(2.5)

if __name__ == "__main__":
    send_message()
