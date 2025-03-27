weights = [45, 59, 90, 32, 56, 43, 41, 99, 55, 56, 78, 43, 31, 33, 98]

# Counters for each category
skinny_count = 0
healthy_count = 0
fat_count = 0

# Loop through each weight and count categories
for weight in weights:
    if weight < 55:
        skinny_count = skinny_count + 1
    elif 55 < weight < 65:
        healthy_count = healthy_count+ 1
    else: 
        fat_count = fat_count+ 1

# Print results
print("Skinny people are:",  skinny_count)
print("Healthy people are: ", healthy_count)
print("Fat people are: ", fat_count)