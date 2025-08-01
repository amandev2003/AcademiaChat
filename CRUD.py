import mysql.connector
import streamlit as st
mydb = mysql.connector.connect(
    host="localhost", user="root", password="Amanbondla2003.", database="chatbot"
)
mycursor = mydb.cursor()
print("connection succesfull")

st.title("CRUD Operations With MySQL")

# Display Options for CRUD Operations
option = st.sidebar.selectbox(
    "Select an Operation", ("Create", "Read", "Update", "Delete") 
)
# Perform Selected CRUD Operations
if option == "Create":
    st.subheader("Create a Record")
    CourseCode = st.text_input("Enter CourseCode")
    CourseName = st.text_input("Enter CourseName")
    FacultyName = st.text_input("Enter FacultyName")
    FacultyId = st.text_input("Enter FacultyId")
    Slot = st.text_input("Enter Slot")
    TotalSessions = st.text_input("Enter TotalSessions")
    FacultySessions = st.text_input("Enter FacultySessions")
    Present = st.text_input("Enter Present")
    PresentPercent = st.text_input("Enter PresentPercent")
    if st.button("Create"):
        sql = "insert into student(CourseCode, CourseName, FacultyName, FacultyId, Slot, TotalSessions,FacultySessions,Present,PresentPercent) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (
            CourseCode,
            CourseName,
            FacultyName,
            FacultyId,
            Slot,
            TotalSessions,
            FacultySessions,
            Present,
            PresentPercent,
        )
        mycursor.execute(sql, val)
        mydb.commit()
        st.success("Record Created Successfully!!!")


elif option == "Read":
    st.subheader("Read Records")
    mycursor.execute("select * from student")
    result = mycursor.fetchall()
    for row in result:
        st.write(row)
        


elif option == "Update":
    st.subheader("Update a Record")
    id = st.number_input("Enter ID", min_value=1)
    CourseCode = st.text_input("Enter CourseCode")
    CourseName = st.text_input("Enter CourseName")
    FacultyName = st.text_input("Enter FacultyName")
    FacultyId = st.text_input("Enter FacultyId")
    Slot = st.text_input("Enter Slot")
    TotalSessions = st.text_input("Enter TotalSessions")
    FacultySessions = st.text_input("Enter FacultySessions")
    Present = st.text_input("Enter Present")
    PresentPercent = st.text_input("Enter PresentPercent")
    if st.button("Update"):
        sql = "insert into student(CourseCode, CourseName, FacultyName, FacultyId, Slot, TotalSessions,FacultySessions,Present,PresentPercent) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (
            CourseCode,
            CourseName,
            FacultyName,
            FacultyId,
            Slot,
            TotalSessions,
            FacultySessions,
            Present,
            PresentPercent,
        )
        mycursor.execute(sql, val)
        mydb.commit()
        st.success("Record Updated Successfully!!!")


elif option == "Delete":
    st.subheader("Delete a Record")
    id = st.number_input("Enter ID", min_value=1)
    if st.button("Delete"):
        sql = "delete from student where id =%s"
        val = (id,)
        mycursor.execute(sql, val)
        mydb.commit()
        st.success("Record Deleted Successfully!!!")
