# This challenge's lesson was to write out my thoughts.
# It was better to find out what I do and don't know before trying to put things together
# Especially considering that once I knew what I was doing,
# THe problem was much simpler, AND there was no spaghetti code.

    # My spaghetti code version

k, K = int(input()), list(map(int, input().split()))
print((sum(set(K))*k-sum(K))//(k-1))

################################################################################

    # My refined version

k, K = int(input()), list(map(int, input().split()))
print((sum(set(K))*k-sum(K))//(k-1))

################################################################################

    # Hackerrank's approach

K = int(raw_input())

#Step 1. Store List: Store the list in a variable. Let roomList be the variable storing the list of room numbers.
roomList = map(int,raw_input().split())

#Step 2. Room Set: In the variable roomSet, store the set of roomList.
roomSet = set(roomList) 

#Step 3. Sum Room Set and List: In the variable sumRoomSet and sumRoomList, store the summations of roomSet and roomList, respectively. 
sumRoomSet = sum(roomSet) 
sumRoomList = sum(roomList) 

# Step 4. Multiply K and Subtract: Now, we multiply  with sumRoomSet, subtract the sumRoomList from it and then store the result in the variable temp. Therefore, temp = the Captain's room number   .
temp = sumRoomSet * K - sumRoomList 

# Step 5. Divide by K-1: Divide temp by  and store the result in the variable answer.
answer = temp / (K - 1) 

# Step 6. Output: Print answer.
print answer
K = int(input())
set_S = set()
sumlist_S = 0
for i in input().split():
    I = int(i)
    set_S.add(I)
    sumlist_S += I

print((sum(set_S)*K - sumlist_S)//(K-1))   
