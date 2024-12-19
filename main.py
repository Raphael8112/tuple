#creating a tuple
my_tuple=(1,2,3,4)
print(my_tuple)
#create a tuple with mixed data types
my_tuple=(1,"hello",3.4)
print(my_tuple)
#nest a tuple-add a tuple to another data structure eg list
my_tuple=("mouse",[6,4,5,6],(1,2,3,4))#list another tuple
print(my_tuple)
#access the elements in a tuple
my_tuple=("c","o","t","s","g","l")
print(my_tuple[5])
print(my_tuple[1])
#slicing a tuple
my_tuple=(1,2,3,4,5,6,7)
print("Slice tuple is :", my_tuple[1:4])
#iterate a tuple
my_tuple=("h","e","l","l","o")
for letter in (my_tuple):
      print("The letter is:", letter)
