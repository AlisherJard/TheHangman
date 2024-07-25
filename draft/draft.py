answer = 'hangman'


class hangman:
    def __init__(self, word='', life=0):
        self.word = word
        self.life = life

    def get_word(self, word_2):
        self.word = input("Enter a word to guess: ")
        return self.word

    def get_lives(self, life_2):
        self.life = input("Choose the number of lives: ")
        return self.life


    def get_guess(self, guess):
        g = []
        if guess in answer:
            g.append(guess)

    def asses_guess(self, answer, g, life):
        if g in answer:
            return 'Correct'
        else:
            return 'Wrong'

    def display_word(self, answer, guess):
        return answer, answer == guess


a = hangman()
print(a.get_word('fd'))