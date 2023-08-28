import json
filename='students.json'

def update_student(student_id):
    with open(filename,"r+") as fp:
        students=json.loads(fp.read())
        student=list(filter(lambda x:x['id']==student_id,students))
        if student:
            student=student[0]
            index=students.index(student)
            key=input("Ener info you want to update:")
            new_val=input("Enter the new value:")
            student[key]=new_val
            students[index]=student
            fp.seek(0)
            fp.write(json.dumps(students,indent=2))
        else:
            print("Invalid student Id")
    repeat=input("Do you want to continue? (y/n)")
    return True if repeat.lower()=='y' else False