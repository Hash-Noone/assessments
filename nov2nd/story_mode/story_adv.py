"""The Last $100 - v2: trade, hustle, steal (carefully). Reach $500 to win."""
import random

START_MONEY = 100
TARGET = 500
MAX_HEAT = 3
RISK_PENALTY = 0.4   # win chance drops by up to 40 points at 100% risk
BOOK_BONUS = 0.08    # extra win chance from the risk book (cafe only)
HOODIE_BONUS = 0.15  # extra stealing success chance


def ending(kind, text):
    banner = "*** YOU WIN! ***" if kind == "win" else "*** YOU LOSE! ***"
    return {"text": f"{text}\n{banner}", "exits": {}, "ending": kind}


# Markets: name -> (label, base win chance, win payout, loss, as a fraction of the stake)
# Shops: item -> price. Buyers: item -> (min, max) resale price.
rooms = {
    "apartment": {
        "text": "You wake up in your Lagos apartment with your last $100.\n"
                "A PHONE and a black HOODIE are on the table. You can SLEEP to lay low.\n"
                "The door leads OUT to the street.",
        "exits": {"out": "street"},
        "items": ["phone", "hoodie"],
        "can_sleep": True,
    },
    "street": {
        "text": "You are on a busy street. Danfo buses honk everywhere.\n"
                "Cyber cafe: NORTH. Market: WEST. Bus park: SOUTH. Mall: EAST. Apartment: HOME.",
        "exits": {"north": "cafe", "west": "market", "south": "bus_park",
                  "east": "mall", "home": "apartment"},
        "needs": {"north": ("phone", "The cafe wifi needs a phone to log in. You left yours behind!")},
    },
    "market": {
        "text": "The market is loud. A bookseller sells a RISK_BOOK about stop-losses ($15).\n"
                "You can BUY it, TRADE goods (garri, phones), SELL things you bought at the mall,\n"
                "or STEAL from a distracted stall.\n"
                "A stranger waves: 'Join my WHATSAPP group, 10x guaranteed!'\n"
                "Go EAST to return to the street.",
        "exits": {"east": "street", "whatsapp": "scam"},
        "shop": {"risk_book": 15},
        # Buyers pay a random price in this range for goods bought at the mall.
        "buyers": {"sneakers": (32, 48), "perfume": (18, 28), "sunglasses": (12, 20)},
        "markets": {
            "garri": ("Garri sacks (safe)", 0.85, 0.15, 0.10),
            "phones": ("Used phones (riskier)", 0.60, 0.60, 0.40),
        },
        "steal": {"chance": 0.50, "min": 10, "max": 25, "heat": 1, "fine": 15,
                  "win": "You slip a wad of naira from a busy stall.",
                  "lose": "A trader grabs your wrist and shouts 'Thief!'"},
    },
    "cafe": {
        "text": "You sit at a trading desk in the cyber cafe. Type TRADE to see the markets,\n"
                "or WORK behind the counter for steady pay.\n"
                "Go BACK to the street when you are done.",
        "exits": {"back": "street"},
        "book_bonus": True,
        "work": {"min": 5, "max": 9,
                 "text": "You print documents, reset the wifi and fix a frozen PC."},
        "markets": {
            "eurusd": ("EURUSD (lower risk)", 0.65, 0.80, 0.50),
            "stocks": ("AAPL stock (slow and steady)", 0.60, 0.50, 0.30),
            "gold": ("Gold XAUUSD (high risk)", 0.50, 1.50, 1.00),
            "btc": ("Bitcoin (wild)", 0.35, 3.00, 1.00),
        },
    },
    "bus_park": {
        "text": "Danfo drivers are shouting 'Oshodi! Yaba! Ikeja!'\n"
                "You can WORK as a conductor for small, safe pay, or STEAL from the crowded queue.\n"
                "Go NORTH to return to the street.",
        "exits": {"north": "street"},
        "work": {"min": 4, "max": 8,
                 "text": "You shout destinations and collect fares all afternoon."},
        "steal": {"chance": 0.45, "min": 8, "max": 20, "heat": 1, "fine": 12,
                  "win": "You lift a purse from the packed danfo queue.",
                  "lose": "A conductor spots you and the passengers start shouting!"},
    },
    "mall": {
        "text": "A shiny mall with security guards and rich shoppers.\n"
                "You can BUY sneakers ($25), perfume ($15) or sunglasses ($8) to resell at the market,\n"
                "or try to STEAL a luxury item. Big reward, big risk.\n"
                "Go WEST to return to the street.",
        "exits": {"west": "street"},
        "shop": {"sneakers": 25, "perfume": 15, "sunglasses": 8},
        "steal": {"chance": 0.35, "min": 40, "max": 90, "heat": 2, "fine": 30,
                  "win": "You walk out with a designer watch and sell it quickly.",
                  "lose": "Security tackles you at the exit!"},
    },
    # Endings
    "win_500": ending("win", "You hit $500! You rent a better flat and buy proper charts. "
                             "The hustle paid off."),
    "broke": ending("lose", "You are out of money. Back to square one."),
    "jail": ending("lose", "Too much heat. The police pick you up. Your trading career ends in a cell."),
    "scam": ending("lose", "You send your money to join the 'signals' group. The admin blocks you instantly."),
}


