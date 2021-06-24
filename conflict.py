def find(lst, sum):
    # find indexes of 2 elements that sum up to $sum
    my_hash_table = dict()
    for i, val in enumerate(lst):
        my_hash_table[f"{val}"] = i
    for i, val in enumerate(lst):
        other = my_hash_table.get(f"{sum - val}")
        if other:return (i,other)
    
def main():
    lst = [1, 2, 3, 4, 5, 6, 7]
    sum = 10
    print(find(lst, sum))


if __name__ == "__main__":
    main()
