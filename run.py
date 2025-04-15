try:
    print("🧠 DEBUG: Starting run.py")
    from app.gymspotter_agent import handle_message
    print("✅ DEBUG: Imported handle_message")

    if __name__ == "__main__":
        print("💪 GymSpotterAI is live and waiting for your message...")
        user_id = "+14155550199"

        while True:
            try:
                user_input = input("You: ")
                print("✅ Received message from user, processing...")

                if user_input.lower() in ["exit", "quit"]:
                    print("👋 Exiting GymSpotterAI. See you next session!")
                    break

                response = handle_message(user_id, user_input)
                print(f"🏋️ GymSpotterAI: {response}\n")

            except Exception as inner_e:
                print(f"❌ INNER Error: {inner_e}")
                break

except Exception as outer_e:
    print(f"❌ OUTER Error: {outer_e}")



