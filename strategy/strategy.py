import csv

class Strategy():

    def __init__(self, player):
        self.player = player

        self.hard_hand = self.build_dict("strategy/hard_hand.csv")
        self.soft_hand = self.build_dict("strategy/soft_hand.csv")
        self.split_hand = self.build_dict("strategy/split_hand.csv")

    def check_hand(self):
        hand_value = 0

        for card in self.player.hand:
            if card == 'A':
                self.soft_hand = True

            hand_value += card.value

        return hand_value
    
    def get_start_number(self, file_name):
        with open(file_name, 'r') as csv_file:
            count = 0
            reader = csv.reader(csv_file)
            
            for line in reader:
                if count == 1:
                    # grabs first number in csv to start array
                    start = int(line[0])
                    break
                count += 1
        return start
    
    def build_dict(self, file_name):
        strategy = {}
        start_number = self.get_start_number(file_name)
        
        with open(file_name, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            
            for line in reader:
                if not file_name == "strategy/split_hand.csv":
                    strategy[start_number] = line
                    start_number += 1
                else:
                    if start_number == 5 or start_number == 10:
                        start_number += 1
                        strategy[start_number] = line
                        
                    strategy[start_number] = line
                    start_number += 1
                    
        return strategy

    def execute(self):
        if self.hard_hand:
            print("Basic strategy for hard hands")

    @property
    def surrender(self, bool):
        self._surrender = bool

    def hard(self):
        self.hard_hand = True