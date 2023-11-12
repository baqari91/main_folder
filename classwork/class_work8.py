# li = [1,2,3,4,5,6,7,8,9]
# filtered = list(filter(lambda x: x%3==0,li))
# print(filtered)

# li = [1,2,3,4,5,6,7,8,9]
# filtered = list(filter(lambda x: x%7!=0,li))
# print(filtered)

# names = input("enter names with space: ").split()
# ages = input("enter 3 ages: ").split()
# print(list(zip(names,ages)))

# try:
#     a = int(input("enter num: "))
#     b = int(input("enter num: "))
# except:
#     print("enter integer")
# try:
#     print(a/b)
# except:
#     raise Exception("Zero division")

# def bubble_sort():
#     arr=[3,5,6,3,1,23,4,2]
#     n = len(arr)-1
#     sorted2 = False
#     while not sorted:
#         sorted2 = True
#         for i in range(0,n):
#             if arr[i] > arr[i+1]:
#                 sorted2 = False
#                 arr[i],arr[i+1]=arr[i+1],arr[i]
#     print("bubble sort")
#     return arr
# print(bubble_sort())

def selection_sort():
    arr = [4,1,-5,8,9,2]
    indexing_lenghth=range(0,len(arr)-1)
    for i in indexing_lenghth:
        min_value = i
        for k in range(i+1,len(arr)):
            if arr[k]<arr[min_value]:
                min_value=k
        if min_value!=i:
            arr[min_value],arr[i]=arr[i],arr[min_value]
    print("selection sort")
    return arr
print(selection_sort())