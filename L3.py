my_array1 = np.array(my_list1)
my_array1
#Our out is my_array1 = array([1,2,3,4,])
my_list2 = [11,22,33,44]
my_lists = [my_list1, my_list2]
my_array2 = np.array(my_lists)
my_array2
#Should give us an output like my_array2 = ([1,2,3,4], [11,22,33,44])
my_array2.shape
#Should give an output like (2L,4L)
