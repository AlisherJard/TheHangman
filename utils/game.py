import random

class hangman:
    """
    A class hangman represents a guessing game.

    Attributes
    ----------
    word : list
    The attribute that contains a list of words. Out of these words, one will be selected as the word to find.

    life : int
    The attribute that contains the number of lives that the player still has left. It should start at 5.

    turn_count : int
    The attribute that contain the number of turns played by the player. This will be represented as an int.

    error_count: int
    The attribute that contain the number of errors occurred during the game.

    correctly_guessed_letters: list[str]
    The attribute that contains a list of strings where each element will be a letter guessed by the user.

    wrongly_guessed_letters: list[str]
    The attribute that contains a list of strings where each element will be a letter guessed by the user that is not in word_to_find.

    word_to_find: list[str]
    The attribute that contains a list of strings. Each element will be a letter of the word.

    """

    def __init__(self, life=5):

        self.word = random.choice(['becode', 'learning', 'mathematics', 'sessions'])
        self.life = life
        self.turn_count = 0
        self.error_count = 0
        self.correctly_guessed_letters = []
        self.wrongly_guessed_letters = []
        self.word_to_find = []

        for x in self.word:
            self.word_to_find.append(x)


    def play(self,x:str)-> str:
        '''
        play() -> str:
        A play() method that asks the player to enter a letter. If the player guessed a letter well, adds it to the
        correctly_guessed_letters list. If not, adds it to the wrongly_guessed_letters list and adds 1 to error_count.
            :param x: The player shouldn't be allowed to type
        something else than a letter and not more than a letter.
        '''

        a = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
        assert x in a, 'Please,enter a letter. Restart the game.'
        if x in self.word:
            self.correctly_guessed_letters.append(x)
        elif x not in self.word:
            self.wrongly_guessed_letters.append(x)
            self.error_count += 1
        return x

    def start_game(self)-> str:
        '''
        start_game() -> str:
        will call play() until the game is over (because the use guessed the word or because of a game over).
        will call game_over() if lives is equal to 0.
        will call well_played() if all the letter are guessed.
        will print correctly_guessed_letters, bad_guessed_letters, life, error_count and turn_count at the end of each turn.
        '''
        while self.life > 0:
            print(self.word_to_find)
            letter = input("Enter a letter to guess:").lower()
            print(f'You have {self.life} lives left!')
            for x in self.play(letter):
                if x in self.word:
                    self.turn_count +=1

                    correctly_guessed_letters_2 = '_'.split() * len(self.word_to_find)
                    for index, x in enumerate(self.word_to_find):
                        if x in self.correctly_guessed_letters:
                            correctly_guessed_letters_2[index] = x
                    print(f'Correctly guessed letters:{correctly_guessed_letters_2} Wrongly guessed letter: {self.wrongly_guessed_letters}, Error count: {self.error_count}.')

                    if set(self.correctly_guessed_letters) == set(self.word_to_find):
                        return self.well_played()

                elif x not in self.word:
                    self.turn_count += 1
                    self.life -= 1

                    correctly_guessed_letters_2 = '_'.split() * len(self.word_to_find)
                    for index, x in enumerate(self.word_to_find):
                        if x in self.correctly_guessed_letters:
                            correctly_guessed_letters_2[index] = x
                    print(f'Correctly guessed letters:{correctly_guessed_letters_2} Wrongly guessed letter: {self.wrongly_guessed_letters}, Error count: {self.error_count}.')

                if self.life == 0:
                    return self.game_over()
                    break

    def game_over(self)-> str:
        '''
        game_over() -> str:
        A game_over() method that will stop the game and print game over...
        '''
        return "Game over!"

    def well_played(self)-> str:
        '''
        well played() -> str:
        A well played() method that will print You found the word: {word_to_find_here} in {turn_count_here} turns
        with {error_count_here} errors!
        '''
        return f"You found the word: '{self.word}' in {self.turn_count} turns with {self.error_count} errors!"



