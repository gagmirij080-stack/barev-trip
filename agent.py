import os
import json

class BarevTripAgent:
    def __init__(self):
        self.name = "Barev.trip AI Assistant"
        self.version = "2.0.0"
        self.tours_db = [
            {"id": 1, "name": "Գառնի և Գեղարդ", "region": "Կոտայք", "price_amd": 15000, "duration": "1 օր"},
            {"id": 2, "name": "Սևանա լիճ և Սևանավանք", "region": "Գեղարքունիք", "price_amd": 18000, "duration": "1 օր"},
            {"id": 3, "name": "Խոր Վիրապ և Արարատ", "region": "Արարատ", "price_amd": 16000, "duration": "1 օր"},
            {"id": 4, "name": "Տաթևի վանք (Քրիստոնեական հրաշք)", "region": "Սյունիք", "price_amd": 45000, "duration": "2 օր"},
            {"id": 5, "name": "Դիլիջան և Աղարծին", "region": "Տավուշ", "price_amd": 20000, "duration": "1 օր"},
            {"id": 6, "name": "Արենիի գինու տուր", "region": "Վայոց Ձոր", "price_amd": 22000, "duration": "1 օր"}
        ]

    def greet(self, lang="hy"):
        greetings = {
            "hy": "Բարև ձեզ! Ես Barev.trip-ի խելացի տուրիստական գործակալն եմ։ Ինչպ՞ես կարող եմ օգնել ձեզ բացահայտել Հայաստանը:",
            "ru": "Здравствуйте! Я умный туристический агент Barev.trip. Как я могу помочь вам открыть Армению?",
            "en": "Hello! I am the smart travel agent for Barev.trip. How can I help you discover Armenia today?"
        }
        return greetings.get(lang, greetings["hy"])

    def recommend_tour(self, preference="nature"):
        # Advanced recommendation logic based on client preference
        recommendations = {
            "history": [t for t in self.tours_db if t["id"] in [1, 3, 4]],
            "nature": [t for t in self.tours_db if t["id"] in [2, 5]],
            "wine": [t for t in self.tours_db if t["id"] in [6]]
        }
        return recommendations.get(preference, self.tours_db[:3])

    def calculate_trip_cost(self, tour_id, persons=1, include_hotel=False):
        tour = next((t for t in self.tours_db if t["id"] == tour_id), None)
        if not tour:
            return "Tour not found"
        
        base_cost = tour["price_amd"] * persons
        hotel_cost_per_person = 15000 if include_hotel else 0
        total = base_cost + (hotel_cost_per_person * persons)
        
        return {
            "tour": tour["name"],
            "persons": persons,
            "include_hotel": include_hotel,
            "total_amd": total,
            "currency": "AMD"
        }

if __name__ == "__main__":
    agent = BarevTripAgent()
    print(agent.greet("hy"))
    print("\nRecommended Tours (History & Culture):")
    print(json.dumps(agent.recommend_tour("history"), ensure_ascii=False, indent=2))
    print("\nSample Cost Calculation (Tour #1 for 2 persons with hotel):")
    print(json.dumps(agent.calculate_trip_cost(1, 2, True), ensure_ascii=False, indent=2))
