from ggs import Ggs

def add_entries(ggs, entries):
    for entry in entries:
        ggs.add_entry(entry)

def print_prob_table(table):
    print(f'%-16s %-18s %s' % ('Name', 'Gifts Received', 'Probability'))
    for entry in table:
        print(f'%-16s %-18d %-.4f%%' % (entry['name'], entry['gifts'], 100 * entry['probability']))

def run_probabilitic_test(ggs, n=100000):
    results = {}

    for user in ggs.users:
        results[user['name']] = 0

    for _ in range(n):
        winner = ggs.choose_winner()
        results[winner['name']] += 1

    for (name, win_ammount) in results.items():
        print(f'%-16s won %.4f%% of the time' % (name, 100 * win_ammount / n))


if __name__ == '__main__':
    ggs = Ggs(25000)

    add_entries(ggs, [
        {'name': 'Bran', 'points': 2180, 'gifts': 1},
        {'name': 'Sansa', 'points': 2340, 'gifts': 0},
        {'name': 'Arya', 'points': 3180, 'gifts': 2},
        {'name': 'Robb', 'points': 1180, 'gifts': 0},
        {'name': 'Jon', 'points': 2755, 'gifts': 3},
        {'name': 'Rickon', 'points': 390, 'gifts': 1},
    ])

    table = ggs.get_prob_table()

    # print_prob_table(table)
    # run_probabilitic_test(ggs)

    print("Probability table:")
    print_prob_table(table)

    winner = ggs.choose_winner()

    print("Winner is\033[32m", winner['name'], '\033[0m\n')

    print("Probability table (after winner chosen):")
    table = ggs.get_prob_table()
    print_prob_table(table)
    
