import random

class generatePassword:

    def generate_Password(self):
        word_list_1 = ['charismatic', 'chance', 'mirror', 'demonstrate', 'circumstance']
        word_list_2 = ['gift', 'date', 'cupboard', 'apathy', 'venture']

        first_word = random.choice(word_list_1)
        second_word = random.choice(word_list_2)

        num = random.randint(0, 10)

        return ''.join(first_word+'_'+second_word + str(num))

