def find(lst, sum):
    #find indexes of 2 elements that sum up to $sum
    try:
        for i, val in enumerate(lst):
            for k, other in enumerate(lst[i+1:]):
                if val + other == sum:return (i,k +i+1)
    except Exception as err:
        return None

def main():
    lst = [1, 2, 3, 4, 5, 6, 7]
    sum = 10
    print(find(lst, sum))

if __name__ == "__main__":
    main()