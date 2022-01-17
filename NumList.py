# Display numbers from a list using loop
number = [12, 75, 150, 180, 145, 525, 50]
for lists in number:
    if lists > 500:
        break
    elif lists > 150:
        continue
    elif lists % 5 != 0:
        continue
    else:
        print(lists)
