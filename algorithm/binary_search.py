

def binary_search(search_list, item):
    low = 0
    high = len(search_list)-1
    while low <= high:
        middle = (low + high)//2
        if search_list[middle] == item:
            return middle
        elif search_list[middle] < item:
            low = middle+1
        else: #  search_list[middle] > item
            high = middle-1
    return None

