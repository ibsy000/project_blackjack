import random
import time
import os


class Blackjack:
    

    def __init__(self):

        self.full_deck = [
        'A♣', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J♣', 'Q♣', 'K♣',
        'A♦', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J♦', 'Q♦', 'K♦',
        'A♥', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J♥', 'Q♥', 'K♥',
        'A♠', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J♠', 'Q♠', 'K♠'
        ]

        self.player_hand = []
        self.dealer_hand = []
        
        self.player_total = []
        self.dealer_total = []

        self.pocket_change = 150
        self.bet_amount = 0

    def bet(self):

        while True:

            bet = input(f"How much would you like to bet? You currently have ${self.pocket_change:.2f}. $")
            bet = int(bet)

            self.bet_amount = bet

            os.system("cls")

            if bet > self.pocket_change:
                print("I'm sorry you don't have enough money. ")

            else:
                print(f"Thank you for your bet of: ${bet}.")
                break



    def first_deal(self):

        print("Dealer is now shuffling the deck...")
        print("----------------------------------------")
        time.sleep(5)

        os.system("cls")

        self.player_hand = []
        self.dealer_hand = []
        
        self.player_total = []
        self.dealer_total = []

        while len(self.dealer_hand) < 2:

            self.dealer_hand.append(random.choice(self.full_deck))

            if len(self.dealer_hand) == 2:

                print(f"Dealer Hand: [?, {self.dealer_hand[1]}]")

                for card in self.dealer_hand:

                    if card in {'J♣', 'Q♣', 'K♣', 'J♦', 'Q♦', 'K♦', 'J♥', 'Q♥', 'K♥', 'J♠', 'Q♠', 'K♠'}:
                        card = 10
                        self.dealer_total.append(card) 

                    elif card in {'A♣', 'A♦', 'A♥', 'A♠'}:
                        card = 11
                        self.dealer_total.append(card)
                        
                    else:
                        self.dealer_total.append(card)

                print(f"Dealer has {self.dealer_total[1]} showing.")
                print("----------------------------------------")
                time.sleep(3)


        while len(self.player_hand) < 2:

                self.player_hand.append(random.choice(self.full_deck))

                if len(self.player_hand) == 2:
                    print(f"Your Hand: {self.player_hand}")

                    for card in self.player_hand:

                        if card in {'J♣', 'Q♣', 'K♣', 'J♦', 'Q♦', 'K♦', 'J♥', 'Q♥', 'K♥', 'J♠', 'Q♠', 'K♠'}:
                            
                            card = 10
                            self.player_total.append(card)

                        elif card in {'A♣', 'A♦', 'A♥', 'A♠'}:
                            
                            card = 11
                            self.player_total.append(card)

                        else:
                            
                            self.player_total.append(card)

                    print(f"You have a total of {sum(self.player_total)} showing.")
                    print("----------------------------------------")
                    time.sleep(3)



    def totals(self):

        if sum(self.dealer_total) == 21:

            print(f"Dealer Hand: {self.dealer_hand}")
            print(f"Dealer has a total of {sum(self.dealer_total)} showing.")
            print("----------------------------------------")

            print("Dealer has BLACKJACK and WINS!")
            print(f"Sorry but you lose your bet of ${self.bet_amount}!")

            self.pocket_change -= self.bet_amount

            print(f"""
    Bummer! You now have ${self.pocket_change:.2f}.
            """)
            print("----------------------------------------")


        elif sum(self.player_total) == 21:

            print("You have BLACKJACK and WIN!")

            new_amount = self.bet_amount * 1.5
            self.pocket_change += new_amount

            print(f"""
    Congrats! You win 1 1/2 times your bet amount!
    You now have ${self.pocket_change:.2f}!
    That's a lot of cheddar!
            """)
            print("----------------------------------------")



    def hit(self):

        os.system("cls")

        print(f"Dealer Hand: [?, {self.dealer_hand[1]}]")
        print(f"Dealer has {self.dealer_total[1]} showing.")
        print("----------------------------------------")
        time.sleep(2)

        self.player_hand.append(random.choice(self.full_deck))

        print(f"Your Hand: {self.player_hand}")

        new_card = self.player_hand[-1]
        
        if new_card in {'J♣', 'Q♣', 'K♣', 'J♦', 'Q♦', 'K♦', 'J♥', 'Q♥', 'K♥', 'J♠', 'Q♠', 'K♠'}:
            
            new_card = 10
            self.player_total.append(new_card)

        elif new_card in {'A♣', 'A♦', 'A♥', 'A♠'}:
            
            new_card = 11
            self.player_total.append(new_card)

        else:
            
            self.player_total.append(new_card)

        print(f"You have a total of {sum(self.player_total)} showing.")
        print("----------------------------------------")
        time.sleep(2)

        if sum(self.player_total) > 21:

            self.pocket_change -= self.bet_amount

            print(f"""
    Oh no! You BUSTED!
    Sorry but you lose your bet of ${self.bet_amount}!
    You now have ${self.pocket_change:.2f}
            """)



    def stay(self):

        os.system("cls")

        print(f"Your Hand: {self.player_hand}")
        print(f"You have a total of {sum(self.player_total)} showing.")
        print("----------------------------------------")
        time.sleep(2)

        print("Now it's the Dealer's turn...")
        print("----------------------------------------")
        time.sleep(3)

        while sum(self.dealer_total) < 17:

            self.dealer_hand.append(random.choice(self.full_deck))

            print(f"Dealer Hand: [?, {self.dealer_hand[1:]}]")

            new_card = self.dealer_hand[-1]
            
            if new_card in {'J♣', 'Q♣', 'K♣', 'J♦', 'Q♦', 'K♦', 'J♥', 'Q♥', 'K♥', 'J♠', 'Q♠', 'K♠'}:
                
                new_card = 10
                self.dealer_total.append(new_card)

            elif new_card in {'A♣', 'A♦', 'A♥', 'A♠'}:
                
                new_card = 11
                self.dealer_total.append(new_card)

            else:
                
                self.dealer_total.append(new_card)


            print(f"Dealer has {sum(self.dealer_total[1:])} showing.")
            print("----------------------------------------")
            time.sleep(3)
            

        if sum(self.dealer_total) > 21 or sum(self.dealer_total[1:]) > 21:

            print("Dealer will now reveal it's hand...")
            print("----------------------------------------")
            time.sleep(3)

            print(f"Dealer Hand: {self.dealer_hand}")
            print(f"Dealer has a total of {sum(self.dealer_total)} showing.")

            new_amount = self.bet_amount * 2
            self.pocket_change += new_amount

            print(f"""
    Woah! Dealer BUSTED!
    Congrats! You win double your bet amount of: ${self.bet_amount}!
    You now have ${self.pocket_change:.2f}
            """)

        else:
            print("Dealer will now reveal it's hand...")
            print("----------------------------------------")
            time.sleep(3)

            print(f"Dealer Hand: {self.dealer_hand}")
            print(f"Dealer has a total of {sum(self.dealer_total)} showing.")
            print("----------------------------------------")


        if sum(self.player_total) == sum(self.dealer_total):

            self.pocket_change -= self.bet_amount

            print(f"""
    Looks like you tied with the dealer!
    Unfortunately, tie goes to Dealer!
    You lose your ${self.bet_amount}...
    You now have ${self.pocket_change:.2f}.
            """)


        elif sum(self.player_total) > sum(self.dealer_total):

            new_amount = self.bet_amount * 2
            self.pocket_change += new_amount

            print(f"""
    Woah! You beat the Dealer!
    Congrats! You win double your bet amount of: ${self.bet_amount}!
    You now have ${self.pocket_change:.2f}
            """)
            
        elif sum(self.player_total) < sum(self.dealer_total) and sum(self.dealer_total) < 21:

            self.pocket_change -= self.bet_amount

            print(f"""
    Dealer beat you!
    Bummer! You now have ${self.pocket_change:.2f}.
            """)
            
        

