import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# Variable definitions
item_value = 50
people_count = 480
max_days = 1000

# Initialize people's money
people1 = [item_value for _ in range(people_count)]  # For the sorted animation
people2 = [item_value for _ in range(people_count)]  # For the unsorted animation

# Initialize animation for sorted data
fig1, ax1 = plt.subplots()
plt.xlabel('Personer')
plt.ylabel('Kronor')
plt.title('Slumpmässig ojämlikhet - Sorterad')
people_number1 = list(range(people_count, 0, -1))  # Reverse order
bar_data1 = ax1.bar(people_number1, people1)
variance_text1 = ax1.text(0.2, 0.4, '', ha='left')

# Initialize animation for unsorted data
fig2, ax2 = plt.subplots()
plt.xlabel('Personer')
plt.ylabel('Kronor')
plt.title('Slumpmässig ojämlikhet - Osorterad')
people_number2 = list(range(people_count, 0, -1))  # Reverse order
bar_data2 = ax2.bar(people_number2, people2)
variance_text2 = ax2.text(0.2, 0.4, '', ha='left')

# Function to update plot data and visualization for sorted data
def update_plot1(frame, people, bar_data):
    if frame >= max_days:
        ani1.event_source.stop()  # Stop animation if max_days is reached

    max_money = np.max(people)
    y_lim_buffer = 5
    ax1.set_ylim(0, max_money + y_lim_buffer)

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

    people.sort()

    for i in range(len(people)):
        bar_data[i].set_height(people[i])

    ax1.set_title(f'Slumpmässig ojämlikhet - Sorterad - Dag {frame + 1}')

    variance = np.var(people)
    std_deviation = np.std(people)
    range_difference = np.ptp(people)
    mean_value = np.mean(people)

    above_starting_value = sum(1 for p in people if p > item_value)
    below_starting_value = sum(1 for p in people if p < item_value)

    variance_text1.set_text(f'Varians: {variance:.2f}\nStandardavvikelse: {std_deviation:.2f}\nHögsta-lägsta: {range_difference:.2f}\nMedelvärde: {mean_value:.2f}\n'
                            f'Antal personer över startvärde: {above_starting_value}\nAntal personer under startvärde: {below_starting_value}')

    return bar_data

# Function to update plot data and visualization for unsorted data
def update_plot2(frame, people, bar_data):
    if frame >= max_days:
        ani2.event_source.stop()  # Stop animation if max_days is reached

    max_money = np.max(people)
    y_lim_buffer = 5
    ax2.set_ylim(0, max_money + y_lim_buffer)

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

    for i in range(len(people)):
        bar_data[i].set_height(people[i])

    ax2.set_title(f'Slumpmässig ojämlikhet - Osorterad - Dag {frame + 1}')

    variance = np.var(people)
    std_deviation = np.std(people)
    range_difference = np.ptp(people)
    mean_value = np.mean(people)

    above_starting_value = sum(1 for p in people if p > item_value)
    below_starting_value = sum(1 for p in people if p < item_value)

    variance_text2.set_text(f'Varians: {variance:.2f}\nStandardavvikelse: {std_deviation:.2f}\nHögsta-lägsta: {range_difference:.2f}\nMedelvärde: {mean_value:.2f}\n'
                            f'Antal personer över startvärde: {above_starting_value}\nAntal personer under startvärde: {below_starting_value}')

    return bar_data

# Create animations
ani1 = animation.FuncAnimation(fig1, update_plot1, fargs=(people1, bar_data1))
ani2 = animation.FuncAnimation(fig2, update_plot2, fargs=(people2, bar_data2))

plt.show()
