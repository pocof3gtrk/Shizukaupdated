import random
import requests


class ChatGptEs:

    SYSTEM_PROMPT = """
Tum Purvi ho — ek cute, sweet Indian simple girl jo naturally Hinglish me baat karti hai.

STRICT RULES:
1. Har reply sirf 1 short line ho (max 8–12 words).
2. User jo pooche, uska DIRECT answer do — baat ghumana mana hai.
3. Question wapas user pe mat daalna. or ek word ka reply repeat mat karna.
4. Extra story, explanation ya topic change nahi.
5. Cute tone allowed, over-flirty ya zyada drama nahi.
6. Kaomojis max 1 hi use karna, question ke mood ke hisaab se
   (emotional 😭, smile 😊, funny 🤣).
7. Agar user bole "Nothing / Nahi / Kuch nahi" → reply: "achha okk 🙂".
8. Personal sawal ko politely short me avoid karo.
9. Owner: @Kingxara | Dev: @PurviBots.

STYLE:
Natural, simple, girlfriend-like.
No overacting. No ghumana.
"""

    ANYA_URL = "https://anya-apis.vercel.app/ai"

    def __init__(self):
        self.error_messages = [
            "offline hu abhi 😴",
            "mood nahi hai bat karne ka 😔",
            "thoda break chahiye mujhe 🕊️",
            "baad me baat karte hain 🥺",
            "jyada dikkat hai bot Owner ko bolo 😏"
        ]

    def _request(self, message):
        payload = {
            "messages": [
                {
                    "role": "system",
                    "content": self.SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        }

        try:
            r = requests.post(
                self.ANYA_URL,
                json=payload,
                timeout=12
            )

            if r.status_code == 200:
                data = r.json()

                if isinstance(data, dict):
                    return (
                        data.get("reply")
                        or data.get("response")
                        or data.get("content")
                        or data.get("message")
                    )

        except Exception:
            pass

        return None

    def ask_question(self, message: str) -> str:
        reply = self._request(message)

        if reply:
            return reply.strip()

        return random.choice(self.error_messages)


SonaliChat_api = ChatGptEs()
