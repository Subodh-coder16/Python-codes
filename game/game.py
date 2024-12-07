import random

n = int(input("Enter the number of players:\n"))
name = [input(f"Enter the name of player{i+1}:") for i in range(n)]

arr = [
    "Who do you think is the most annoying person?",
    "Who is the ugliest?",
    "Who is the smartest?",
    "Who is the most beautiful?",
    "Who is your crush?",
    "What's your biggest lie?",
    "What do you regret the most?",
    "What do you think is your greatest achievement?"
]

randomindex1 = random.randint(0, len(arr) - 1)
randomindex2 = random.randint(0, n - 1)

print(f"The person who should answer a question is {name[randomindex2]}")
print(f"And the question is {arr[randomindex1]}")

