def add_binary(bin_num1: str, bin_num2: str) -> str:
  carry = 0
  result = ''
  max_len = max(len(bin_num1), len(bin_num2))
  bin_num1 = bin_num1.rjust(max_len, '0')[::-1]
  bin_num2 = bin_num2.rjust(max_len, '0')[::-1]
  for val_1, val_2 in zip(bin_num1, bin_num2):
    add_result = carry + int(val_1) + int(val_2)
    carry = 1 if add_result > 1 else 0
    result = f"{add_result%2}{result}"
  return f"{1 if carry else ''}{result}"


def can_construct(word: str, letters: str) -> bool:
  for letter in word:
    if letter not in letters:
      return False
    letters = letters.replace(letter, '', 1)
  return True


class Complex:
  def __init__(self, a: float, b: float):
    self.a = a
    self.b = b

  def __add__(self, other: 'Complex') -> 'Complex':
    return Complex(self.a + other.a, self.b + other.b)
  
  def __sub__(self, other: 'Complex') -> 'Complex':
    return Complex(self.a - other.a, self.b - other.b)

  def __mul__(self, other: 'Complex') -> 'Complex':
    return Complex(self.a * other.a - self.b * other.b,
        self.a * other.b + self.b * other.a)

  def __repr__(self) -> str:
    return f"{self.a} {'-' if self.b < 0 else '+'} {abs(self.b)}i"


import random

def create_permutation(n: int) -> list:
  unscrambled = [i for i in range(n)]
  result = []
  while unscrambled:
    result.append(unscrambled.pop(random.randint(0, len(unscrambled) - 1)))
  return result


def scramble_word(word: str) -> str:
  return ''.join(word[i] for i in create_permutation(len(word)))


def guessing_game(word: str) -> None:
  print(f"Unscramble the word: {' '.join(scramble_word(word))}")
  guess = input("Try #1: ")
  try_num = 2
  while(guess != word):
    print("Wrong!")
    guess = input(f"Try #{try_num}: ")
    try_num = try_num + 1
  print("Yay, you got it!")
