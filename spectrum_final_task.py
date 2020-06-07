import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
import mysql.connector as mysql


win = tk.Tk()
win.title('student login')
win.geometry('300x300+500+200')


name_label = ttk.Label(win, text='Enter user name',font="20").place(x=60,y=10)
name_var = tk.StringVar()
name_entrybox = ttk.Entry(win, width=16, textvariable = name_var).place(x=80,y=40)

password_label = ttk.Label(win, text='Enter password',font="20").place(x=60,y=80)




pass_var = tk.StringVar()
pass_entrybox = ttk.Entry(win, width=16, textvariable = pass_var).place(x=80,y=110)












def second_window():
   
    win_2 = tk.Toplevel()
    win_2.title('student details')
    win_2.geometry('600x400+500+100')
    name2_label = ttk.Label(win_2, text='Enter your name : ', font='10').place(x=10,y=50)
    name2_var = tk.StringVar()
    name2_entrybox = ttk.Entry(win_2, width=60, textvariable = name2_var).place(x=170,y=55)
    branch_label = ttk.Label(win_2, text='Enter your branch : ',font="20").place(x=10,y=100)
    branch_var = tk.StringVar()
    branch_entrybox = ttk.Entry(win_2, width=60, textvariable = branch_var).place(x=180,y=105)
    Id_label = ttk.Label(win_2, text='Enter your college id : ',font="20").place(x=10,y=150)
    Id_var = tk.StringVar()
    Id_entrybox = ttk.Entry(win_2, width=60, textvariable = Id_var).place(x=210,y=155)
 
      
    def insert1():

        name3 = name2_var.get()
        branch = branch_var.get()
        Id = Id_var.get()
        if(name3 == "" or branch == "" or Id == ""):
            m_box.showinfo('error','all fields are required')
        else: 
            win_3 = tk.Toplevel()
            win_3.title('subjects')
            win_3.geometry('600x400+500+100')
        
            subjects_label = ttk.Label(win_3, text='select your three subjects',font="20").place(x=60,y=10)

            checkbtn1 = ttk.Checkbutton(win_3, text='physics').place(x=10,y=50)
            checkbtn2 = ttk.Checkbutton(win_3, text='chemistry').place(x=160,y=50)
            checkbtn4 = ttk.Checkbutton(win_3, text='biology').place(x=310,y=50)

        def insert2():

        

            sub1_label = ttk.Label(win_3, text='enter the marks obtained in physics: ',font="10").place(x=10,y=110)
            sub1_var = tk.IntVar()
            sub1_entrybox = ttk.Entry(win_3, width=10, textvariable = sub1_var).place(x=340,y=115)


            sub2_label = ttk.Label(win_3, text='enter the marks obtained chemistry : ',font="10").place(x=10,y=210)
            sub2_var = tk.IntVar()
            sub2_entrybox = ttk.Entry(win_3, width=10, textvariable = sub2_var).place(x=340,y=215)

            sub3_label = ttk.Label(win_3, text='enter the marks obtained biology : ',font="10").place(x=10,y=310)
            sub3_var = tk.IntVar()
            sub3_entrybox = ttk.Entry(win_3, width=10, textvariable = sub3_var).place(x=320,y=315)
            
            

            def insert3():

                a = sub1_var.get()
                b = sub2_var.get()
                c = sub3_var.get()

                conn = mysql.connect(host='localhost',username='root',password='Saumesh@95',database='student_college_details')
                cursor = conn.cursor()
                cursor.execute("INSERT INTO students_details VALUE ('%s','%s','%s','%s','%s','%s')" % (name3,branch,Id,a, b, c))
            
        
            
        

                conn.commit()
                conn.close()


                win_4 = tk.Toplevel()
                win_4.title('grading')
                win_4.geometry('600x400+500+100') 

                physics = sub1_var.get()
                chemistry = sub2_var.get()
                biology = sub3_var.get()
                cgpa = ((physics+chemistry+biology)/3)/10
   
                def cgpa1():

                    CGPA_label = ttk.Label(win_4, text="Your C.G.P.A is : ",font="10").place(x=10,y=110)
                    CGPA_label2 = ttk.Label(win_4, text=cgpa,font="9").place(x=180,y=110)
                    return True
                
                def garde1():
                    if(9<=cgpa<=10):
                        grade = 'O'
                    elif(8<=cgpa<=9):
                        grade = 'E'
                    elif(7<=cgpa<=8):
                        grade = 'A'
                    elif(6<=cgpa<=7):
                        grade = 'B'
                    elif(5<=cgpa<=6):
                        grade = 'C'
                    elif(4<=cgpa<=5):
                        grade = 'D'
                    else:
                        grade = 'F'

                    grade_label = ttk.Label(win_4, text='your grade is :',font="10").place(x=10,y=210)
                    grade_label2 = ttk.Label(win_4, text=grade,font="10").place(x=150,y=210)
                    return True


                  

                def exit_screen():
                    win.destroy()
                    return True

                def next_window():
                    win_4.destroy()
                    win_3.destroy()
                    return True

                exit_button = tk.Button(win_4, text=' exit ',bg='grey',command=exit_screen).place(x=50,y=340)
                
                return_button = tk.Button(win_4, text='next entry',bg='grey',command=next_window).place(x=350,y=340)
                
                grade_button = tk.Button(win_4, text='Grade',bg='grey',command=garde1).place(x=180,y=30)

                cgpa_button = tk.Button(win_4, text='C.G.P.A',bg='grey',command=cgpa1).place(x=30,y=30)


                return True



            
            submit_button4 = tk.Button(win_3, text='calculate C.G.P.A',bg='grey',command=insert3).place(x=180,y=340)

                    


        submit_button3 = tk.Button(win_3, text='submit',bg='grey',command=insert2).place(x=180,y=75)
        
        return True
    
    
    submit_button2 = tk.Button(win_2, text='Submit',bg='grey',command=insert1).place(x=210,y=230)
    return True




            




def open_second_window():
    if(name_var.get() == 'saumesh' and pass_var.get() == 'sahoo'):
        second_window() 
    elif(name_var.get() == "" or pass_var.get() == ""):
        m_box.showerror('blank entry', 'please fill both boxes')
    elif(name_var.get() == "" and pass_var.get() == ""):
        m_box.showerror('blank entry', 'please fill both boxes')
    else:
        m_box.showerror('incorrect entry', 'your password or username is incorrect')











    
submit_button = tk.Button(win, text='Submit',bg='grey',command=open_second_window).place(x=110,y=150)




win.mainloop()