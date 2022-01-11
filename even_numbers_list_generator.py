#Even Numbers List Generator
import math
import os

def generate_even_numbers(generate:int=math.inf , generate_until_in_list:int=None, generator_power:int=1):
    numbers_list = [0]
    number = 0
    while (len(numbers_list) <= generate) or (generate_until_in_list not in numbers_list):
        if os.name == "nt": os.system("cls")
        else: os.system("clear") 

        print(number)
        for _ in range(generator_power):
            number += 2
            numbers_list.append(number)

        if (len(numbers_list) >= generate) or (generate_until_in_list in numbers_list):
            break
        

#Warning: if you set the generator power with a very high number it may or will frezee/crash your pc