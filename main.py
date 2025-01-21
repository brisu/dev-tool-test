import random

def random_action(user_input):
    actions = [
        lambda x: x.upper(),  # Convert to uppercase
        lambda x: x.lower(),  # Convert to lowercase
        lambda x: ''.join(reversed(x)),  # Reverse the input
        lambda x: f"{x}!!!",  # Add exclamation marks
        lambda x: ''.join(random.sample(x, len(x))) if len(x) > 1 else x,  # Shuffle the input
    ]
    chosen_action = random.choice(actions)
    return chosen_action(user_input)

def main():
    print("Welcome! Enter a word or sentence, and I'll do something random with it.")
    user_input = input("Enter your input: ")
    result = random_action(user_input)
    print(f"Here are the results of the random action: {result}")

if __name__ == "__main__":
    main()
