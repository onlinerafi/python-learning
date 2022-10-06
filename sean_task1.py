""" sean task 1
"""
def determine_three_elements_add_to_k(arr, K):
    """
    Given an array of numbers and a number k,
    determine if there are three entries in the
    array which add up to the specified number k.

    For example, given [20, 303, 3, 4, 25] and 
    k = 49, return true as 20 + 4 + 25 = 49.
    """
    for i in arr[:-2]:
        if i >= K: continue
        for j in arr[:-1]:
            if sum((i, j)) >= K: continue
            for k in arr:
                if sum((i, j, k)) == K:
                    return True, i, j, K
    return False

def main():
    """Get user input"""
    arr=[23,34,25,567,42,87,4,8,65]
    K=int(input("Enter Value for K: "))
    return arr, K

if __name__ == '__main__':
    arr, K = main()
    print(determine_three_elements_add_to_k(arr, K))
