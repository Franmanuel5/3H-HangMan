import random as rand


class HangManFunctions:
    def find_characters(self, word, letter):
        index_list = []
        for i in range(len(word)):
            if word[i] == letter:
                index_list.append(i)
        return index_list


class HangMan:
    word_list = ["chemical","nothing","attached","suddenly","pay","horse","would","one","white","tape",
                "soldier","evidence","block","shaking","learn","kind","football","process","older","bar",
                "tomorrow","pale","mass","arm","ring","seldom","raw","voice","quick","divide",
                "silent","watch","hole","manufacturing","deal","chain","desert","sight","correct","manufacturing",
                "be","everyone","tune","layers","log","due","rain","tape","spider","tales",
                "nearer","family","floating","snake","gain","passage","television","greatly","upon","fourth",
                "elephant","missing","loud","ear","distant","difficulty","fish","biggest","adult","swimming",
                "regular","broken","story","scared","shallow","sell","contrast","soft","troops","blind",
                "officer","central","race","continued","pet","flower","golden","claws","science","composed",
                "outside","fellow","tail","immediately","clay","member","history","trunk","happened","enjoy",
                "range","degree","surrounded","cookies","former","generally","go","play","studied","officer"]
    strikes = 0
    current_word = -1
    game_status = False
    positions = []

    def start_game(self):
        if not self.game_status:
            self.current_word = self.word_list[rand.randint(0, len(self.word_list))]
            self.strikes = 0
            self.positions = ['_']*len(self.current_word)
            self.game_status = True

    def main_loop(self):
        utility = HangManFunctions()
        end_state = False

        while not end_state:
            self.start_game()
            print('\nStart Game: New Word Generated\n')
            while self.game_status:
                print(self.positions)
                letter = input('Enter Letter > ')
                if letter == 'end':
                    end_state = True
                    self.game_status = False
                elif len(letter) != 1:
                    print('Please enter a single letter.')
                elif letter.isdigit():
                    print('Please enter a character instead of number.')
                else:
                    value = utility.find_characters(self.current_word, letter)
                    for x in value:
                        self.positions[x] = self.current_word[x]
                    if len(value) == 0:
                        self.strikes += 1
                    if self.strikes == 5:
                        print("\nGAME OVER!")
                        print('The word was: ' + self.current_word)
                        self.game_status = False
                        self.strikes = 0
                    if ''.join(self.positions) == self.current_word:
                        print("\nYOU WON")
                        self.game_status = False
                        self.strikes = 0


class Main:
    game = HangMan()
    game.main_loop()










