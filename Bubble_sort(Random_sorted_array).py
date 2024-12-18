import random

def bubble_sort(arr, ascending=True):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if (ascending and arr[j] > arr[j + 1]) or (not ascending and arr[j] < arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    arr = [random.randint(1, 100) for _ in range(20)]
    order = input("Enter 'asc' for ascending order or 'desc' for descending order: ")
    if order.lower() == 'asc':
        bubble_sort(arr, ascending=True)
        print("Sorted array:", arr)
    
    elif order.lower() == 'desc':
        bubble_sort(arr, ascending=False)
        print("Sorted array:", arr)
    
    else:
        print("Invalid input. Please enter 'asc' or 'desc' for sorting the array.")


if __name__ == "__main__":
    main()