def play():

    os.system("cls")

    print("""
    Hello and Welcome to Online Blackjack Casino!
    The only game we have here is Blackjack!
    I hope you're ready!

    -------------------------------------
    *Tip: In this game Aces are worth 11*
    -------------------------------------
    """)

    my_hand = Blackjack()

    # there is probably a better way to do this..
    # but this is what worked for me as of right now
    while True:
        
        my_hand.bet()
        my_hand.first_deal()
        my_hand.totals()

        while True:

            # I really didn't want it to keep asking this question after a game
            # is over but it works for now, I will continue to workshop it
            hit_or_stay = input("Would you like to hit, stay, quit, or start over? ")
            hit_or_stay = hit_or_stay.strip().lower()

            if hit_or_stay == 'hit':
                my_hand.hit()
            

            elif hit_or_stay == 'stay':
                my_hand.stay()


            elif hit_or_stay == 'start over':

                os.system("cls")
                my_hand.bet()
                my_hand.first_deal()
                my_hand.totals()


            elif hit_or_stay == 'quit':

                os.system("cls")

                print("""
    ---------------------------------------------------------
    Thank you for playing at ♥♦♣♠Online Blackjack Casino!♠♣♦♥
    I hope you had fun!
    Come back and spend your money again!
    ---------------------------------------------------------
                """)
                break


            else:
                print("That is not a valid response.")

        break
        
play()