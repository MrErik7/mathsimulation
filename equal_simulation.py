import random
import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib import animation

# Variable definitions
item_value = 50
people_count = 480
max_days = 100

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

def take_integer_percentage(wealth, percentage):
  """
  This function takes a wealth value and a percentage (as an integer) and returns the integer amount representing that percentage of the wealth.
  """
  return wealth * percentage // 100  # Integer division for percentage calculation


# Function to update plot data and visualization for sorted data
def update_plot(frame, people, bar_data):
    if frame >= max_days:
        ani.event_source.stop()  # Stop animation if max_days is reached

    max_money = np.max(people)
    y_lim_buffer = 5
    ax.set_ylim(0, max_money + y_lim_buffer)

    # Calculate mean value
    mean_value = np.mean(people)


    for _ in range(1):
        for index in range(len(people)):
     

            if people[index] == 0:
                continue

            while True:
                recipient = random.randrange(len(people))
                if recipient != index:
                    break

            people[index] -= 1
            people[recipient] += 1

    # Implement proportional tax system
    total_tax_amount = 0
    for index in range(len(people)):
        if people[index] > mean_value:
            # Calculate tax proportional to exceeding mean (adjustable coefficient)
            tax_rate = (people[index] - mean_value) / people[index] * 0.2
            tax_amount = people[index] * tax_rate
            people[index] -= tax_amount
            total_tax_amount += tax_amount

    # Sort people by wealth (ascending order)
    people.sort()

    # Distribute proportionally to the first 10 poorest people
    num_poorest_recipients = min(10, len(people))  # Ensure there are enough people
    total_wealth_poorest = sum(people[:num_poorest_recipients])
    for recipient_index in range(num_poorest_recipients):
        # Distribute proportionally based on recipient's current wealth
        share = people[recipient_index] / total_wealth_poorest
        people[recipient_index] += total_tax_amount * share


    people.sort()

    for i in range(len(people)):
        bar_data[i].set_height(people[i])

    ax.set_title(f'Slumpmässig ojämlikhet - Sorterad - Dag {frame + 1}')

    variance = np.var(people)
    std_deviation = np.std(people)
    range_difference = np.ptp(people)

    above_starting_value = sum(1 for p in people if p > item_value)
    below_starting_value = sum(1 for p in people if p < item_value)
    at_starting_value = sum(1 for p in people if p == item_value)

    variance_text .set_text(f'Varians: {variance:.2f}\nStandardavvikelse: {std_deviation:.2f}\nHögsta-lägsta: {range_difference:.2f}\nMedelvärde: {mean_value:.2f}\n'
                            f'Antal personer över startvärde: {above_starting_value}\nAntal personer under startvärde: {below_starting_value}\nAntal personer på startvärde: {below_starting_value}')

    return bar_data
# Create animation
ani = animation.FuncAnimation(fig, update_plot, fargs=(people, bar_data))

plt.show()
