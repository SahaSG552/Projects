import random
import string


num = int(input())


def generate_string(num):
    return ("").join(random.choice(string.ascii_letters) for _ in range(num))


random_string = generate_string(num)


def output_vowel_freq(random_string):
    vowel_count = sum(letter.lower() in {"a", "e", "i", "o", "u"}
                      for letter in random_string)
    return vowel_count / len(random_string)


proportion_of_vowels = output_vowel_freq(random_string)

print(random_string)
print(proportion_of_vowels)
