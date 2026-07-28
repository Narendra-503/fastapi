from fastapi import FastAPI,Body

app=FastAPI()
students = [
    {"name":"srihari","course":"DS","studentid":1},
    {"name":"srinu","course":"DA","studentid":2},
    {"name":"rajesh","course":"DS","studentid":3},
    {"name":"Srikanth","course":"DA","studentid":4}]
@app.get('/')
def home_page():
    return {"message":"welcome to fastAPI 552_B"}

@app.get('/add two_numbers')
def add(a:int,b:int):
    c=a+b
    return {"request":"GET","result":c}
@app.get('/get_all_students')
def view_all_students():
    return {"operation":"GET","result":students}

@app.get('/get_single_student_by_id/{studentid}')
def single_student(student_id:int):
    for i in students:
        if i['studentid']==student_id:
            return {"request":"GET","result":i}
    return {"message":"student id you are looking for is not available in the student list"}

@app.post('/add_student')
def add_single_student(addnewstudent=Body()):

    students.append(addnewstudent)
    return {"operation":"POST","student_details":students}

@app.put('/update_students_details_by_id/{studentid}')
def update_student(name:str,course:str,student_id:int):
    dict_={"name":name,"course":course,"studentid":student_id}
    for i in students:
        if i['studentid']==student_id:
            p = i.update(dict_)
            return {"request":"PUT","pervious details":i}
    return {"message":"student id you are looking for is not available in the student list"}

@app.delete('/delete_student_by_id/{studentid}')
def delete_student(studentid:int):
    for i in students:
        if i["studentid"]==studentid:
            students.remove(i)
            return {"operation": "DELETE","message": "Student deleted successfully","deleted_student": i}
    return {"message": "Student ID you are looking for is not available in the student list"}
