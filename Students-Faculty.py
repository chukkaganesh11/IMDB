import csv
f1=open(r"/mnt/d/GenAi/students_data.csv",mode='r')
data2=csv.reader(f1)
new_list=[]
for info in data2:
    new_list.append(info)
f1.close()
#print(new_list)

for i in new_list:
    if i[1].lower()=="mathematics":
        print(i)

student_physics_data=[]

for i in new_list:
    if i[1].lower()=="physics":
        student_physics_data.append([i[0],i[2]])
print(student_physics_data)

# 1.Find the faculty with highest student count who got more than 90%
faculty_file=open(r"/mnt/d/GenAi/faculties_data.csv",mode='r')
student_file=open(r"/mnt/d/GenAi/students_data.csv",mode='r')
faculty_data=csv.reader(faculty_file)
new_faculty_list=[]
for info2 in faculty_data:
    new_faculty_list.append(info2)

student_data=csv.reader(student_file)
top_faculty=[]
maths=0
physics=0
chemistry=0
social=0
english=0
telugu=0
for i in new_list:
    if i[2]>"90":
        sub=i[1]
        if sub.lower() == "Mathematics":
            maths+=1
        elif sub.lower()== "Telugu":
            telugu+=1
        elif sub.lower()=="Physics":
            physics+=1
        elif sub.lower()=="social":
            social+=1
        elif sub.lower()=="chemistry":
            chemistry+=1
        elif sub.lower()=="english":
            english+=1

max_count_data={"maths":maths,
                    "physics":physics,
                    "chemistry":chemistry,
                    "telugu":telugu,
                    "english":english,
                    "social":social
                    }
# max_count=max([maths,physics,chemistry,telugu,english,social])
# max_count=max(max_count_data.values())
max_subject=max(max_count_data,key=max_count_data.get)
# print(max_subject)

# print(new_faculty_list)
for top_faculty in new_faculty_list:
    if top_faculty[0].lower()==max_subject:
        print(top_faculty[1])


# 4.
students=[]
for s in new_list:
    if s[0] not in students:
        students.append(s[0])
# print(students)

students_marks_list=[]
for sl in students:
    total_marks_sum=0
    for s in new_list:
        if s[0]==sl:
            total_marks_sum+=int(s[2])
    students_marks_list.append([sl,total_marks_sum])

# print(students_marks_list)
topper=max(students_marks_list,key=lambda x:x[1])
print(topper)

# 7.Find the student with least numbers of marks as total.
min_student=min(students_marks_list,key=lambda x:x[1])
print(min_student)


# 2.3.
maths_marks=0
telugu_marks=0
physics_marks=0
social_marks=0
chemistry_marks=0
english_marks=0
for i in new_list:
    # if i[2]>"40":
        sub=i[1]
        if sub.lower() == "mathematics":
            maths_marks+=int(i[2])
            maths+=1
        elif sub.lower()== "telugu":
            telugu_marks+=int(i[2])
            telugu+=1
        elif sub.lower()=="physics":
            physics_marks+=int(i[2])
            physics+=1
        elif sub.lower()=="social":
            social_marks+=int(i[2])
            social+=1
        elif sub.lower()=="chemistry":
            chemistry_marks+=int(i[2])
            chemistry+=1
        elif sub.lower()=="english":
            english_marks+=int(i[2])
            english+=1
maths_avg=maths_marks//maths
telugu_avg=telugu_marks//telugu
chemistry_avg=chemistry_marks//chemistry
social_avg=social_marks//social
english_avg=english_marks//english
physics_avg=physics_marks//physics

# 6.What is the average mark for each subject, (ignore failures)?
sub_avg_marks=[maths_avg,telugu_avg,chemistry_avg,english_avg,social_avg,physics_avg]
fac_highest_pass_percetage=[]
fac_highest_pass_percetage2=[]
for m in sub_avg_marks:
    if m>40:
        fac_highest_pass_percetage.append(m)
    elif m<=40:
        fac_highest_pass_percetage2.append(m)
print(fac_highest_pass_percetage)


# 5.Who is the best student in Mathematics?
result=[[data[0], int(data[2])] for data in new_list if data[1].lower()=="mathematics"]
print(max(result, key=lambda x: x[1]))
