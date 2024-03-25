import random
import numpy as np
import matplotlib.pyplot as plt

# Variable definitions
item_value = 50
people_count = 480
max_days = 10000

# Initialize people's money
people1 = [item_value for _ in range(people_count)]  # For the sorted animation
people2 = [item_value for _ in range(people_count)]  # For the unsorted animation

# Function to update plot data and visualization for sorted data
def update_plot1(frame, people, ax, bar_data):
    ax.set_ylim(0, 200)

    for _ in range(1000):  # Run for 1000 days
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

    ax.set_title('Slumpmässig ojämlikhet - Sorterad - Dag 1000')

    variance = np.var(people)
    std_deviation = np.std(people)
    range_difference = np.ptp(people)
    mean_value = np.mean(people)

    above_starting_value = sum(1 for p in people if p > item_value)
    below_starting_value = sum(1 for p in people if p < item_value)

    ax.text(0.2, 0.4, f'Varians: {variance:.2f}\nStandardavvikelse: {std_deviation:.2f}\nHögsta-lägsta: {range_difference:.2f}\nMedelvärde: {mean_value:.2f}\n'
            f'Antal personer över startvärde: {above_starting_value}\nAntal personer under startvärde: {below_starting_value}', ha='left')

# Function to update plot data and visualization for unsorted data
def update_plot2(frame, people, ax, bar_data):
    ax.set_ylim(0, 200)

    for _ in range(1000):  # Run for 1000 days
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

    ax.set_title('Slumpmässig ojämlikhet - Osorterad - Dag 1000')

    variance = np.var(people)
    std_deviation = np.std(people)
    range_difference = np.ptp(people)
    mean_value = np.mean(people)

    above_starting_value = sum(1 for p in people if p > item_value)
    below_starting_value = sum(1 for p in people if p < item_value)

    ax.text(0.2, 0.4, f'Varians: {variance:.2f}\nStandardavvikelse: {std_deviation:.2f}\nHögsta-lägsta: {range_difference:.2f}\nMedelvärde: {mean_value:.2f}\n'
            f'Antal personer över startvärde: {above_starting_value}\nAntal personer under startvärde: {below_starting_value}', ha='left')

# Initialize plot for sorted data
fig1, ax1 = plt.subplots()
plt.xlabel('Personer')
plt.ylabel('Kronor')
bar_data1 = ax1.bar(range(1, people_count + 1), people1)
update_plot1(999, people1, ax1, bar_data1)

# Initialize plot for unsorted data
fig2, ax2 = plt.subplots()
plt.xlabel('Personer')
plt.ylabel('Kronor')
bar_data2 = ax2.bar(range(1, people_count + 1), people2)
update_plot2(999, people2, ax2, bar_data2)

plt.show()
