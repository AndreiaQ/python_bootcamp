from art import logo , vs
from list import data
import random


def get_comparison(index):
    selected_item = data[index]
    return (f"Compare A: {selected_item['name']}, "
            f"a {selected_item['description']}, "
            f"from {selected_item['country']}.")

def get_followers(index):
    selected_item = data[index]
    return selected_item['follower_count']

def check_answer(user_answer , a_followers, b_followers):
    if a_followers > b_followers:
        return user_answer == 'a'
    elif a_followers < b_followers:
        return user_answer == 'b'

game_should_continue = True
score = 0


first_random_index = random.randint(0, 49)

comparison_b = get_comparison(first_random_index)

print(logo)

while game_should_continue:

    second_random_index = random.randint(0, 49)

    comparison_a = comparison_b
    comparison_b = get_comparison(second_random_index)

    # Print the comparisons
    print(comparison_a)
    print(vs)
    print(comparison_b)

    guess = input("Who has more followers ? Type A or B:").lower()


    print("\n" * 20)
    print(logo)

    followers_a = get_followers(first_random_index)
    followers_b = get_followers(second_random_index)

    is_correct = check_answer(guess, followers_a, followers_b)

    if is_correct:
        score += 1
        print(f"You're right! Current score:{score}")

    else:
        print(f"Sorry, you're wrong! Final score: {score}")
        game_should_continue = False









