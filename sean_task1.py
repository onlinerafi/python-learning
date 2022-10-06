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
    ln=len(arr)
    for i in range(ln-2):
        if arr[i]>=K: continue
        for j in range(ln-1):
            if arr[i]+arr[j]>=K: continue
            for k in range(ln):
                if arr[i]+arr[j]+arr[k]==K: 
                    return True,arr[i],arr[j],arr[k]
    return False

def main():
    """Get user input"""
    arr=[23,34,25,567,42,87,4,8,65]
    K=int(input("Enter Value for K: "))
    return arr, K

if __name__ == '__main__':
    arr, K = main()
    print(determine_three_elements_add_to_k(arr, K))
