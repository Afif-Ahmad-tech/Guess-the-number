import random

def play_game():
    secret_number = random.randint(1, 100)
    max_attempts = 7
    previous_guess = None

    print("\n🎮 NUMBER GUESSING GAME")
    print("Guess the number between 1 and 100.")
    print(f"You have {max_attempts} attempts.")

    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"\nAttempt {attempt}/{max_attempts}: "))

            if guess == secret_number:
                print("\n🎉 CONGRATULATIONS! YOU WON! 🎉")
                print(f"🏆 You guessed the number {secret_number}!")
                return

            difference = abs(secret_number - guess)

            if previous_guess is not None and (
                (previous_guess < secret_number < guess) or
                (guess < secret_number < previous_guess)
            ):
                hint = "⚡ JUST MISSED IT!"
            elif difference > 30:
                hint = "❄️ Very Far"
            elif difference > 15:
                hint = "🙂 Getting Closer"
            elif difference > 5:
                hint = "🔥 Nearby"
            else:
                hint = "🚨 Extremely Close!"

            if guess < secret_number:
                print(f"📉 Too Low! {hint}")
            else:
                print(f"📈 Too High! {hint}")

            previous_guess = guess

        except ValueError:
            print("❌ Enter a valid number.")

    print("\n💀 GAME OVER!")
    print(f"🎯 The correct number was {secret_number}")

while True:
    play_game()

    retry = input("\n🔄 Play Again? (y/n): ").lower()

    if retry != "y":
        print("👋 Thanks for playing!")
        break