import random

class Carte:
    def __init__(self):
        self.valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.couleurs = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.carte_valeurs = {"Ace": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10}
        self.deck = []


        def get_deck(self):
            return self.deck

        for couleur in self.couleurs:
            for valeur in self.valeurs:
                carte_valeur = self.carte_valeurs[valeur] 
                self.deck.append(f'{valeur} of {couleur}')

        random.shuffle(self.deck)


class Jeu(Carte):
    def __init__(self):
        Carte.__init__(self)
        self.deck = self.deck

    def melanger_paquet(self):
        random.shuffle(self.deck)
    
    def deal_cards(self, hand):
        for i in range(2): 
            card = self.deck.pop() 
            hand.append(card)

    def hit(self, hand):
        card = self.deck.pop()
        hand.append(card)

    def calculate_hand_value(self,hand):
        value = 0
        has_ace = False

        for card in hand:
            self.couleurs = card.split()[0]

            if self.couleurs.isdigit():
                value += int(self.couleurs)
            elif self.couleurs in ['Jack', 'Queen', 'King']:
                value += 10
            elif self.couleurs == 'Ace':
                has_ace = True
                value += 11

        if has_ace and value > 21:
            value -= 10
        return value
    
    def compare(self, player_hand, dealer_hand):
        player_score = self.calculate_hand_value(player_hand)
        dealer_score = self.calculate_hand_value(dealer_hand)

        if player_score > dealer_score and player_score <= 21:
            print("You win!")
        elif player_score == dealer_score and player_score <= 21:
            print("It's a tie!")
        elif player_score < dealer_score and dealer_score <= 21:
            print("You lose!")
        elif player_score > 21:
            print("You lose!")
        elif dealer_score > 21:
            print("You win!")



def BlackJack():
    run = True
    player_hand = []
    dealer_hand = []
    player_score = 0
    dealer_score = 0   

    while len(player_hand) < 2:
        jeu.deal_cards(player_hand)

        player_score += jeu.calculate_hand_value(player_hand)

        # check if the first two cards are aces and if so, subtract 10 from the player_score
        # if len(player_hand) == 2:
        #     if player_hand[0].cards_values == 'Ace' and player_hand[1].cards_values == 'Ace':
        #         player_score -= 10
        print(f"Player card is {player_hand} with {player_score} points")

        jeu.deal_cards(dealer_hand)
        dealer_score += jeu.calculate_hand_value(dealer_hand)

        # if len(dealer_hand) == 2:
        #     if dealer_hand[0].cards_values == 'Ace' and dealer_hand[1].cards_values == 'Ace':
        #         dealer_score -= 10

        print(f"Dealer card is {dealer_hand} with {dealer_score} points")

    while player_score < 21 :

        choice = input('Do you want to hit (h) or stand (s)? ')

        if choice == 'h':
            jeu.hit(player_hand)
            player_score += jeu.calculate_hand_value(player_hand)
            print(f"Player card is {player_hand} with {player_score} points")
        elif choice == 's':
            break

            
    while dealer_score < 21:
        if dealer_score < 17:
            jeu.hit(dealer_hand)
            dealer_score += jeu.calculate_hand_value(dealer_hand)
            print(f"Dealer card is {dealer_hand} with {dealer_score} points")
        else:
            break
        
    jeu.compare(player_hand, dealer_hand)



carte_deck = Carte()
# print(carte_deck.deck)
jeu = Jeu()
# print(jeu.deck)
# jeu.melanger_paquet()



# jeu.deal_cards(player_hand)
# jeu.deal_cards(dealer_hand)

# print(player_hand)
# print(dealer_hand)
# print(jeu.calculate_hand_value(player_hand))

BlackJack()


