import random
import time

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def dungeon_escape():
    health = 100
    rooms = 5

    slow_print("\n🏰 WELCOME TO DUNGEON ESCAPE 🏰")
    slow_print("You are trapped inside a dark dungeon.")
    slow_print("Choose wisely to survive and escape!\n")

    for room in range(1, rooms + 1):
        if health <= 0:
            slow_print("💀 You have no health left. Game Over!")
            return

        slow_print(f"\n🚪 Room {room}")
        slow_print("Choose a door: [1] Left  [2] Middle  [3] Right")

        try:
            choice = int(input("Your choice (1-3): "))
            if choice not in [1, 2, 3]:
                raise ValueError
        except ValueError:
            slow_print("❌ Invalid choice! You lose 10 health.")
            health -= 10
            continue

        event = random.choice(["monster", "treasure", "trap"])

        if event == "monster":
            damage = random.randint(10, 30)
            health -= damage
            slow_print(f"👹 A monster attacks you! You lose {damage} health.")

        elif event == "trap":
            damage = random.randint(5, 20)
            health -= damage
            slow_print(f"⚠️ A hidden trap! You lose {damage} health.")

        else:
            heal = random.randint(10, 25)
            health += heal
            slow_print(f"💎 You found a health potion! You gain {heal} health.")

        slow_print(f"❤️ Current Health: {health}")

    slow_print("\n🎉 CONGRATULATIONS!")
    slow_print("You escaped the dungeon successfully! 🏆")

# Run the game
dungeon_escape()
