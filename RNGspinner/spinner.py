import random 

reward_probs = { 
        'Steam Deck': 0.00001,
        'nothing': 0.5,
        'next shower is warm': 0.05, 
        '10 mins social media': 0.1, 
        'game of league': 0.05, 
        'eat takeout': 0.05, 
        '10 mins of anything': 0.05, 
        '10 mins of chess': 0.05, 
        'read an article': 0.1, 
        'two spins': 0.04999, 
}
def spin(): 
    return random.choices(list (reward_probs. keys ()), list (reward_probs. values () )) [0]
def main(): 

    spin_result = spin() 
    print('Your Random Reward is...')
    print(spin_result) 
    if (spin_result != 'nothing'): 
        with open('rewards.txt', 'a') as f: 
            f.write(spin_result +'\n') 
if __name__ == '__main__': main()


