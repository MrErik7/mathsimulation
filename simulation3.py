import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# Variable definitions
item_value = 50
people_count = 480
max_days = 10000

# Initialize people's money
people = [item_value for _ in range(people_count)]

# Initialize animation
fig, ax = plt.subplots()
plt.xlabel('Personer')
plt.ylabel('Kronor')
plt.title('Slumpmässig ojämlikhet')

# Initialize plot data
people_number = list(range(1, people_count + 1))
bar_data = ax.bar(people_number, people)

# Text object for displaying variance and std. dev.
variance_text = ax.text(0.2, 0.4, '', ha='left')

# Function to update plot data and visualization
def update_plot(frame, people, bar_data):
    if frame >= max_days:
        ani.event_source.stop()  # Stop animation if max_days is reached

    # Set dynamic y-axis limits
    max_money = np.max(people)
    y_lim_buffer = 5  # Add a buffer for better visualization
    ax.set_ylim(0, max_money + y_lim_buffer)

    # Simulate one day
    for _ in range(1):
        for index in range(len(people)):
            # Skip if person has no money
            if people[index] == 0:
                continue

            # Person loses one money
            people[index] -= 1

            # Find a random person other than the giver (ensure not self)
            while True:
                recipient = random.randrange(len(people))
                if recipient != index:
                    break  # Found a valid recipient

            # Random person gains one money
            people[recipient] += 1


    # Sort people array
   # people.sort()

    # Update bar data
    for i in range(len(people)):
        bar_data[i].set_height(people[i])

    # Set title with current day
    ax.set_title(f'Slumpmässig ojämlikhet - Dag {frame + 1}')

    # Calculate and update variance and std. dev.
    variance = np.var(people)
    std_deviation = np.std(people)
    range_difference = np.ptp(people)  # Calculate the difference between max and min
    mean_value = np.mean(people)  # Calculate the mean

    # Count number of people above and below the starting value
    above_starting_value = sum(1 for p in people if p > item_value)
    below_starting_value = sum(1 for p in people if p < item_value)

    variance_text.set_text(f'Varians: {variance:.2f}\nStandardavvikelse: {std_deviation:.2f}\nHögsta-lägsta: {range_difference:.2f}\nMedelvärde: {mean_value:.2f}\n'
                       f'Antal personer över startvärde: {above_starting_value}\nAntal personer under startvärde: {below_starting_value}')

    return bar_data

# Create animation
ani = animation.FuncAnimation(fig, update_plot, fargs=(people, bar_data))

plt.show()
