print("Wlcome to Data Analyzer and Transformer Program.")

arr = []

def array():
    """This Function takes 1D array input separated by spaces."""
    global arr
    arr = list(map(int, input("Enter data for a 1D array (separated by spaces):\n").split()))
    print("Your data added successfully...")
    print(f"\nYour data: {arr}")
    
def summary():
    """Display Dataset Summary using Built-In functions."""
    
    print("\nData Summary:")
    print(f"-Total Elements: {len(arr)}")
    print(f"-Minimum value: {min(arr)}")
    print(f"-Maximum value: {max(arr)}")
    print(f"-Sum of all values: {sum(arr)}")
    print(f"-Average of values: {sum(arr)/len(arr)}")
    
def factorial(n):
    """Recursive function to calculate factorial using given argument."""
    
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

def threshold():
    """Filters data using lambda function."""
    
    if not arr:
        print("No data avaible!")
        return
    
    n = int(input("\nEnter a threshold value to filter out data above this value: "))
    filtered = list(filter(lambda x: x>n, arr))
    print(f"Filtered Data (Values >= {n}): \n{filtered}") 

def sort_data():
    """Demonstrates sort() vs sorted()."""
    
    if not arr:
        print("No data available!")
        return

def data_statistic():
    """Returns multiple statistics values."""
    if not arr:
        print("No data available!")
        return
    
    maximum = max(arr)
    minimum = min(arr)
    total = sum(arr)
    average = total / len(arr)
    
    return minimum, maximum, total, average

def display_stat():
    stats = data_statistic()
    if stats:
        minimum, maximum, total, average = stats
        print("\nDataset Statistics:")
        print(f"Minimum Value: {minimum}")
        print(f"Maximum Value: {maximum}")
        print(f"Total Value: {total}")
        print(f"Average Value: {average}")
    
while True:
    print(f"\n{'-'*20} Main Menu {'-'*20}")
    print("1.Input Data")
    print("2.Display Data Summury (Built-In Function)")
    print("3.Calculate Factorial (Recursion)")
    print("4.Filter data by Threshold (Lambda Function)")
    print("5.Sort data")
    print("6.Display Data Set Statistics (Return Multiple Values)")
    print("7.Exit Program")
    
    choice = int(input("\nEnter your choice: "))
    
    match choice:
        case 1:
            array()
         
        case 2:
            summary()
         
        case 3:
            n = int(input("\nEnter a number to calculate factorial: "))
            result = factorial(n)
            print(f"Factorial of {n} is : {result}")
         
        case 4:
            threshold()
         
        case 5:
            sort_data()
            print("\nChoose Sorting option:")
            print("1.Ascending Order")
            print("1.Descending Order")
            
            option = int(input("\nEnter your option: "))
            
            match option:
                case 1:
                    a_sort = arr.copy()
                    a_sort.sort()
                    print(f"Sorted data in Ascending Order using Sort(): \n{a_sort}")
                    
                case 2:
                    d_sort = sorted(arr, reverse=True)
                    print(f"Sorted data in Descending Order using Sorted(): \n{d_sort}")
                    
                case _:
                    print("Invalid Input!!")
         
        case 6:
            display_stat()
         
        case 7:
            print("Exiting the Program...")
            break
         
        case _:
            print("Invalid Input!!")

print("Thank you for using the Data Analyzer and Transformer Program. \nGood Bye!!")