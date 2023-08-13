# convert the given list to dictionary using dictionary comprehension
student_list=[("name","john"),("age",25),("address","KTM")]
student=dict(student_list)
student_dict={key:value for key,value in student_list}
print(student_dict)