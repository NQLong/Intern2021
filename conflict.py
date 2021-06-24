def find(lst, sum):
# <<<<<<< HEAD
    # find indexes of 2 elements that sum up to $sum
    my_hash_table = dict()
    for i, val in enumerate(lst):
        my_hash_table[f"{val}"] = i
    for i, val in enumerate(lst):
        other = my_hash_table.get(f"{sum - val}")
        if other:return (i,other)
    
# =======
#     #find indexes of 2 elements that sum up to $sum
#     try:
#         for i, val in enumerate(lst):
#             for k, other in enumerate(lst[i+1:]):
#                 if val + other == sum:return (i,k +i+1)
#     except Exception as err:
#         return None

# >>>>>>> refs/remotes/origin/main
def main():
    lst = [1, 2, 3, 4, 5, 6, 7]
    sum = 10
    print(find(lst, sum))


if __name__ == "__main__":
    main()