import requests
from config import Config

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"


class AIServiceError(Exception):
    pass


class AIService:

    def __init__(self):
        self.api_anahtari = Config.GROQ_API_KEY
        self.model = Config.AI_MODEL

    def _sistem_talimati(self):
        return Config.BUSINESS_CONTEXT

    def _groq_istegi(self, mesajlar):
        try:
            yanit = requests.post(
                GROQ_URL,
                headers={"Authorization": f"Bearer {self.api_anahtari}"},
                json={"model": self.model, "messages": mesajlar},
                timeout=30,
            )
            yanit.raise_for_status()
            return yanit.json()["choices"][0]["message"]["content"]
        except (requests.RequestException, KeyError, IndexError) as hata:
            raise AIServiceError(f"Yapay zekâ yanıt veremedi: {hata}")

    def yanit_uret(self, mesaj, gecmis=None):
        if not self.api_anahtari:
            return "Demo modu: Yapay zekâ anahtarı tanımlı değil. Lütfen GROQ_API_KEY ekleyin."

        mesajlar = [{"role": "system", "content": self._sistem_talimati()}]
        mesajlar += gecmis or []
        mesajlar.append({"role": "user", "content": mesaj})

        return self._groq_istegi(mesajlar)


ai_service = AIService()