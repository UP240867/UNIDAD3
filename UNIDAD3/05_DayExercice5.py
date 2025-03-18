empty_list = []

items = [10, 20, 30, 40, 50, 60]

print(len(items))

print(items[0], items[len(items)//2], items[-1])

mixed_data_types = ["Alex", 30, 1.80, "Casado", "Calle Falsa 123"]

it_companies = ["Twitter", "Spotify", "Netflix", "Adobe", "Intel", "Salesforce", "TikTok"]

print(it_companies)

print(len(it_companies))

print(it_companies[0], it_companies[len(it_companies)//2], it_companies[-1])

it_companies[0] = "X (Twitter)"
print(it_companies)

it_companies.append("SpaceX")
print(it_companies)

it_companies.insert(len(it_companies)//2, "Snapchat")
print(it_companies)

it_companies[1] = it_companies[1].upper()
print(it_companies)

print("#; ".join(it_companies))

print("Spotify" in it_companies)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

print(it_companies[:3])

print(it_companies[-3:])

del it_companies[len(it_companies)//2]
print(it_companies)

it_companies.pop(0)
print(it_companies)

del it_companies[len(it_companies)//2]
print(it_companies)

it_companies.pop()
print(it_companies)

it_companies.clear()
print(it_companies)

front_end = ['Vue.js', 'Tailwind', 'TypeScript', 'React', 'Redux']
back_end = ['Django', 'Spring Boot', 'PostgreSQL']
full_stack = front_end + back_end
print(full_stack)

full_stack.insert(full_stack.index("Redux") + 1, "Go")
full_stack.insert(full_stack.index("Go") + 1, "Rust")
print(full_stack)

ages = [21, 29, 23, 31, 25, 28, 30, 27, 26, 24]

ages.sort()
print(ages[0], ages[-1])

ages.append(ages[0])
ages.append(ages[-1])
print(ages)

median = ages[len(ages)//2] if len(ages) % 2 != 0 else (ages[len(ages)//2 - 1] + ages[len(ages)//2]) / 2
print(median)

average = sum(ages) / len(ages)
print(average)

print(max(ages) - min(ages))

print(abs(min(ages) - average), abs(max(ages) - average))

countries = ['Japón', 'Corea del Sur', 'India', 'Italia', 'Alemania', 'Canadá', 'Australia']
print(countries[len(countries)//2])

half = len(countries) // 2
first_half = countries[:half + (len(countries) % 2)]
second_half = countries[half + (len(countries) % 2):]
print(first_half, second_half)

first, second, third, *others = countries
print(first, second, third, others)
