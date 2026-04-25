# Given N cards arranged in a row, each card has an associated score denoted by the cardScore array.
# Choose exactly k cards. In each step, a card can be chosen either from the beginning or the end of the row. The score is the sum of the scores of the chosen cards.
# Return the maximum score that can be obtained.
# Examples:
# Input: cardScore = [1, 2, 3, 4, 5, 6], k = 3
# Output: 15
# Explanation: Choosing the rightmost cards will maximize your total score. So optimal cards chosen are the rightmost three cards 4,5,6.
# Th score is 4 + 5 + 6 =>15
# Input: cardScore = [5, 4, 1, 8, 7, 1, 3], k = 3
# Output: 12


arr = [5, 4, 1, 8, 7, 1, 3]
max_score=0
k=3
for i in range(k+1):
    cur = sum(arr[0:i]) + sum(arr[len(arr)-k+i: len(arr)])
    if cur>max_score:
        max_score = cur

print(max_score)

