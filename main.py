import numpy as np

class DataAnalytics:
    """NumPy Analyzer integrating NumPy + OOP principles"""
    
    def __init__(self, array=None):
        self.__array = array  # Encapsulation: private variable
        self.__history = []

    # --- Private Methods for internal computations ---
    def __validate_array(self):
        if self.__array is None:
            print("No array created yet! Please create an array first.")
            return False
        return True

    def __parse_range(self, range_str):
        
        try:
            if ":" in range_str:
                parts = range_str.split(":")
                start = int(parts[0]) if parts[0] != '' else None
                end = int(parts[1]) if parts[1] != '' else None
                return slice(start, end)
            else:
                return int(range_str)
        except:
            return slice(None)

    # --- Class and Static Methods (OOP Requirement) ---
    @classmethod
    def from_list(cls, data_list):
        """Create object from Python list """
        return cls(np.array(data_list))

    @staticmethod
    def is_valid_numeric(value):
        """Check if value is numeric"""
        try:
            float(value)
            return True
        except:
            return False

    @staticmethod
    def show_info():
        print("NumPy Analyzer v1.0 | Uses NumPy for data analysis")

    # --- 1. Array Management: Creation, Indexing, Slicing ---
    def create_array(self):
        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")
        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                n = int(input("Enter the number of elements: "))
                elems = input(f"Enter {n} elements separated by space: ")
                arr = np.array(list(map(float, elems.split()))[:n])
                self.__array = arr

            elif choice == '2':
                r = int(input("Enter the number of rows: "))
                c = int(input("Enter the number of columns: "))
                total = r * c
                elems = input(f"Enter {total} elements for the array separated by space: ")
                data = list(map(float, elems.split()))
                self.__array = np.array(data[:total]).reshape(r, c)

            elif choice == '3':
                d = int(input("Enter depth: "))
                r = int(input("Enter rows: "))
                c = int(input("Enter columns: "))
                total = d * r * c
                elems = input(f"Enter {total} elements separated by space: ")
                data = list(map(float, elems.split()))
                self.__array = np.array(data[:total]).reshape(d, r, c)
            else:
                print("Invalid choice")
                return
            
            print("\nArray created successfully:")
            print(self.__array)
        
        except Exception as e:
            print(f"Error creating array: {e}")

    def indexing_slicing_menu(self):
        if not self.__validate_array(): return
        print("\nChoose an operation:")
        print("1. Indexing")
        print("2. Slicing")
        print("3. Go Back")
        ch = input("Enter your choice: ")

        if ch == '1':
            try:
                if self.__array.ndim == 1:
                    idx = int(input(f"Enter index (0 to {self.__array.shape[0]-1}): "))
                    print(f"Element at {idx}: {self.__array[idx]}")
                elif self.__array.ndim == 2:
                    r = int(input("Enter row index: "))
                    c = int(input("Enter column index: "))
                    print(f"Element at [{r},{c}]: {self.__array[r, c]}")
            except Exception as e:
                print(f"Error: {e}")

        elif ch == '2':
            try:
                row_range = input("Enter the row range (start:end): ")
                col_range = input("Enter the column range (start:end): ")
                r_slice = self.__parse_range(row_range)
                c_slice = self.__parse_range(col_range)
                
                if self.__array.ndim == 2:
                    sliced = self.__array[r_slice, c_slice]
                else:
                    sliced = self.__array[r_slice]
                
                print("\nSliced Array:")
                print(sliced)
            except Exception as e:
                print(f"Error: {e}")

    # --- 2. Mathematical Operations ---
    def mathematical_operations(self):
        if not self.__validate_array(): return
        print("\nChoose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Dot Product")
        print("6. Matrix Multiplication")
        ch = input("Enter your choice: ")

        # For dot/matmul we need 2 arrays
        if ch in ['5', '6']:
            try:
                elems = input(f"Enter second array elements ({self.__array.size} elements): ")
                arr2 = np.array(list(map(float, elems.split()))).reshape(self.__array.shape)
                if ch == '5':
                    result = np.dot(self.__array, arr2.T) if self.__array.ndim == 2 else np.dot(self.__array, arr2)
                    print(f"Dot Product:\n{result}")
                else:
                    result = np.matmul(self.__array, arr2) if self.__array.ndim == 2 else np.matmul(self.__array, arr2)
                    print(f"Matrix Multiplication:\n{result}")
            except Exception as e:
                print(f"Error: {e}")
            return

        try:
            total = self.__array.size
            elems = input(f"Enter the same-size array elements ({total} elements separated by space): ")
            arr2 = np.array(list(map(float, elems.split()))[:total]).reshape(self.__array.shape)
            
            print("\nOriginal Array:")
            print(self.__array)
            print("\nSecond Array:")
            print(arr2)

            if ch == '1':
                res = self.__array + arr2
                print(f"\nResult of Addition:\n{res}")
            elif ch == '2':
                res = self.__array - arr2
                print(f"\nResult of Subtraction:\n{res}")
            elif ch == '3':
                res = self.__array * arr2
                print(f"\nResult of Multiplication:\n{res}")
            elif ch == '4':
                res = self.__array / arr2
                print(f"\nResult of Division:\n{res}")
        except Exception as e:
            print(f"Error: {e}")

    # --- 3. Combine or Split ---
    def combine_split(self):
        if not self.__validate_array(): return
        print("\nChoose an option:")
        print("1. Combine Arrays")
        print("2. Split Array")
        ch = input("Enter your choice: ")

        try:
            if ch == '1':
                total = self.__array.size
                elems = input(f"Enter the elements of another array to combine ({total} elements separated by space): ")
                arr2 = np.array(list(map(float, elems.split()))[:total]).reshape(self.__array.shape)
                
                print("\nOriginal Array:")
                print(self.__array)
                print("\nSecond Array:")
                print(arr2)
                
                combined = np.vstack((self.__array, arr2))
                print(f"\nCombined Array (Vertical Stack):\n{combined}")

            elif ch == '2':
                parts = int(input("Enter number of splits: "))
                split_arr = np.array_split(self.__array, parts)
                print(f"\nSplit into {parts} parts:")
                for i, p in enumerate(split_arr):
                    print(f"Part {i+1}:\n{p}")
        except Exception as e:
            print(f"Error: {e}")

    # --- 4. Search, Sort, Filter ---
    def search_sort_filter(self):
        if not self.__validate_array(): return
        print("\nChoose an option:")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")
        ch = input("Enter your choice: ")

        try:
            print("\nOriginal Array:")
            print(self.__array)

            if ch == '1':
                val = float(input("Enter value to search: "))
                indices = np.where(self.__array == val)
                print(f"Value {val} found at indices: {indices}")

            elif ch == '2':
                # Sorting row-wise
                sorted_arr = np.sort(self.__array, axis=1) if self.__array.ndim == 2 else np.sort(self.__array)
                print(f"\nSorted Array:\n{sorted_arr}")
                print("(Sorting applied row-wise.)")

            elif ch == '3':
                cond = input("Enter condition (e.g., >30, <50, ==20): ")
                
                if ">" in cond:
                    v = float(cond.replace(">", ""))
                    filtered = self.__array[self.__array > v]
                elif "<" in cond:
                    v = float(cond.replace("<", ""))
                    filtered = self.__array[self.__array < v]
                elif "==" in cond:
                    v = float(cond.replace("==", ""))
                    filtered = self.__array[self.__array == v]
                else:
                    print("Invalid condition")
                    return
                print(f"Filtered Array ({cond}): {filtered}")
        except Exception as e:
            print(f"Error: {e}")

    # --- 5. Aggregates and Statistics ---
    def aggregates_and_statistics(self):
        if not self.__validate_array(): return
        print("\nChoose an aggregate/statistical operation:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        print("6. Min / Max")
        print("7. Percentiles")
        print("8. Correlation Coefficient")
        ch = input("Enter your choice: ")

        try:
            print("\nOriginal Array:")
            print(self.__array)

            if ch == '1':
                print(f"Sum of Array: {np.sum(self.__array)}")
            elif ch == '2':
                print(f"Mean of Array: {np.mean(self.__array)}")
            elif ch == '3':
                print(f"Median of Array: {np.median(self.__array)}")
            elif ch == '4':
                print(f"Standard Deviation: {np.std(self.__array)}")
            elif ch == '5':
                print(f"Variance: {np.var(self.__array)}")
            elif ch == '6':
                print(f"Min: {np.min(self.__array)}, Max: {np.max(self.__array)}")
            elif ch == '7':
                p = int(input("Enter percentile (0-100): "))
                print(f"{p}th Percentile: {np.percentile(self.__array, p)}")
            elif ch == '8':
                total = self.__array.size
                elems = input(f"Enter second array ({total} elements) for correlation: ")
                arr2 = np.array(list(map(float, elems.split()))[:total])
                corr = np.corrcoef(self.__array.flatten(), arr2)[0,1]
                print(f"Correlation Coefficient: {corr}")

        except Exception as e:
            print(f"Error: {e}")

# --- Main Menu Driven UI ---
def main():
    analyzer = DataAnalytics()
    print("\nWelcome to the NumPy Analyzer!")
    print("========================================")

    while True:
        print("\nChoose an option:")
        print("1. Create a Numpy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            analyzer.create_array()
            
            analyzer.indexing_slicing_menu()

        elif choice == '2':
            analyzer.mathematical_operations()
        elif choice == '3':
            analyzer.combine_split()
        elif choice == '4':
            analyzer.search_sort_filter()
        elif choice == '5':
            analyzer.aggregates_and_statistics()
        elif choice == '6':
            print("\nThank you for using the NumPy Analyzer! Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()