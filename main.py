# test
from concurrent.futures import ThreadPoolExecutor
import time
from turtle import heading
import requests
from pyfiglet import Figlet

#!urls_list = ['https://10minutemail.com',
#!            'https://temp-mail.org/',
#!             'https://www.guerrillamail.com', has params that change mailbox behavior
#!             'https://www.emailondeck.com', (Use burp to confirm the GET request headers)
#!              'https://tempmail.dev/en/Gmail',
#!             'https://smailpro.com/advanced', https://smailpro.com/api for the api- issues with key and email generation
#!             'https://www.gmailnator.com'] - no response from this site

# ? websites API list

#! urls_api = ['https://10minutemail.com/session/address',
#!            'https://web2.temp-mail.org/mailbox',
#!            'https://www.guerrillamail.com/ajax.php?f=check_email&seq=1&site=guerrillamail.com&in=jrtzcnnd&_=1662040663217',
#!            'https://tempmail.dev/GmailEmail/',
#!             '']

url = "https://10minutemail.com/session/address"  # url api to mine data from

# headers to prevent cloudflare blocking
headers = {"User-Agent": "Mozilla/5.0"}

mined_emails = []  # Collects list of mined emails

#!pyfiglet Intro
f = Figlet(font="banner3", justify="center")
print(f.renderText("A tool to mine Temp-mail addresses"))

email_num = int(input("Enter the number of emails to mine: "))

start_timer = time.time()

# ? fetch function querying the api. Counter prints the number of current email being mined


def fetch(url, headers=headers, counter=[0]):
    with requests.get(url, headers=headers) as response:
        counter[0] += 1
        #!modify "address" to match the JSON response from the email api
        print(f'{counter}', response.json()["address"])
        mined_emails.append(response.json()["address"])
    return counter[0]

# *Multithreading for performance


def main():
    with ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(fetch, [url] * int(email_num))
        executor.shutdown(wait=True)


if __name__ == "__main__":
    main()

end_timer = time.time()

print("Time took => ", end_timer - start_timer, "s")
