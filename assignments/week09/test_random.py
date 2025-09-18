import random


test_random = random.randint(1, 10)

print("-- เกมทายตัวเลข")

guess_number = int(input("What is your guess number (0-9)? : "))

if test_random == guess_number:
    print("ยูเก่งมาก มั่วถูกตั้งแต่แรกเลย เก่งมากๆ")

if guess_number < test_random:
    print("ผิดจ้า น้อยไปเนอะ")

if guess_number > test_random:
    print("ผิดจ้า เยอะไปเนอะ")
    
