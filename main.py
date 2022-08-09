import time
import random

name = input("Hello, what is your name? ")

time.sleep(2)
print("My name is Hello" + name)

feeling = input("How are you today? ")

time.sleep(2)
if "good" in feeling:
    print("I'm feeling good too!")
else:
    print("I'm sorry to hear that!")

time.sleep(2)
favcolour = input("What is your favourite colour? ")

colours = ["Red","Green","Blue"]

time.sleep(2)
print("My favourite colour is " + random.choice(colours))

time.sleep(2)
print("wow")