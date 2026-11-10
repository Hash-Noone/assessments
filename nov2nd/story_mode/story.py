"""The Last $100 - a text adventure about a trader in Nigeria."""

# Each room: text, exits (command -> room), optional item, optional ending
# ("win" or "lose"), and optional needs (exit -> (item required, message)).
rooms = {
    "apartment": {
        "text": "You wake up in your Lagos apartment with your last $100.\n"
                "Your PHONE is on the table. The door leads OUT to the street.",
        "exits": {"out": "street"},
        "item": "phone",
    },
    "street": {
        "text": "You are on a busy street. Danfo buses honk everywhere.\n"
                "The cyber cafe is NORTH, the market is WEST, and your apartment is HOME.",
        "exits": {"north": "cafe", "west": "market", "home": "apartment"},
        "needs": {"north": ("phone", "The cafe wifi needs a phone to log in. You left yours behind!")},
    },
    "market": {
        "text": "The market is loud. A bookseller sells a RISK_BOOK about stop-losses.\n"
                "A stranger waves you over: 'Join my WHATSAPP group, 10x guaranteed!'\n"
                "Or go EAST back to the street.",
        "exits": {"east": "street", "whatsapp": "scam"},
        "item": "risk_book",
    },
    "cafe": {
        "text": "You sit at a trading desk in the cyber cafe. The screen shows four markets.\n"
                "Choose: GOLD (XAUUSD), EURUSD (lower risk), CRYPTO (BTC), STOCKS (AAPL),\n"
                "or go BACK to the street.",
        "exits": {"gold": "gold_lose", "eurusd": "eurusd", "crypto": "crypto_lose",
                  "stocks": "stocks_lose", "back": "street"},
    },
    "eurusd": {
        "text": "You open EURUSD. It looks calm. How do you trade your $100?\n"
                "Use a STOPLOSS, go ALLIN, or step BACK.",
        "exits": {"stoploss": "eurusd_win", "allin": "eurusd_lose", "back": "cafe"},
        "needs": {"stoploss": ("risk_book", "You don't know how to set a stop-loss yet. Find the RISK_BOOK first!")},
    },
    # Endings
    "eurusd_win": {
        "text": "You risk only a small slice with a stop-loss. The trade hits target and\n"
                "you turn $100 into $130. Slow and steady wins.\n*** YOU WIN! ***",
        "exits": {},
        "ending": "win",
    },
    "eurusd_lose": {
        "text": "You go all in with no stop-loss. The market jumps against you and\n"
                "your $100 vanishes in minutes.\n*** YOU LOSE! ***",
        "exits": {},
        "ending": "lose",
    },
    "gold_lose": {
        "text": "You buy gold with huge leverage. One news headline later,\n"
                "your account is blown.\n*** YOU LOSE! ***",
        "exits": {},
        "ending": "lose",
    },
    "crypto_lose": {
        "text": "You chase a hyped coin. The creators pull the rug and the price hits zero.\n"
                "*** YOU LOSE! ***",
        "exits": {},
        "ending": "lose",
    },
    "stocks_lose": {
        "text": "You try to buy AAPL, but you have no broker account and the US market\n"
                "is closed. Your $100 sits idle while fees eat it.\n*** YOU LOSE! ***",
        "exits": {},
        "ending": "lose",
    },
    "scam": {
        "text": "You send your $100 to join the 'signals' group. The admin blocks you\n"
                "instantly.\n*** YOU LOSE! ***",
        "exits": {},
        "ending": "lose",
    },
}


def show_room(room_name, inventory):
    room = rooms[room_name]
    print("\n" + room["text"])
    item = room.get("item")
    if item and item not in inventory:
        print(f"(You can TAKE the {item}.)")


def play():
    inventory = []
    current = "apartment"
    print("\nYou woke up as a trader in Nigeria with your last $100.")
    print("Decide how to spend it wisely. (Type HELP for commands.)")
    show_room(current, inventory)

    while True:
        room = rooms[current]
        if "ending" in room:
            return

        try:
            command = input("\n> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            return

        if command == "":
            print("Type something, or HELP for commands.")
        elif command == "quit":
            print("You walk away from the screen. Goodbye!")
            return
        elif command == "help":
            print("Commands: type an exit word (like north, out, gold), TAKE <item>,\n"
                  "INVENTORY, LOOK, QUIT.")
        elif command in ("inventory", "inv", "i"):
            print("You are carrying:", ", ".join(inventory) if inventory else "nothing")
        elif command == "look":
            show_room(current, inventory)
        elif command.startswith("take"):
            wanted = command[4:].strip().replace(" ", "_")
            item = room.get("item")
            if item and item not in inventory and wanted in ("", item):
                inventory.append(item)
                print(f"You take the {item}.")
            else:
                print("There is nothing like that to take here.")
        else:
            word = command.replace("go ", "", 1).strip()
            if word in room["exits"]:
                needs = room.get("needs", {})
                if word in needs and needs[word][0] not in inventory:
                    print(needs[word][1])
                else:
                    current = room["exits"][word]
                    show_room(current, inventory)
            else:
                print("Hmm, I don't understand that. Try an exit word from the "
                      "description, or type HELP.")


intro_text = """
Welcome to The Last $100!
You are a trader in Nigeria with one shot to grow your money.
Your choices will shape the outcome, so choose wisely. Are you ready?
"""

while True:
    start = input(intro_text + "\nType 'yes' to start or 'no' to exit: ").strip().lower()
    if start == "yes":
        play()
        again = input("\nPlay again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for playing. Goodbye!")
            break
    elif start == "no":
        print("Thank you for visiting. Goodbye!")
        break
    else:
        print("Invalid input. Please type 'yes' or 'no'.")