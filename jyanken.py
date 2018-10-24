def print_hand(hand, name='キキ'):
    print(name + 'は' + hand + 'を出しました')

print('じゃんけんをはじめます')

player_name = input('プレイヤー名を入力してください：')

if player_name == '':
    print_hand('グー')

else:
    print_hand('グー', player_name) 