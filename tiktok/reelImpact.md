6. TikTok Reel Impact
In the dynamic landscape of TikTok, creators are in a constant race to boost their videos' engagement by leveraging new features that enhance their content.

Each creator starts with a set of m videos, represented by initialReelImpacts, which indicates the baseline popularity of each reel. For the next n days, TikTok releases new trending features, represented by newReelImpacts, with each feature offering an additional boost to the creator's existing reels.

Process for Each Day:
The creator appends the new feature from newReelImpacts[i] (where 0 ≤ i < n) to their current reels.
The updated lineup of reels is reviewed, and the k-th most impactful reel is selected based on its popularity.
The impact value of this reel is added to the total impact score.
Note:
The initial impact score of the creator is the k-th highest impact value from the initial set of initialReelImpacts.
Example
Input:
m = 2  
initialReelImpacts = [2, 3]  
n = 3  
newReelImpacts = [4, 5, 1]  
k = 2  
Explanation:
The initial impact score is the 2nd highest value in initialReelImpacts = [2, 3].
Impact score = 2
Over the next n days:
Day 1: Append 4. Current reels: [2, 3, 4]. The 2nd highest impact is 3.
Impact score = 2 + 3 = 5
Day 2: Append 5. Current reels: [2, 3, 4, 5]. The 2nd highest impact is 4.
Impact score = 5 + 4 = 9
Day 3: Append 1. Current reels: [1, 2, 3, 4, 5]. The 2nd highest impact is 4.
Impact score = 9 + 4 = 13
Output:
Total Impact Score = 13
