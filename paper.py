import random
def play_game():
    your_score = 0
    computer_score = 0
    
    while True:
        print("Choose: rock, paper, or scissors")
        player = input("Your choice: ").lower()
        
        if player == "quit":
            print(f"Final Score - You: {your_score}, Computer: {computer_score}")
            break
        
        if player not in ['rock', 'paper', 'scissors']:
            print("Invalid input plz try again.")
            continue

        computer = random.choice(['rock', 'paper', 'scissors'])
        print(f"Computer chose: {computer}")
        
        if player == computer:
            print("It's a tie!")
        elif (player == 'rock' and computer == 'scissors') or \
             (player == 'scissors' and computer == 'paper') or \
             (player == 'paper' and computer == 'rock'):
            print("You win!")
            your_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
        
        print(f"Score - You: {your_score}, Computer: {computer_score}")
        
        again = input("Play again? (yes/no): ").lower()
        if again != 'yes':
            print(f"Final Score - You: {your_score}, Computer: {computer_score}")
            break

play_game()
