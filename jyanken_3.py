def validate(hand):
    if hand < 0 or hand > 2:
        return False
    return True

def print_hand(hand, name="ゲスト"):
    hands = ["ぐー","ちょき","ぱー"]
    print(name + "は" + hands[hand] + "を出しました")

    