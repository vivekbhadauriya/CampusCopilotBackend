import json
import os

def load_json(filename):
    path = os.path.join(os.path.dirname(__file__), '..', 'local_data', filename)
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

faqs = load_json('faqs.json')
food_places = load_json('food_places.json')

def search_faqs(query):
    for faq in faqs:
        if faq["question"].lower() in query.lower():
            return faq["answer"]
    return None

def search_food(query):
    for food in food_places:
        if food["query"].lower() in query.lower():
            return food["answer"]
    return None