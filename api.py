import requests
import random

def fetch_random_person():
    response = requests.get('https://randomuser.me/api/')
    if response.status_code == 200:
        data = response.json()
        person = data['results'][0]['name']['first']
        return person
    else:
        return None

def fetch_random_location():
    response = requests.get('https://api.teleport.org/api/cities/')
    if response.status_code == 200:
        data = response.json()
        city = random.choice(data['_links']['city:item'])['name']
        return city
    else:
        return None

def fetch_random_activity():
    response = requests.get('https://www.boredapi.com/api/activity/')
    if response.status_code == 200:
        data = response.json()
        activity = data['activity']
        return activity
    else:
        return None

def generate_sentence():
    days = random.randint(1, 100)  # Random number of days
    random_location = fetch_random_location()
    random_activity = fetch_random_activity()
    random_person = fetch_random_person()

    sentence = f"In {days} days, you'll be {random_activity} in {random_location} with {random_person}"
    return sentence

random_sentence = generate_sentence()
print(random_sentence)
