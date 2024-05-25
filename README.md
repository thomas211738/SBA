# Sports Betting Arbitrage 

## What is arbitrage betting?
“A way for gamblers to ensure a betting profit regardless of the outcome of a specific event”

This means if Team A wins or Team B wins a game the better will still make money. However, opportunities like this can be difficult to find.

## Implied Odds
Implied probability refers to the overall likelihood of a betting outcome according to the listed odds.

| Odds  | Prob 1 (Betting odd) | Prob 2 (Betting odd)| Implied Prob |
| ------------- | ------------- | ------------- | ------------- |
| Fair Odds (1)  | 50% (+100) | 50% (+100) | 100%  |
| In favor of Book (>1) | 52.4% (-110) | 52.4% (-110) | 104.8%  |
| In favor of Better (<1)  | 47.6% (+110)  | 47.6% (+110)  | 95.2%  |

## Finding Arbitrage Opportunities (before game)  
Used Odds-API to get sports odds from sports books

| Advantages  | Disadvantages |
| ------------- | ------------- |
| Over 15 Sports Books | Only 500 free monthly requests  |
| 70 different sports  | Didn’t Include tie Odds  |

Example: New Orleans Pelicans vs Oklahoma City Thunder

<img width="300" alt="image" src="https://github.com/thomas211738/SBA/assets/109131481/5dced3ef-f3a5-4dce-80c6-1bdf83e280f9">

The best odds here are with Unibet for odds1 and MyBookie.ag for odds2.

| Odds1 (Unibet)  | Odds2 (MyBookie.ag) |
| ------------- | ------------- |
| +163 | -179  |
|  38%  |  64.2% |

Implied odds = 38% + 64.2% = 102%. Since the Implied Odds are greater than 1, the odds are in favor of the book, and there is no arbitrage opportunity. This goes to show how difficult it is to find arbitrage opportunities. However, we wanted to see if arbitrage opportunities rose during the game. Our theory was that different sports books update their odds slightly differently after specific game events, and therefore there could be more significant differences as the game goes on within the odds.


