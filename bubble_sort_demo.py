# Aaron Walker

mylist = [64, 25, 12, 22, 11]

print("Original list:", mylist)

# Loop until the list is sorted
sorting = True
pass_number = 0

while sorting:
    sorting = False
    pass_number += 1

    # Compare adjacent elements
    for i in range(len(mylist) - 1):
        if mylist[i] > mylist[i + 1]:
            # Swap elements if they are in the wrong order
            mylist[i], mylist[i + 1] = mylist[i + 1], mylist[i]
            sorting = True

    # Display the list after each pass
    print("After pass", pass_number, ":", mylist)

print("Sorted list:", mylist)
