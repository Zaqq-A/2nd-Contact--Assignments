import os

with open("Name.txt", "r") as file:
    full_name = file.read().strip()

name_parts = full_name.split()

first_name = name_parts[0] if len(name_parts) > 0 else ""
middle_name = " ".join(name_parts[1:-1]) if len(name_parts) > 2 else ""
last_name = name_parts[-1] if len(name_parts) > 1 else ""

print(f"First Name: {first_name}")
print(f"Middle Name: {middle_name}")
print(f"Last Name: {last_name}")


# The file path

file_path = os.path.abspath("Name.txt")

print(f"Full File Path: {file_path}")
print("-" * 50)


# Extraction of baby name from file using regex

import re

with open("baby2008.html", "r", encoding="utf-8") as file:
    html_content = file.read()

pattern = r"<tr[^>]*>\s*<td>(\d+)</td>\s*<td>([A-Za-z]+)</td>\s*<td>([A-Za-z]+)</td>\s*</tr>"
matches = re.findall(pattern, html_content)

all_names = []
for rank, male_name, female_name in matches:
    all_names.append((male_name, "Male", int(rank)))
    all_names.append((female_name, "Female", int(rank)))

print(f"Total names extracted: {len(all_names)}")


# Sort Algorithm 
def merge_sort(records):
    if len(records) <= 1:
        return records

    mid = len(records) // 2
    left_half = merge_sort(records[:mid])
    right_half =  merge_sort(records[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    sorted_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        
        if left[i][0].lower() <= right[j][0].lower():
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Append any remaining elements
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list


sorted_records = merge_sort(all_names)
print("First 5 sorted records:", sorted_records[:5])


# Binary Search Algorithm
def binary_search(sorted_list, target_name):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_name = sorted_list[mid][0]

        if mid_name.lower() == target_name.lower():
            return mid  # Return index of a match
        elif mid_name.lower() < target_name.lower():
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Test Binary Search on the 2008 dataset
search_target = "Jordan"
index = binary_search(sorted_records, search_target)

if index != -1:
    name, gender, rank = sorted_records[index]
    print(f"Found '{name}' ({gender}) at Rank #{rank} (Sorted Index: {index}).")
else:
    print(f"'{search_target}' was not found in the top 1,000 names of 2008.")
