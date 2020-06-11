def count_letter(value, letter):
    count = 0
    for i in value:
        if i == letter:
            count +=1
    return count

print(count_letter('romit','o'))