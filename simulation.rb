# Variabel definiering
item_value = 50
people_count = 50
max_days = 100

# Skapa en lista med X antal människor, med X antal pengar
people = [people_count] * item_value

# Genomför simuleringen
days = 0
while days < max_days

    # Loopa igenom varje person
    index = 0
    while index < people.length-1

        # Personen förlorar sin peng
        people[index]-=1

        # En annan slumpmässig person får en ny peng
        people[rand(0..people.length-1)]+=1

        # Inkrementera people index
        index+=1
    end
    days+=1
end

# Print the list
print(people)
