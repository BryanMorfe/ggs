from ggs import Ggs

def add_entries(ggs, entries):
    for entry in entries:
        ggs.add_entry(entry)

def print_entries(entries):
    print(f'\033[1;34m%-16s %-22s %s\033[0m' % ('Name', 'Points Earned Today', 'Gifts Received (7 days)'))
    for entry in entries:
        print(f'\033[32m%-16s\033[0m %-22d %d' % (entry['name'], entry['points'], entry['gifts']))

def print_prob_table(table):
    print(f'\033[1;34m%-16s %-18s %s\033[0m' % ('Name', 'Gifts Received', 'Probability'))
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

def determine_winners(n_gifts, ggs):
    for i in range(n_gifts):
        table = ggs.get_prob_table()
        print(i + 1, ") Probability table:")
        print_prob_table(table)

        winner = ggs.choose_winner()

        print("The winner is\033[32m", winner['name'], '\033[0m\n')

if __name__ == '__main__':

    GUILD_ACTIVITY_POINTS = 25000  # Change this number to the actual points to be given
    NUM_GIFTS             = 5      # Change this to the number of gifts to give
    USER_DATA             = [      # Set data of users that will participate below
        {'name': 'Bran', 'points': 2180, 'gifts': 1},
        {'name': 'Sansa', 'points': 2340, 'gifts': 0},
        {'name': 'Arya', 'points': 3180, 'gifts': 2},
        {'name': 'Robb', 'points': 1180, 'gifts': 0},
        {'name': 'Jon', 'points': 2755, 'gifts': 3},
        {'name': 'Rickon', 'points': 390, 'gifts': 1},
    ]

    print("                  \033[32m*** GGS ***\033[0m")
    print("          Number of gifts to be given:", NUM_GIFTS)
    print("Number of activity points earned by the guild:", GUILD_ACTIVITY_POINTS)
    print("Users participating:")
    print_entries(USER_DATA)
    print()

    ggs = Ggs(GUILD_ACTIVITY_POINTS)
    add_entries(ggs, USER_DATA)

    # Uncomment code to run probabilistic test 
    # print_prob_table(table)
    # run_probabilitic_test(ggs)

    """Running: call determine_winners and pass
       n_gifts = number of gifts to give given the above data
       ggs = The GGS instance
    """
    determine_winners(n_gifts=NUM_GIFTS, ggs=ggs)
    
