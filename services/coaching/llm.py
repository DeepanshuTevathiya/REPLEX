from services.config.workout_config import PROMPT

class LLMCoach:
    def __init__(self, client):
        self.client = client
        self.history = []
        self.system_prompt = PROMPT

    def give_feedback(self, event, issue):
        prompt = f"Event = {event}"

        if issue:
            prompt += f"\nForm Issue = {issue}"

        messages = [
            {"role": "system", "content": self.system_prompt},
            *self.history[-10:],
            {"role": "user", "content": prompt}
        ]
       
        response = self.client.chat.completions.create(
            model="google/gemma-3-4b-it",
            messages=messages,
            temperature=0.4,
        )

        text = response.choices[0].message.content.strip()
        self.history.append({"role": "assistant", "content": text})

        return text