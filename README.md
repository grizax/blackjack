### Blackjack

# General Rules

- Player starts with 100 chips
- Allowable bets are increments of 10 up to the total amount the player has
- Allowable actions for the player:
- (H)it
  - player is dealt one additional card
- (S)tand
  - player is dealt no additional cards
- (D)ouble
  - player doubles bet
  - player is dealt one additional card

- Dealer will hit until their hand totals at least 17, then stops

- Game Outcomes:
- Push: the player and dealer tie - the bet is returned to the player
- Dealer Wins: dealer has more than player and less than 21 - bet is forfeited by the player
- Player Wins: player has more than dealer and less than 21 - player is paid their bet
- Dealer Bust: dealer has more than 21 - player wins and is paid their bet
- Player Bust: player has more than 21 - bet is foreited by the player
- Player Blackjack: player is dealt 21 (first two cards) - player is paid 1.5 times their bet
- Dealer Blackjack: dealer is dealt 21 (first two cards) - bet is forfeited by player

## Classes

# Card

Creates a card with a given suit and value. Prints with prettyPrint

# Deck

Generates full deck, shuffles, and notes decksize after deal. Prints cards using prettyPrint.

# Dealer

Class that runs general gameplay

Collaborators:

* Holds a deck instance
* Holds an array of player's cards
* Holds an array of dealer's cards


Responsibilities:

* Initializes game deck
* Starts new game and shuffles deck
* Deals 2 cards to each player one by one
* Deals card to player
* Deals card to dealer
* Prints hands
* Confirms if player busted if hand is over 21
* Confirms if dealer busted if hand is over 21
* Confirms if dealer stops if hand is over 16
* Confirms if player blackjacks if first two cards are 21
* Confirms if dealer blackjacks if first two cards are 21
* Evaluates hands and prints returns


# Main

Handles input / output for general gameplay.  Manages general gameplay and player bank using an instance of `Blackjack`.
