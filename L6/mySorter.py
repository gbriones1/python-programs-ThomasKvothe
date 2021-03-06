import csv
import time

class mySorter():
    """ CLASS THAT HANDLES CSV FILES AND IMPLEMENTS METHODS FOR SORTING THEIR CONTENT"""
    
    def __init__(self, alist = None):
        self.alist = alist
        self.records_sorted = 0
        self.start_time = None
        self.end_time = None
        
    def set_input_data(self, file_path_name: str):
        """This methods sets the information about the file that will be used to read the data"""
        try:
            self.alist = []
            with open(file_path_name) as csvfile:
                readCSV = csv.reader(csvfile, delimiter = ',')
                for row in readCSV:
                    for element in row:
                        self.alist.append(float(element))
        except FileNotFoundError:
            print("File doesn't exist")
            return False
        except ValueError:
            print("A value found is not a number")
            return False
        return True
    
    def set_output_data(self, file_path_name: str):
        """This methods sets the information about the file that will be used to store the sorted data"""
        with open(file_path_name, 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',')
            filewriter.writerow(self.alist)
    
    def execute_heap_sort(self):
        """This methods sorts the data contained in the file specified"""
        self.records_sorted = len(self.alist)
        self.start_time = time.time()
        arr = self.alist
        n = len(arr) 
    
        # Build a maxheap. 
        for i in range(n, -1, -1): 
            self._heap_sort_recursion(arr, n, i) 
    
        # One by one extract elements 
        for i in range(n-1, 0, -1): 
            arr[i], arr[0] = arr[0], arr[i] # swap 
            self._heap_sort_recursion(arr, i, 0)
        self.end_time = time.time()

    def _heap_sort_recursion(self, arr, n, i):
        # Find largest among root and children
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2 
        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
        # If root is not largest, swap with largest and continue heapifying
        if largest != i:
            arr[i],arr[largest] = arr[largest],arr[i]
            self._heap_sort_recursion(arr, n, largest)
    
    def execute_quick_sort(self):
        """This methods sorts the data contained in the file specified"""
        self.records_sorted = len(self.alist)
        self.start_time = time.time()
        self._quick_sort_recursion(self.alist, 0, len(self.alist)-1)
        self.end_time = time.time()
    
    def get_performance_data(self):
        """This method returns the performance data associated to the last sorting execution
            [Number of Records Sorted, TimeConsumed, StartTime, EndTime]"""
        time_consumed = None
        if self.start_time and self.end_time:
            time_consumed = self.end_time - self.start_time
        performance_data = {
            "Records Sorted": self.records_sorted,
            "Time Consumed": time_consumed,
            "Start Time": self.start_time,
            "End Time": self.end_time
        }
        return performance_data
    
    def _partition(self, array, begin, end):
        pivot_idx = begin
        for i in range(begin+1, end+1):
            if array[i] <= array[begin]:
                pivot_idx += 1
                array[i], array[pivot_idx] = array[pivot_idx], array[i]
        array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
        return pivot_idx

    def _quick_sort_recursion(self, array, begin, end):
        if begin >= end:
            return
        pivot_idx = self._partition(array, begin, end)
        self._quick_sort_recursion(array, begin, pivot_idx-1)
        self._quick_sort_recursion(array, pivot_idx+1, end)

    def execute_merge_sort(self):
        self.records_sorted = len(self.alist)
        self.start_time = time.time()
        self._merge_sort_recursion(self.alist)
        self.end_time = time.time()

    def _merge_sort_recursion(self, alist):
        #print("Splitting ",alist)
        if len(alist)>1:
            mid = len(alist)//2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]

            self._merge_sort_recursion(lefthalf)
            self._merge_sort_recursion(righthalf)

            i=0
            j=0
            k=0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    alist[k]=lefthalf[i]
                    i=i+1
                else:
                    alist[k]=righthalf[j]
                    j=j+1
                k=k+1

            while i < len(lefthalf):
                alist[k]=lefthalf[i]
                i=i+1
                k=k+1

            while j < len(righthalf):
                alist[k]=righthalf[j]
                j=j+1
                k=k+1
        #print("Merging ",alist)
