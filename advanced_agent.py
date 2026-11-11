import json
from datetime import datetime

class AdvancedBarevAgent:
    def __init__(self):
        self.name = "Barev.trip AI Concierge"
        self.version = "3.5.0"
        self.knowledge_base = {
            "attractions": {
                "garni": "Единственный сохранившийся языческий храм I века в Армении с симфонией камней.",
                "geghard": "Уникальный пещерный монастырь XII века, высеченный в цельной скале (ЮНЕСКО).",
                "sevan": "Одно из крупнейших высокогорных пресноводных озер в мире, «Гегамское море»."
            },
            "faq": {
                "visa": "Гражданам большинства стран виза в Армению не требуется.",
                "currency": "Национальная валюта — армянский драм (AMD). Везде принимают карты и наличные.",
                "best_time": "Лучшее время для поездок — с мая по октябрь, но зимой здесь прекрасны горнолыжные курорты (Цахкадзор)."
            }
        }

    def process_query(self, user_text, lang="ru"):
        user_text = user_text.lower()
        
        if "garni" in user_text or "гарни" in user_text:
            return self.knowledge_base["attractions"]["garni"]
        elif "sevan" in user_text or "севан" in user_text:
            return self.knowledge_base["attractions"]["sevan"]
        elif "visa" in user_text or "виза" in user_text:
            return self.knowledge_base["faq"]["visa"]
        elif "currency" in user_text or "деньги" in user_text or "валюта" in user_text:
            return self.knowledge_base["faq"]["currency"]
        else:
            responses = {
                "ru": "Я готов помочь вам с подбором тура по Армении, рассказать о достопримечательностях или рассчитать стоимость поездки. Что вас интересует?",
                "hy": "Ես պատրաստ եմ օգնել ձեզ ընտրել տուր Հայաստանում, պատմել տեսարժան վայրերի մասին կամ հաշվել արժեքը:",
                "en": "I am ready to help you plan your trip in Armenia, recommend attractions, or calculate tour costs. What are you looking for?"
            }
            return responses.get(lang, responses["ru"])

    def create_itinerary(self, client_name, days=3, interests="culture"):
        itinerary = {
            "client": client_name,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "duration_days": days,
            "focus": interests,
            "schedule": [
                {"day": 1, "title": "Ереван и окрестности", "activities": ["Обзорная экскурсия по Еревану", "Вернисаж", "Каскад"]},
                {"day": 2, "title": "Гарни, Гегард и Симфония камней", "activities": ["Языческий храм Гарни", "Монастырь Гегард", "Обед с лавашом"]},
                {"day": 3, "title": "Озеро Севан", "activities": ["Монастырь Севанаванк", "Дегустация севанской рыбы"]}
            ]
        }
        return itinerary

if __name__ == "__main__":
    bot = AdvancedBarevAgent()
    print("--- AI AGENT TEST ---")
    print("Query about Garni:", bot.process_query("Tell me about Garni"))
    print("\nCustom Itinerary for Anna:")
    print(json.dumps(bot.create_itinerary("Anna Smith", 3, "history"), ensure_ascii=False, indent=2))
