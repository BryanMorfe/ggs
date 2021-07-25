from rand_generator import RandIntGenerator
import enum

class GgsConstants(enum.Enum):
    MaxRandInteger = 100000000
    MinPointsToEnter = 400
    GiftAdjustDivisor = 3.2667

class Ggs(object):

    def __init__(self, total_points):
        super().__init__()
        self.users = []
        self.total_points = total_points
        self.prob_table = None

    def add_entry(self, entry):
        if entry['points'] >= GgsConstants.MinPointsToEnter.value:
            self.users.append(entry)

    def _calc_prob_table(self):
        self.prob_table = []
        total_sum = 0.0

        # Initial probability
        for user in self.users:
            prob = user['points'] / self.total_points
            total_sum += prob
            self.prob_table.append({'name': user['name'], 'probability': prob, 'gifts': user['gifts']})

        # Normalize probability & calculate percentage to be distributed for to others (gifts received)
        all_pct_dist = []
        for i in range(len(self.prob_table)):
            self.prob_table[i]['probability'] /= total_sum
            t = self.prob_table[i]['gifts'] / GgsConstants.GiftAdjustDivisor.value
            all_pct_dist.append(t * self.prob_table[i]['probability'])

        # Calculate the adjustment needed per entry for gifts given
        adjust = [[] for _ in range(len(all_pct_dist))]
        for i in range(len(all_pct_dist)):
            if all_pct_dist[i] != 0:  # if 0, we can skip it because it will not be redistributed
                adjust[i].append(-all_pct_dist[i])
                total_minus_self = 1 - self.prob_table[i]['probability']
                for j in range(len(all_pct_dist)):
                    if i != j:
                        norm2 = self.prob_table[j]['probability'] / total_minus_self
                        adjust[j].append(norm2 * all_pct_dist[i])

        # Apply adjustments
        for i in range(len(adjust)):
            for j in range(len(adjust[i])):
                self.prob_table[i]['probability'] += adjust[i][j]    


    def get_prob_table(self):
        if self.prob_table is None:
            print('Calculating prob table')
            self._calc_prob_table()

        return self.prob_table


    def choose_winner(self):
        # Assign slots
        probabilities = self.get_prob_table()
        slots = []

        for i in range(len(probabilities)):
            entry = probabilities[i]
            hi_bound = round(GgsConstants.MaxRandInteger.value * entry['probability'])
            if i == 0:
                slots.append(hi_bound - 1)
            else:
                slots.append(slots[i - 1] + hi_bound)

        # Generate Number
        rand_int = RandIntGenerator.generate(max=GgsConstants.MaxRandInteger.value)
        winner = -1

        # Determine Winner
        for i in range(len(slots)):
            if rand_int <= slots[i]:
                winner = i
                break

        winner_entry = {'name': self.users[winner]['name'], 'points': self.users[winner]['points']}
        
        # Add gift received to winner for successive draws
        self.users[winner]['gifts'] += 1

        self.prob_table = None  # for recalculation upon request

        return winner_entry

