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
    'Nothing': 50,
}


def spin():
    rewards = list(reward_probs.keys())
    probabilities = list(reward_probs.values())

    return random.choices(rewards, probabilities)[0]


def main():
    spin_result = spin()
    print('Your Random Reward is...')
    print(spin_result)

    if spin_result != 'Nothing':
        date_time = datetime.datetime.now().strftime("%H:%M, %d/%m/%Y")
        with open('rewards.txt', 'a') as f:
            f.write(spin_result + '\n' + date_time + '\n\n')


if __name__ == '__main__':
    main()
