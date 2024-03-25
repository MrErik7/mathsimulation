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
    index = 0
    while index < len(people):

        # Kolla så att personen inte har noll, isåfall skippa
        if (people[index] == 0):
            continue

        # Personen förlorar sin peng
        people[index]-=1

        # En annan slumpmässig person får en ny peng
        people[random.randrange(0, len(people))]+=1

        # Inkrementera people index
        index+=1
    days+=1

# Skapa en lista för person 1 --> person 50
people_number = list(range(1, people_count + 1)) 

# Beräkna variansen och standardavvikelsen
variance = np.var(people)
std_deviation = np.std(people)

people.sort()


print(people)

# Måla upp ett visuellt diagram
plt.bar(people_number, people)
plt.xlabel('Personer')
plt.ylabel('Kronor')
plt.title('Slumpmässig ojämlikhet')
plt.figtext(0.6, 0.7, f'Varians: {variance:.2f}\nStandard avvikelse: {std_deviation:.2f}\nAntal dagar: {max_days}', ha='left')
plt.show()

