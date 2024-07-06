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

Implied odds = 38% + 64.2% = 102%. Since the Implied Odds are greater than 1, the odds are in favor of the book, and there is no arbitrage opportunity. This goes to show how difficult it is to find arbitrage opportunities. However, we wanted to see if arbitrage opportunities rose during the game. 

## Finding Arbitrage Opportunities (during game)

Our theory was that different sports books update their odds slightly differently after specific game events, and therefore there could be more significant differences in odds as the game goes on. 

Here is an example we did with the Mavericks vs Clippers:

<img width="930" alt="image" src="https://github.com/thomas211738/SBA/assets/109131481/304868f4-acb2-4bb5-b5bd-8737bbc13650">

Our program collected odds every 5 minutes and had 38 odds for each book. You can also note that some values are NaN. This is because some books decide to close betting and so no odds are available. 

These are our findings for in-game arbitrating:

<img width="413" alt="image" src="https://github.com/thomas211738/SBA/assets/109131481/25c970eb-89f5-4de6-ac72-869d24f52851">
<img width="412" alt="image" src="https://github.com/thomas211738/SBA/assets/109131481/d11d4940-31e0-4250-bfab-313a4f6312c8">

In the first graph, we can see that all sportsbook odds are relatively similar at the beginning of the game. However, sportsbook odds varied a lot as the game went on, especially in the 70th minute. The second graph shows the best book odds for each team. 

<img width="406" alt="image" src="https://github.com/thomas211738/SBA/assets/109131481/85564e19-aff1-4ecb-881c-cc268c12dad3">

Now, when we look at the implied odds graph, we can see that the implied Odds are less than 1, so the odds favor the gambler. More interestingly, the game was arbitrable for almost all of it. This was because one book deviated a lot from the others, allowing for this opportunity to occur throughout the whole game. This gave us proof that arbitrage opportunities were still possible throughout the games. 

## Possible errors and Future Considerations

In the example we looked at, one thing we didn't consider was that the underdog team won. This could have been the reason that the book odds varied and not because of our hypothesized inconsistencies between the books. To address this in the future, we can look at a game where the favored team wins, and compare the variances of the sportsbook odds. Another improvement we can consider for the future is subscribing to the Odds-API paid version to get more odds data per game, or use web scraping. This can help us get more accurate and up-to-date odds. Sportsbooks update their books very quickly so getting data more frequently would help us keep up with them. 












