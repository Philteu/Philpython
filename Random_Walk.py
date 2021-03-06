# A game 
#Throw a die 100 times
#if it is 1 or 2, you will go 1 step down.
#if it is 3, 4 or 5, you will go 1 step up. 
#if it is 6, you will throw the die again and will wall up the resulting number of steps

#rule:
#Can't go below step 0
#0.1% chance of falling down the stairs(0.1% to start again from zero. 
#Bet: you'll reach step 60.


#Python fucntion used:
# range(x) - limit the value in the bracket, start from 0 until x.
#append(x) - add a single item x  into list
#randint(x,y)- return a specific number within x and y-1


# Initialize random_walk, # start from 0
random_walk =[0]

#Throw a die 100 times
for x in range(100) :
    # Set step: last element in random_walk, new item will be added into last element
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step= max(0,x-1) #avoid go below step 0 
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk, append() adds a single item in to list
    random_walk.append(step)

# Print random_walk
print(random_walk)

#visualize the walk 
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()
