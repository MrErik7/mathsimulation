import random
import numpy as np
import matplotlib.pyplot as plt

# Variabel definiering
item_value = 50
people_count = 480
max_days = 100

# Skapa en lista med X antal människor, med X antal pengar
people = []
for i in range(people_count):  
    people.append(item_value)  

# Genomför simuleringen
days = 0
while days < max_days:

    # Loopa igenom varje person
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


    days += 1

    print(days)


# Sortera people för att skapa en ordnad visualisering
sorted_people = sorted(people)

# Måla upp ett visuellt diagram för den sorterade listan
plt.figure()
plt.bar(range(1, len(sorted_people) + 1), sorted_people)
plt.title('Slumpmässig ojämlikhet - Sorterad')
plt.xlabel('Personer')
plt.ylabel('Kronor')

variance = np.var(sorted_people)
std_deviation = np.std(sorted_people)
range_difference = np.ptp(sorted_people)
mean_value = np.mean(sorted_people)
above_starting_value = sum(1 for p in sorted_people if p > item_value)
below_starting_value = sum(1 for p in sorted_people if p < item_value)

plt.text(0.2, 0.4, f'Varians: {variance:.2f}\nStandardavvikelse: {std_deviation:.2f}\nHögsta-lägsta: {range_difference:.2f}\nMedelvärde: {mean_value:.2f}\n'
         f'Antal personer över startvärde: {above_starting_value}\nAntal personer under startvärde: {below_starting_value}', ha='left')

# Måla upp ett visuellt diagram för den ursprungliga listan
plt.figure()
plt.bar(range(1, len(people) + 1), people)
plt.title('Slumpmässig ojämlikhet - Osorterad')
plt.xlabel('Personer')
plt.ylabel('Kronor')

variance = np.var(people)
std_deviation = np.std(people)
range_difference = np.ptp(people)
mean_value = np.mean(people)
above_starting_value = sum(1 for p in people if p > item_value)
below_starting_value = sum(1 for p in people if p < item_value)

plt.text(0.2, 0.4, f'Varians: {variance:.2f}\nStandardavvikelse: {std_deviation:.2f}\nHögsta-lägsta: {range_difference:.2f}\nMedelvärde: {mean_value:.2f}\n'
         f'Antal personer över startvärde: {above_starting_value}\nAntal personer under startvärde: {below_starting_value}', ha='left')

plt.show()