def fmt(amount):
    sign = "-" if amount < 0 else ""
    return f"{sign}${abs(amount):,.2f}"


def loss_report(before, after):
    print(f"Before: {fmt(before)} -> Now: {fmt(after)} (difference: -{fmt(before - after)})")
    if after < 0:
        print(f"You can't cover it. You are now {fmt(abs(after))} in debt!")


def status(state):
    print(f"[Money: {fmt(state['money'])} / {fmt(TARGET)} | Heat: {state['heat']}/{MAX_HEAT}]")


def show_room(state):
    room = rooms[state["room"]]
    print("\n" + room["text"])
    items = [i for i in room.get("items", []) if i not in state["inv"]]
    if items:
        print("(You can TAKE: " + ", ".join(items) + ".)")


def check_end(state):
    if state["money"] >= TARGET:
        return "win_500"
    if state["money"] <= 0:
        return "broke"
    if state["heat"] >= MAX_HEAT:
        return "jail"
    return None


def do_trade(state, room, parts):
    markets = room.get("markets")
    if not markets:
        print("There is nothing to trade here.")
        return
    if len(parts) < 3:
        print("Usage: TRADE <market> <percent of your money to risk>   e.g. trade eurusd 20")
        for name, (label, base, win, loss) in markets.items():
            print(f"  {name}: {label} | base win chance {int(base * 100)}%, "
                  f"win +{int(win * 100)}% / lose -{int(loss * 100)}% of stake")
        print("Tip: the more of your money you risk, the lower your chance of winning.")
        return
    name = parts[1]
    if name not in markets:
        print("I don't know that market. Type TRADE to see the list.")
        return
    try:
        pct = int(parts[2].rstrip("%"))
    except ValueError:
        print("Please give the risk as a whole number from 1 to 100.")
        return
    if not 1 <= pct <= 100:
        print("Risk must be between 1 and 100 percent.")
        return

    label, base, win_ratio, loss_ratio = markets[name]
    chance = base - RISK_PENALTY * (pct / 100)
    if room.get("book_bonus") and "risk_book" in state["inv"]:
        chance += BOOK_BONUS
    chance = min(0.95, max(0.05, chance))

    stake = round(state["money"] * pct / 100, 2)
    print(f"You risk {fmt(stake)} on {label}. Win chance: {int(round(chance * 100))}%.")
    if random.random() < chance:
        gain = round(stake * win_ratio, 2)
        state["money"] = round(state["money"] + gain, 2)
        print(f"WIN! You make {fmt(gain)}.")
    else:
        loss = round(stake * loss_ratio, 2)
        before = state["money"]
        state["money"] = max(0, round(before - loss, 2))
        print(f"LOSS. You lose {fmt(loss)}.")
        loss_report(before, state["money"])


def do_steal(state, room):
    cfg = room.get("steal")
    if not cfg:
        print("Nothing worth stealing here, and you should be ashamed for asking. :)")
        return
    chance = cfg["chance"] + (HOODIE_BONUS if "hoodie" in state["inv"] else 0)
    chance = min(0.9, chance)
    if random.random() < chance:
        loot = random.randint(cfg["min"], cfg["max"])
        state["money"] = round(state["money"] + loot, 2)
        print(f"{cfg['win']} You gain {fmt(loot)}.")
    else:
        before = state["money"]
        fine = cfg["fine"]
        state["money"] = round(before - fine, 2)
        state["heat"] += cfg["heat"]
        print(f"{cfg['lose']} You lose {fmt(fine)} and the heat rises!")
        loss_report(before, state["money"])


def do_work(state, room):
    cfg = room.get("work")
    if not cfg:
        print("There is no work to do here.")
        return
    pay = random.randint(cfg["min"], cfg["max"])
    state["money"] = round(state["money"] + pay, 2)
    print(f"{cfg['text']} You earn {fmt(pay)}.")


