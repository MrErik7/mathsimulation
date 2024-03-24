import random
import matplotlib.pyplot as plt

# Variabel definiering
item_value = 50
people_count = 50
max_days = 100

# Skapa en lista med X antal människor, med X antal pengar
people = []
for i in range(people_count):  
    people.append(item_value)  

# Måla upp ett visuellt diagram
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()
bars = ax.bar(range(1, people_count + 1), 200)

# Genomför simuleringen
days = 0
while days < max_days:

    # Loopa igenom varje person
    index = 0
    while index < len(people):

        # Kolla så att personen inte har noll, isåfall skippa
        if people[index] == 0:
            continue

        # Personen förlorar sin peng
        people[index] -= 1

        # En annan slumpmässig person får en ny peng
        people[random.randrange(0, len(people))] += 1

        # Uppdatera baren för den aktuella personen
        bars[index].set_height(people[index])

        # Uppdatera plottet
        plt.pause(0.001)

        # Inkrementera people index
        index += 1

    days += 1

plt.ioff()  # Turn off interactive mode after the loop
plt.show()
