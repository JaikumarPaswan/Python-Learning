# Question
# You are given N bank transactions.
# Each transaction has:
# Sender Receiver Amount Timestamp
# A transaction is considered fraud if:
#   Sender, Receiver, Amountand Timestamp are same
#   Timestamp between for same Sender, Receiver, Amount has difference ≤ 60 seconds
# Find and print all such fraud transactions.



n = int(input("Enter num of Transactions: "))

seen = {}

for i in range(n):
    s, r, a, t = input().split() 
    t = int(t)

    if (s, r, a) in seen:
        if abs(seen[(s, r, a)] - t)<60:
            print("Fraud Detected: " + s +" "+ r +" "+ a +" "+str(t))
            break
    else:
        seen[(s, r, a)] = t
else:
    print("No Fraud")


    



