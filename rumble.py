from collections import defaultdict
import random


def get_partners(num_players, past_partners, max_attempts=10):
    remaining_players = list(range(num_players))
    partners = []

    for i in range(max_attempts):
        while remaining_players:
            p1 = remaining_players.pop()
            possible_partners = [p for p in remaining_players if p not in past_partners[p1]]

            if not possible_partners and i+1 < max_attempts:
                # case 1: only repeat partners left, but let's try again
                remaining_players = list(range(num_players))
                break
            else:
                if not possible_partners:
                    print('OUT OF ATTEMPTS')
                # case 2: we'll get a unique partner or we're out of attempts for uniqueness
                p2 = random.choice(remaining_players)
                remaining_players.remove(p2)
                partners.append((p1, p2))

        return partners


def main():
    num_players = int(input('How many people are playing? '))
    num_tables = num_players // 4
    num_rounds = int(input('How many rounds will you play? '))
    player_list = list(range(num_players))
    past_partners = defaultdict(list)

    for i in range(num_rounds):
        print(f'### Round {i} ###')
        partners = get_partners(num_players, past_partners)
        print(partners)

        # update past_partners
        for pair in partners:
            past_partners[pair[0]].append(pair[1])
            past_partners[pair[1]].append(pair[0])

        for j in range(num_tables):
            print(f'  ### Table {j} ###')
            pair1 = partners.pop()
            pair2 = partners.pop()
            print(f'  players {pair1[0]} and {pair1[1]} vs. players {pair2[0]} and {pair2[1]}\n')


if __name__ == '__main__':
    main()