def do_buy(state, room, parts):
    shop = room.get("shop")
    if not shop:
        print("Nothing is for sale here.")
        return
    item = "_".join(parts[1:])
    if not item:
        print("For sale: " + ", ".join(f"{n} ({fmt(p)})" for n, p in shop.items()))
        print("Usage: BUY <item>")
        return
    if item not in shop:
        print("They don't sell that here. Type BUY to see what's available.")
        return
    price = shop[item]
    if item == "risk_book" and "risk_book" in state["inv"]:
        print("You already own the risk book.")
        return
    if state["money"] <= price:
        print(f"That costs {fmt(price)} and you would be left with nothing. Not worth the risk!")
        return
    state["money"] = round(state["money"] - price, 2)
    state["inv"].append(item)
    print(f"You buy {item} for {fmt(price)}.")


def do_sell(state, room, parts):
    buyers = room.get("buyers")
    if not buyers:
        print("Nobody here wants to buy your things.")
        return
    wanted = "_".join(parts[1:])
    goods = [i for i in state["inv"] if i in buyers]
    if not goods:
        print("You have nothing the traders here want. Try buying goods at the mall.")
        return
    if wanted == "":
        print("Usage: SELL <item> or SELL ALL. Buyers want: " + ", ".join(sorted(set(goods))))
        return
    to_sell = goods if wanted == "all" else [i for i in goods if i == wanted][:1]
    if not to_sell:
        print("You don't have that, or they don't buy it. Check INVENTORY.")
        return
    total = 0
    for item in to_sell:
        low, high = buyers[item]
        price = random.randint(low, high)
        state["inv"].remove(item)
        total += price
        print(f"You sell {item} for {fmt(price)}.")
    state["money"] = round(state["money"] + total, 2)


def inventory_text(inv):
    if not inv:
        return "nothing"
    counts = {}
    for item in inv:
        counts[item] = counts.get(item, 0) + 1
    return ", ".join(f"{n} x{c}" if c > 1 else n for n, c in counts.items())


def play():
    state = {"room": "apartment", "inv": [], "money": START_MONEY, "heat": 0}
    print("\nYou woke up as a trader in Nigeria with your last $100.")
    print(f"Grow it to {fmt(TARGET)} to win. Hit $0 and you lose. (Type HELP for commands.)")
    show_room(state)
    status(state)

    while True:
        room = rooms[state["room"]]
        if "ending" in room:
            return

        try:
            command = input("\n> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            return

        parts = command.split()
        verb = parts[0] if parts else ""

        if not parts:
            print("Type something, or HELP for commands.")
        elif verb == "quit":
            print("You walk away from the screen. Goodbye!")
            return
        elif verb == "help":
            print("Commands: exit words (north, out, back...), TAKE <item>, INVENTORY, LOOK,\n"
                  "TRADE <market> <percent>, BUY <item>, SELL <item|all>, STEAL, WORK, SLEEP,\n"
                  "STATUS, QUIT.")
        elif verb in ("inventory", "inv", "i"):
            print("You are carrying:", inventory_text(state["inv"]))
        elif verb == "look":
            show_room(state)
        elif verb == "status":
            status(state)
        elif verb == "take":
            wanted = "_".join(parts[1:])
            available = [i for i in room.get("items", []) if i not in state["inv"]]
            picks = available if wanted == "" else [i for i in available if i == wanted]
            if picks:
                state["inv"].extend(picks)
                print("You take: " + ", ".join(picks) + ".")
            else:
                print("There is nothing like that to take here.")
        elif verb == "trade":
            do_trade(state, room, parts)
        elif verb == "buy":
            do_buy(state, room, parts)
        elif verb == "sell":
            do_sell(state, room, parts)
        elif verb == "steal":
            do_steal(state, room)
        elif verb == "work":
            do_work(state, room)
        elif verb == "sleep":
            if room.get("can_sleep"):
                state["heat"] = max(0, state["heat"] - 1)
                print("You lie low and sleep. The heat cools down a little.")
            else:
                print("You can only sleep at home.")
        else:
            word = command.replace("go ", "", 1).strip()
            if word in room["exits"]:
                needs = room.get("needs", {})
                if word in needs and needs[word][0] not in state["inv"]:
                    print(needs[word][1])
                else:
                    state["room"] = room["exits"][word]
                    show_room(state)
            else:
                print("Hmm, I don't understand that. Try an exit word from the "
                      "description, or type HELP.")

        outcome = check_end(state)
        if outcome and "ending" not in rooms[state["room"]]:
            state["room"] = outcome
            show_room(state)
        if "ending" not in rooms[state["room"]]:
            status(state)
        else:
            print(f"Final balance: {fmt(state['money'])}")
            if state["money"] < 0:
                print(f"You finish {fmt(abs(state['money']))} in debt.")


intro_text = """
Welcome to The Last $100 (v2)!
You are a trader in Nigeria. Trade smart, hustle safely, or steal and risk the heat.
Reach $500 to win. Hit $0 or get arrested and you lose. Are you ready?
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