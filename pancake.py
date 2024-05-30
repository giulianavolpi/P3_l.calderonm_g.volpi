def flip(arr, i):
    start = 0
    while start < i:
        arr[start], arr[i] = arr[i], arr[start]
        start += 1
        i -= 1

def find_max(arr, n):
    mi = 0
    for i in range(1, n):
        if arr[i] > arr[mi]:
            mi = i
    return mi

def pancake_sort(arr):
    flips = []
    n = len(arr)
    for curr_size in range(n, 1, -1):
        mi = find_max(arr, curr_size)
        if mi!= curr_size - 1:
            if mi!= 0:
                flip(arr, mi)
                flips.append(mi + 1)  # 1-based index
            flip(arr, curr_size - 1)
            flips.append(curr_size)  # 1-based index
    flips.append(0)  # To mark the end of the sequence
    return flips

def main():
    num_cases = int(input())
    results = []

    for _ in range(num_cases):
        pancakes = list(map(int, input().split()))
        if pancakes == sorted(pancakes, reverse=True):
            results.append("ORDENADO")
        else:
            flips = pancake_sort(pancakes)
            results.append(" ".join(map(str, flips)))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()







 
