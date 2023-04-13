import random
import datetime

reward_probs = {
    'Steam Deck': 0.005,
    'Two spins': 4.995,
    'Next shower is warm': 5,
    'Game of https://chess.com': 5,
    'Eat fancy tonight': 5,
    'Anything for 15 minutes': 5,
    'Read a book for 15 minutes': 5,
    'Browse Reddit for 15 minutes': 5,
    'Read an article from https://thehackernews.com/': 5,
    'Read an article from https://medium.com/': 5,
    'Read an article from https://www.sciencealert.com/': 5,
    'Drink water': 50,
}


def spin():
    rewards = list(reward_probs.keys())
    probabilities = list(reward_probs.values())

    return random.choices(rewards, probabilities)[0]


def main():
    reason = input('Provide a worthy reason to spin the Wheel: ')
    spin_result = spin()

    if reason.replace(" ", "") == "":
        reason = "Void"

    print('Your Random Reward is...')
    print(spin_result)

    if spin_result != 'Drink water':
        date_time = datetime.datetime.now().strftime("%H:%M, %d/%m/%Y")
        with open('rewards.MD', 'a') as f:
            f.write('Motive: ' + reason.capitalize() + '\nPrize: ' + spin_result + '\n' + date_time + '\n\n')


if __name__ == '__main__':
    main()
