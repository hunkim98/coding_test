ByteDance has launched a new feature on TikTok called "TikTok Collectibles," where users can collect and trade digital cards featuring popular TikTok creators. Each creator has different categories of cards, such as rare cards for the most followed creators, special edition cards with unique designs, and interactive cards that come with exclusive video content.

ByteDance wants to create a number of collectible packs, each containing equal numbers of each type of card. To achieve this, they need to add more cards to ensure each type can be evenly distributed across the packs.
Given the current inventory of each category of cards as an integer array cardTypes of size n, determine the minimum number of additional cards needed so that they can create more than one pack with an equal type distribution.

Example
n = 5
cardTypes = [4, 7, 5, 11, 15]
In order to make 2 matching packets, the following numbers of additional cards of each type must be added: [0, 1, 1, 1, 1]. This sums to 4 additional cards. The numbers of cards are [4, 8, 6, 12, 16] and they can be divided evenly among 2 packets.
If 3 packets are created, an additional [2, 2, 1, 1, 0] cards are needed, sum = 6 items. This yields quantities [6, 9, 6, 12, 15]. Any number of packets ≥ 2 can be created, but creating 2 packets requires the minimum number of additional cards.