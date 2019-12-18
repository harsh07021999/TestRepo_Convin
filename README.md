# TestRepo_Convin
Assingment sent for selection procedure of internship

the assingment was:-
In this assignment, you will be implementing the following two systems using Django 

1. Create a model having fields of type CharField and FileField. Implement a system on top of this model which should notify the updated/created field only and its old and new value. (it shouldn’t notify about the field which is not updated). It should also notify in case content of FileField is changed. [You may use signals or any other mechanism of your choice.] 

2. Now suppose CharField is the encrypted value of the content of FileFIeld (or you can choose any heavy computation of your choice on the content of File(it may be just along for loop)). Implement a system which allows updating FileField content by an external party (for example invoking management command from bash or calling a Django API or your choice of making it accessible by an external party). Note: after FileField content is changed, it should notify the updated value of FileField and CharField. 

This is a solution to above problem:
Due to time constraints i have not binded file upload with a form so you have to go into admin and upload the file .
encrypt is the charfield required in the question.
my_custom_command is the management command for updating the file field content which takes the name of the file as an argument and you have to paste that file you want to upate with in the media folder.
state_check1 show that the filefield is updated or created or not. 
