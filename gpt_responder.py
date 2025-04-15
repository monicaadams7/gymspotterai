import openai
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_set_feedback(exercise, reps, weight, form_score, muscles, phone_number):
    try:
        prompt = f"""
        A user just completed a set of {exercise}.
        
        Set details:
        - Reps: {reps}
        - Weight: {weight} lbs
        - Form score: {form_score:.1f}/10
        - Muscles hit: {', '.join(muscles)}

        Give short, specific, motivating feedback in the style of a casual text coach.
        """

        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a motivating, smart gym coach giving short feedback messages to a user via iMessage."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )

        return response.choices[0].message.content.strip()

    except Exception:
        return f"Nice! {reps} reps at {weight}lbs with form score {form_score}/10 🔥 Keep it up!"

# TEMP TEST BLOCK
if __name__ == "__main__":
    result = generate_set_feedback(
        exercise="squat",
        reps=10,
        weight=135,
        form_score=8.5,
        muscles=["quads", "glutes", "core"],
        phone_number="demo123"
    )
    print("GPT Feedback:\n", result)
