from datetime import datetime, time, date, timedelta

from time import sleep
from time import *  # meaning from time import EVERYTHING
import time
from flask import Flask, render_template, session, redirect, request, url_for
import hashlib
from array import *

from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'the random string'
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "clg_prject"
mysql = MySQL(app)


# ----teacher u & p -------#
@app.route("/")
def home():
    return render_template('login.html')


@app.route("/teacherup", methods=['GET', 'POST'])
def teacherup():
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        print(password)
        hashpwd = hashlib.md5(password.encode())
        print(hashpwd.hexdigest())
        cur = mysql.connection.cursor()
        cur.execute("select * from user where username='" + username + "' and password='" + hashpwd.hexdigest() + "'")
        # r=cur.fetchall()
        account = cur.fetchone();
        print(account)

        count = cur.rowcount
        print(count)

        if count == 1:
            # if username == request.form['username'] and password == request.form['password']:
            print(account[0])
            session["id"] = account[0]
            session['username'] = account[1]
            msg = 'Logged in successfully !'
            return render_template('teachers_dashboard.html', msg=msg)
        else:
            msg = "Invalid Credentials";
            return render_template('login.html', msg=msg)

        mysql.connection.commit()
        cur.close()

    return render_template('login.html')


# ===admindashboard


@app.route("/admindashboard")
def admindashboard():
    # if not session.get('collegeid') or session.get('userid'):
    #     return redirect('/login')
    cur = mysql.connection.cursor()

    cur.execute("SELECT COUNT(deptid) FROM department ")
    dept_msg = cur.fetchall()

    print(dept_msg)
    cur.execute("SELECT COUNT(Teacher_id) FROM teacher ")
    teach_msg = cur.fetchall()
    print(teach_msg)
    mysql.connection.commit()
    cur.close()

    return render_template('admin_dashboard.html', msg=dept_msg, msg1=teach_msg)


# ----admin u & p -------#

@app.route("/adminup", methods=['GET', 'POST'])
def adminup():
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        print(password)
        hashpwd = hashlib.md5(password.encode())
        print(hashpwd.hexdigest())
        cur = mysql.connection.cursor()
        cur.execute(
            "select * from admin_up where username='" + username + "' and password='" + hashpwd.hexdigest() + "'")
        # r=cur.fetchall()
        account = cur.fetchone();
        print(account)

        count = cur.rowcount
        print(count)

        if count == 1:
            # if username == request.form['username'] and password == request.form['password']:
            print(account[0])
            session["collegeid"] = account[0]
            session['username'] = account[1]

            return redirect('/admindashboard')
        else:

            return render_template('login.html')

        mysql.connection.commit()
        cur.close()

    return render_template('login.html')


# ----student u & p -------#


@app.route("/studentup", methods=['GET', 'POST'])
def studentup():
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        print(password)
        hashpwd = hashlib.md5(password.encode())
        print(hashpwd.hexdigest())
        cur = mysql.connection.cursor()
        cur.execute(
            "select * from student where Username='" + username + "' and Password='" + hashpwd.hexdigest() + "'")
        # r=cur.fetchall()
        account = cur.fetchone();
        print(account)

        count = cur.rowcount
        print(count)

        if count == 1:
            # if username == request.form['username'] and password == request.form['password']:
            print(account[0])
            p = session["userid"] = account[0]
            print(p)
            session["collegeid"] = account[13]
            f = session['username'] = account[1]
            b = session['class'] = account[6]
            u = session['dept'] = account[14]
            print(u)
            print(b)
            print(f)
            msg = 'Logged in successfully !'
            return render_template('students_dashboard.html', msg=msg)
        else:
            msg = "Invalid Credentials";
            return render_template('login.html', msg=msg)

        mysql.connection.commit()
        cur.close()

    return render_template('students_dashboard.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/addteacherp")
def addteacherp():
    return render_template('add_teacher.html')


@app.route("/stream", methods=['GET', 'POST'])
def stream():
    if request.method == 'POST':
        d_name = request.form['DeptName']
        collegeid = session["collegeid"]

        cur = mysql.connection.cursor()

        cur.execute("insert into department (DeptName,CollegeId) " "VALUES (%s,%s)", (d_name, collegeid))

        mysql.connection.commit()
        cur.close()

        return redirect('/streamlist')
    else:

        return render_template('stream.html')


# ===
@app.route("/streamlist", methods=['GET', 'POST'])
def streamlist():
    cur = mysql.connection.cursor()
    clgid = str(session["collegeid"])
    cur.execute("select * from department Where Collegeid='" + clgid + "'")
    alldata = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template('stream.html', streamList=alldata)


@app.route("/class", methods=['GET', 'POST'])
def classs():
    if request.method == 'POST':
        clsname = request.form['name']
        teach = request.form['teacher']
        strm = request.form['stream']
        collegeid = session["collegeid"]

        cur = mysql.connection.cursor()

        cur.execute("insert into class (classname,teacher,stream,CollegeId) " "VALUES (%s,%s,%s,%s)",
                    (clsname, teach, strm, collegeid))
        print("insert into class (classname,teacher,stream,CollegeId) " "VALUES (%s,%s,%s,%s)",
              (clsname, teach, strm, collegeid))
        mysql.connection.commit()
        cur.close()

        return redirect('/classlist')
    else:

        return render_template('/classlist')


# ===
@app.route("/classlist", methods=['GET', 'POST'])
def clslist():
    cur = mysql.connection.cursor()
    clgid = str(session["collegeid"])
    cur.execute("select * from class Where Collegeid='" + clgid + "'")
    alldata = cur.fetchall()

    cur.execute("select * from teacher Where Collegeid='" + clgid + "'")
    teach = cur.fetchall()

    cur.execute("select * from department Where Collegeid='" + clgid + "'")
    strm = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template('class.html', classlist=alldata, teacher=teach, stream=strm)


# -----  {{ url_for('subjectsubject') }}-----
@app.route("/subject", methods=['GET', 'POST'])
def subject():
    if request.method == 'POST':
        s_name = request.form['subjectname']
        S_code = request.form['subjectcode']
        teach = request.form['teach']
        collegeid = session["collegeid"]
        list = teach.split(',')
        cur = mysql.connection.cursor()
        print(list)
        cur.execute("insert into subject (SubName,SubCode,teacher,Teacherid,CollegeId) " "VALUES (%s,%s,%s,%s,%s)",
                    (s_name, S_code, list[0], list[1], collegeid))

        mysql.connection.commit()
        cur.close()

        return redirect('/subjectlist')
    else:

        return render_template('subject.html')


# ===
@app.route("/subjectlist", methods=['GET', 'POST'])
def subjectlist():
    cur = mysql.connection.cursor()
    clgid = str(session["collegeid"])
    cur.execute("select * from subject where CollegeId='" + clgid + "'")

    alldata = cur.fetchall()

    cur.execute("select * from teacher where CollegeId='" + clgid + "'")
    teacher = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template('subject.html', subjectlist=alldata, teacher=teacher)


@app.route("/addteacha", methods=['GET', 'POST'])
def addteacher():
    if request.method == 'POST':
        T_name = request.form['T_name']
        username = request.form['username']
        password = request.form['password']
        address = request.form['address']
        Qualification = request.form['Qualification']
        contact = request.form['contact']
        email = request.form['email']
        user_role = request.form['user_role']
        collegeid = session["collegeid"]
        cur = mysql.connection.cursor()

        cur.execute(
            "insert into teacher (T_name,Username,Password,Address,Qualification,T_Contact,Email,User_Role,CollegeId) "
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (T_name, username, password, address, Qualification, contact, email, user_role, collegeid))
        mysql.connection.commit()
        cur.close()
        msg = 'Teacher is added successfully in list !'
        return render_template('add_teacher.html', msg=msg)


# ------->studentDetails------>


@app.route('/studentdetails', methods=['GET', 'POST'])
def studentdetails():
    if request.method == 'POST':
        Stud_name = request.form['stud_name']
        Stud_contact = request.form['contact']
        Stude_email = request.form['email']
        parent_name = request.form['parentname']
        parent_contact = request.form['parentcontact']
        classd = request.form['class']
        Address = request.form['address']
        profile_img = request.form['profile_img']
        username = request.form['username']
        password = request.form['password']
        department = request.form['deptname']
        collegeid = str(session["collegeid"])
        cur = mysql.connection.cursor()
        password = hashlib.md5(password.encode())
        cur.execute(
            "insert into student (Stud_Name,Stud_Contact,Stud_email,Parent_name,Parent_contact,class,Address,Profile_Img,Username,Password,CollegeId,Deptname) "
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (Stud_name, Stud_contact, Stude_email, parent_name, parent_contact, classd, Address, profile_img, username,
             password.hexdigest(), collegeid, department))
        mysql.connection.commit()
        cur.close()
        msg = 'student is added successfully in list !'
        return render_template('studentlist.html', msg=msg)
    else:
        collegeid = str(session["collegeid"])
        cur = mysql.connection.cursor()
        query = "Select * from class where CollegeId='" + collegeid + "'"
        cur.execute(query)
        clsdata = cur.fetchall()
        query = "Select * from department where CollegeId='" + collegeid + "'"
        cur.execute(query)
        strm = cur.fetchall()
        return render_template('student.html', clsdata=clsdata, stram=strm)


@app.route('/studentlist')
def studentList():
    cur = mysql.connection.cursor()
    clgid = str(session["collegeid"])
    cur.execute("select * from student where CollegeId='" + clgid + "'")

    alldata = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template('studentlist.html', studentlist=alldata)


@app.route('/exampage')
def exampage():
    return render_template('exampage.html')


@app.route('/savemcq', methods=['GET', 'POST'])
def setpaper():
    if request.method == 'POST':
        paper_name = request.form['examname']
        subcode = request.form['cod']
        print(subcode);
        subject = request.form['subjnm']
        class1 = request.form['class_type']
        noofquest = request.form['noofquesth']
        ttlmarks = request.form['marks']
        questtype = request.form['quest_type']
        print(questtype);
        qp = request.form.getlist('question_1')
        option1 = request.form.getlist('option1')
        option2 = request.form.getlist('option2')
        option3 = request.form.getlist('option3')
        option4 = request.form.getlist('option4')
        rigtans = request.form.getlist('rightansc')
        print(rigtans);
        collegeid = session["collegeid"]

        cur = mysql.connection.cursor()

        cur.execute(
            "insert into papers (Paper_set_name,Qp_code,subject,No_of_questions,Question_type,Class,CollegeId) "
            "VALUES (%s,%s,%s,%s ,%s,%s,%s)",
            (paper_name, subcode, subject, noofquest, questtype, class1, collegeid))
        print(collegeid);

        n = len(qp)

        for x in range(n):
            quest = qp[x];
            op1 = option1[x];
            op2 = option2[x];
            op3 = option3[x];
            op4 = option4[x];
            ritans = rigtans[x];
            cur.execute(
                "insert into question_paper (Paper_set_name,Qp_code,subject,Class,No_of_questions,Total_marks,Question_type,Question,Option1,Option2,Option3,Option4,Right_answer,CollegeId) "
                "VALUES (%s,%s,%s,%s ,%s,%s,%s,%s ,%s,%s,%s,%s ,%s,%s)",
                (
                    paper_name, subcode, subject, class1, noofquest, ttlmarks, questtype, quest, op1, op2, op3, op4,
                    ritans,
                    collegeid))

        mysql.connection.commit()
        cur.close()
        return redirect('/dumylist')
    else:
        clgid = str(session["collegeid"])
        cur = mysql.connection.cursor()
        query = "select * from class where Collegeid='" + clgid + "'"
        cur.execute(query)
        clsdata = cur.fetchall()
        query1 = "select * from subject where Collegeid='" + clgid + "'"
        cur.execute(query1)
        subj = cur.fetchall()
    return render_template('setpaper.html', clsdata=clsdata, subj=subj)


@app.route('/examlist')
def examlist():
    if request.method == 'POST':
        code = request.form['cod']
        clas = request.form['class_type']
        print(code);
        cur = mysql.connection.cursor()
        p = cur.execute("select * from papers where Paper_set_name='" + code + "' and Class='" + clas + "'")
        print(p);
        alldata = cur.fetchall()
        print(alldata);
        mysql.connection.commit()
        cur.close()
        return redirect(url_for("dumylist", examlist=alldata))
    else:
        clgid = str(session['collegeid'])
        cur = mysql.connection.cursor()
        p = cur.execute("select * from papers where CollegeId='" + clgid + "'")
        print(p);
        alldata = cur.fetchall()
        print(alldata);
        mysql.connection.commit()
        cur.close()
    return render_template('dumy.html', examlist=alldata)


@app.route('/dumy', methods=['GET', 'POST'])
def dumy():
    result = "";
    collegeid = session['collegeid']
    cur = mysql.connection.cursor()
    p = cur.execute("select * from papers where CollegeId='" + collegeid + "'")
    print(p);
    alldata = cur.fetchall()

    print(alldata);
    mysql.connection.commit()
    cur.close()

    return render_template('dumy.html', alldata=alldata)


@app.route('/dumylist', methods=['GET', 'POST'])
def dumylist():
    if request.method == 'POST':
        code = request.form['cod']
        clas = request.form['class_type']
        print(code);
        cur = mysql.connection.cursor()
        p = cur.execute("select * from papers where Paper_set_name='" + code + "' and Class='" + clas + "'")
        print(p);
        alldata = cur.fetchall()
        print(alldata);
        mysql.connection.commit()

        return render_template('dumy.html', alldata=alldata)
    else:
        clgid = str(session['collegeid'])
        cur = mysql.connection.cursor()
        p = cur.execute("select * from papers where CollegeId='" + clgid + "'")
        print(p);
        alldata = cur.fetchall()
        print(alldata);
        mysql.connection.commit()
        cur.close()
    return render_template('dumy.html', alldata=alldata)


@app.route('/GetAllPapers', methods=['GET', 'POST'])
def dumyl():
    if request.method == 'POST':
        subcode = request.form['cod']
        class1 = request.form['class_type']
        cur = mysql.connection.cursor()
        p = cur.execute("select * from question_paper where Qpcode='" + subcode + "' and Class='" + class1 + "'")
        print(p);
        alldata = cur.fetchall()
        print(alldata);
        mysql.connection.commit()
        cur.close()
    return alldata


@app.route('/viewpaper/<string:qpcode>')
def viewspaper(qpcode):
    cur = mysql.connection.cursor()
    print(qpcode);
    p = cur.execute(
        "select Question,Option1,Option2,Option3,Option4,Total_marks from question_paper where Qp_code='" + qpcode + "'")
    print(
        "select Question,Option1,Option2,Option3,Option4,Total_marks from question_paper where Qp_code='" + qpcode + "'");
    alldata = cur.fetchall()
    print(alldata);
    mysql.connection.commit()
    cur.close()
    return render_template('viewpaper.html', alldata=alldata)


@app.route('/addexam1', methods=['GET', 'POST'])
def addexam1():
    if request.method == 'POST':
        QPLIST = request.form['qplist']
        class1 = request.form['class_type']

        datee = request.form['date']
        print(datee);
        # datetime.strftime(date, '%Y-%m-%d %H:%M:%S')
        # # print(date);
        # start_time = datetime.time(request.form['start_tim'])
        examnm = request.form['examname']
        descriptn = request.form['exam_descriptn']
        subjectnm = request.form['subject']
        DEPT = request.form['dept']
        start_time = request.form['start_tim']
        print(start_time);
        end_time = request.form['end_tim']
        print(end_time);
        clgid = str(session['collegeid'])
        ststart = datee + " " + start_time
        edend = datee + " " + end_time

        # print(ststart)
        # print(edend)
        cur = mysql.connection.cursor()
        p = cur.execute(
            "insert into exam_list (Exame_name,exam_descrp,Class,DeptName,Exam_date,Exam_start_time,Exam_end_time,"
            "subject,Qp_code,CollegeId)" "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (examnm, descriptn, class1, DEPT, datee, start_time, end_time, subjectnm, QPLIST, clgid))
        print("insert into exam_list (Exame_name,exam_descrp,Class,Exam_date,Exam_start_time,Exam_end_time,"
              "subject,Qp_code,CollegeId)" "values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
              (examnm, descriptn, class1, datee, start_time, end_time, subjectnm, QPLIST, clgid));

        FMT = '%H:%M:%S'
        global tdelta;
        global tdelta1;
        global tdelta2;
        tdelta = diff_times_in_seconds(datetime.strptime(start_time, '%H:%M:%S').time(),
                                       datetime.strptime(end_time, '%H:%M:%S').time())
        print(tdelta);
        tdelta1 = diff_times_in_hours(datetime.strptime(start_time, '%H:%M:%S').time(),
                                      datetime.strptime(end_time, '%H:%M:%S').time())
        print(tdelta1);

        tdelta2 = diff_times_in_minutes(datetime.strptime(start_time, '%H:%M:%S').time(),
                                        datetime.strptime(end_time, '%H:%M:%S').time())
        print(tdelta2);
        print("Time left", tdelta1, ":", tdelta2)

        data = cur.fetchall()

        mysql.connection.commit()
        cur.close()
        return redirect('/examdonelist')

    else:
        cur = mysql.connection.cursor()
        clgid = str(session["collegeid"])
        p = cur.execute("select Qp_code from papers where Collegeid='" + clgid + "'")
        data = cur.fetchall()
        cur.execute("select * from class where Collegeid='" + clgid + "'")
        clsdata = cur.fetchall()
        cur.execute("select * from subject where Collegeid='" + clgid + "'")
        subj = cur.fetchall()
        cur.execute("select * from department where Collegeid='" + clgid + "'")
        dept = cur.fetchall()
        mysql.connection.commit()
        cur.close()
        return render_template('addexam.html', data=data, clsdata=clsdata, subj=subj, dept=dept)
    return render_template('addexam.html')


@app.route('/taskboard')
def taskboard():
    return render_template('taskboard.html')


@app.route('/layout_student')
def layout_student():
    return render_template('layout_teacher.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


@app.route('/exam_scgedule_list')
def exam_sched():
    classs = str(session['class'])
    dept = str(session['dept'])
    print(classs)
    cur = mysql.connection.cursor()
    p = cur.execute(
        "select * from exam_list where Class='" + classs + "' and DeptName='" + dept + "' and Exam_date=cast(now() as date)")
    print(p)
    alldata = cur.fetchall()
    print(alldata)
    mysql.connection.commit()
    cur.close()
    return render_template('Exam_Schedule_List.html', examList=alldata)


@app.route('/givenexams', methods=['GET', 'POST'])
def givenexams():
    cur = mysql.connection.cursor()
    data = "No Details"
    count = 0
    attempt = 0
    subject = ""
    exmname = ""
    qpcode = ""

    studid = str(session["userid"])
    clgid = str(session["collegeid"])
    dept = str(session["dept"])
    cls = str(session["class"])
    marks = 0
    query1 = "select * from exam_list Where Class='" + cls + "' and DeptName='" + dept + "' and CollegeId='" + clgid + "'"
    cur.execute(query1)
    qpaper = cur.fetchall()
    print(query1)
    try:
        for row in qpaper:
            count = count + 1
            exmname = row[1]
            subject = row[9]
            qpcode = row[10]
            query = "select count(right_answer),sum(marks_obtained) from answer Where createdon < cast(now() as datetime) and stud_id='" + studid + "' and QP_code='" + qpcode + "' and CollegeId='" + clgid + "'"
            cur.execute(query)
            print(query)
            answer = cur.fetchone()
            print(answer)
            if answer is not None:
                attempt = answer[0]
                marks = answer[1]

            data = data + "<tr><td>" + str(
                count) + "</td><td>" + exmname + "</td>td>" + subject + "</td>td>" + attempt + "</td>"
            print(data)
            if row[6] == 0:
                data = data + "<td>Result Not Yet Published</td>"
            else:
                data = data + "<td>" + marks + "</td>"
            data = data + "</tr>"
        return render_template('givenexams.html', data=data)
    except:
        return render_template('givenexams.html', data=data)
    return render_template('givenexams.html', data=data)


@app.route('/teacherList')
def teacherList():
    cur = mysql.connection.cursor()
    clgid = str(session["collegeid"])
    cur.execute("select * from teacher Where CollegeId='" + clgid + "'")
    alldata = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template('teacherlist.html', teacherList=alldata)


@app.route('/exam')
def exam():
    cur = mysql.connection.cursor()
    cur.execute(
        "SELECT * FROM `exam_list` WHERE Exam_end_time>cast(now() as time) and Exam_date = cast(now() as date)")
    allexams = cur.fetchall()
    studid = session["userid"]
    diff = 0
    start = 0
    start = cur.fetchone()
    condition = cur.execute(
        "SELECT * FROM `exam_list` WHERE Exam_start_time<=cast(now() as time) and Exam_end_time>=cast(now() as time) and Exam_date <= cast(now() as date) ")

    today = datetime.now().strftime('%H:%M')
    if start is not None:
        diff = diff_times_in_seconds(datetime.strptime(today, '%H:%M').time(), datetime.strptime(start, '%H:%M').time())

    context = {
        'diffinsec': diff,
        'allexams': allexams,
        'today': today,
        'condition': condition
    }
    print(context)
    return render_template('start_exam.html', context=context)


@app.route('/examps')
def examps():
    print(tdelta);

    return render_template('exam.html')


@app.route('/questionpaper/<string:qpcode>')
def startexam(qpcode):
    cur = mysql.connection.cursor()
    print(qpcode);

    cur.execute(
        "Select cast(Exam_date as date),cast(Exam_end_time as time) from exam_list where QP_code='" + qpcode + "'")
    timdata = cur.fetchone()
    time1 = timdata[1]
    date1 = timdata[0]
    print(timdata)
    print(time1)
    studid = str(session["userid"])
    p = cur.execute(
        "select Question,Option1,Option2,Option3,Option4,Total_marks,Qp_id,Qp_code from question_paper where Qp_code='" + qpcode + "'")
    print(
        "select Question,Option1,Option2,Option3,Option4,Total_marks,Qp_id,Qp_code from question_paper where Qp_code='" + qpcode + "'");
    alldata = cur.fetchall()

    cur.execute(
        "SELECT * FROM `answer` WHERE stud_id='" + studid + "' and Qp_code='" + qpcode + "'")
    checkexam = cur.fetchone()
    print(checkexam)
    mysql.connection.commit()
    cur.close()
    if checkexam is not None:
        return redirect('/givenexams')
    return render_template('student_paper.html', alldata=alldata, context=date1, time1=time1)


# https://stackoverflow.com/questions/62428081/compare-datetime-mysql-and-flask
# https://stackoverflow.com/questions/15537254/passing-data-from-javascript-into-flask
# https://www.google.com/search?q=enable+button+on+certain+time+in+flask&rlz=1C1CHBD_enIN947IN947&oq=enable+button+on+certain+time+in+flsk&aqs=chrome.1.69i57j33i10i160.40199j0j7&sourceid=chrome&ie=UTF-8


@app.route('/papersubmit', methods=['GET', 'POST'])
def papersub():
    if request.method == 'POST':
        qpcode = request.form['QpCode']
        examname = request.form['Examname']
        classs = request.form['class']
        qpid = request.form.getlist('Question')
        studname = session["username"];
        studid = session["userid"];
        print("code ", qpcode)
        collegeid = session["collegeid"]
        ans = ""
        n = len(qpid)
        print("length ", n)
        try:
            for x in range(n):
                value = "radio_" + str(qpid[x])
                ans = request.form[value]
                print(ans)

                if ans is None:
                    qattempt = 0
                    print(x, "not inserted")
                else:
                    questid = qpid[x]
                    cur = mysql.connection.cursor()
                    print(x + 1, " ", ans)
                    cur.execute(
                        "select * from question_paper Where Qp_id='" + questid + "'")
                    qpdata = cur.fetchone()
                    qattempt = 1
                    mark = qpdata[6]
                    status = 0
                    right = qpdata[13]
                    if ans == right:
                        status = 1
                    else:
                        status = 0
                        mark = 0

                print(x, "Inserted")
                cur.execute(
                    "insert into answer (Qp_code,student_name,stud_id,Question_id,selected_answer,right_answer,"
                    "Quest_attempted,status,marks_obtained,CollegeId,Class,Exam_name) "
                    "VALUES (%s,%s,%s,%s ,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                    qpcode, studname, studid, questid, ans, right, qattempt, status, mark, collegeid, classs, examname))
                print(
                    "insert into answer (Qp_code,student_name,stud_id,Question_id,selected_answer,right_answer,"
                    "Quest_attempted,status,marks_obtained,CollegeId) "
                    "VALUES (%s,%s,%s,%s ,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (qpcode, studname, studid, questid, ans, right, qattempt, status, mark, collegeid))
                mysql.connection.commit()
                cur.close()
        except:
            return redirect('/givenexams')

    return redirect('/givenexams')


@app.route('/examdonelist')
def examoverlist():
    # if request.method == 'POST':
    # code = request.form['cod']
    # clas = request.form['class_type']
    # print(code);
    cur = mysql.connection.cursor()
    clgid = str(session["collegeid"])
    p = cur.execute("SELECT * FROM `exam_list`where CollegeId='" + clgid + "'")
    alldata = cur.fetchall()

    print(alldata);
    mysql.connection.commit()
    cur.close()
    return render_template('exam_over_list.html', examlist=alldata)
    # else:
    #     clgid = str(session['collegeid'])
    #     cur = mysql.connection.cursor()
    #     p = cur.execute("select * from examlist")
    #     print(p);
    #     alldata = cur.fetchall()
    #     print(alldata);
    #     mysql.connection.commit()
    #     cur.close()
    # return render_template('exam_over_list.html', examlist=alldata)


@app.route('/examresult/<string:qpcode>')
def examresult(qpcode):
    cur = mysql.connection.cursor()
    clgid = str(session["collegeid"])
    totquest = "0"
    marks = "0"
    perc = "0"
    data="<tr></tr>"
    name = "No Details"
    classs = "No Details"
    subj = "No Details"
    status = "<span class='badge badge-danger'>Pending</span>"
    cur.execute("select * from student Where  CollegeId='" + clgid + "'")
    students = cur.fetchall()
    count = 1
    n = len(students)
    for row in students:
        studid = str(row[0])
        name = str(row[1])
        count = count + 1
        cur.execute(
            "select sum(marks_obtained),count(marks_obtained) from answer Where stud_id='" + studid + "'and CollegeId='" + clgid + "' and Qp_code='" + qpcode + "'")
        answer = cur.fetchone()
        print(
            "select sum(marks_obtained),count(marks_obtained) from answer Where stud_id='" + studid + "'and CollegeId='" + clgid + "' and Qp_code='" + qpcode + "'")
        print(name)
        if answer[0] is not None:
            status = "<span class='badge badge-info'>Paper Submitted</span>"
            totquest = str(answer[1])
            marks = answer[0]
            cur.execute(
                "select No_of_questions,subject,class,sum(Total_marks) from question_paper Where  CollegeId='" + clgid + "' and  Qp_code='" + qpcode + "'")
            questiom = cur.fetchone()
            print(questiom)
            perc = str((marks / int(questiom[3])) * 100)
            print(perc)
            marks = str(answer[0])
            subj = str(questiom[1])
            classs = str(questiom[2])
        data = data+"<tr><td>" + str(count) + "</td><td>" + name + "</td><td>" + subj + "</td><td>" + classs + "</td><td>" + totquest + "</td><td>" + marks + "</td>"
        data = data + "<td><strong>" + perc + "</strong></td>><td>" + status + "</td><td><a class='btn btn-square btn-info' type='button' href='/viewcorrectanswer?stud=" + studid + "&qpcode=" + qpcode + "' data-original-title='Click Here to View Paper' title="">View Paper</a></td></tr>"

    return render_template('examresults.html', data=data)


@app.route('/viewcorrectanswer')
def viewcorrectanswer():
    stud = request.args.get("stud", None)
    qpcode = request.args.get("qpcode", None)
    count = 0
    name=""
    cur = mysql.connection.cursor()
    print(qpcode)
    data = ""
    cur.execute("select * from question_paper Where  Qp_code='" + qpcode + "'")
    question = cur.fetchall()

    n = len(question)
    for qrow in question:
        count = count + 1

        qid = str(qrow[0])
        optiona = str(qrow[9])
        optionb = str(qrow[10])
        optionc = str(qrow[11])
        optiond = str(qrow[12])
        right = "No Details"
        selected = "No Details"
        status = "No Details"
        qry="select * from answer Where Question_id='" + qid + "' and stud_id='" + stud + "' and Qp_code='" + qpcode + "'"
        cur.execute(qry)
        answer = cur.fetchone()
        print(qry)
        qname = str(qrow[8])

        if answer is not None:
            name=answer[2]
            if answer[6] == "A":
                right = "<span class='badge badge-success'>" + optiona + "</span>"
            elif answer[6] == "B":
                right = "<span class='badge badge-success'>" + optionb + "</span>"
            elif answer[6] == "C":
                right = "<span class='badge badge-success'>" + optionc + "</span>"
            elif answer[6] == "D":
                right = "<span class='badge badge-success'>" + optiond + "</span>"

            if answer[5] == "A":
                selected = "<span class='badge badge-info'>" + optiona + "</span>"
            elif answer[5] == "B":
                selected = "<span class='badge badge-info'>" + optionb + "</span>"
            elif answer[5] == "C":
                selected = "<span class='badge badge-info'>" + optionc + "</span>"
            elif answer[5] == "D":
                selected = "<span class='badge badge-info'>" + optiond + "</span>"

            if str(answer[5]) == str(answer[6]):
                status = "<span class='badge badge-success'>Correct Answer</span>"
            else:
                status = "<span class='badge badge-danger'>Wrong Answer</span>"

        data = data + "<tr><td>" + str(
            count) + "</td><td>" + qname + "</td><td>" + right + "</td><td>" + selected + "</td><td>" + status + "</td></tr>"

    return render_template('view_correct_ans.html', data=data,name=name)


# https://www.codegrepper.com/code-examples/javascript/disable+submit+button+flask+condition
def diff_times_in_seconds(t1, t2):
    # caveat emptor - assumes t1 & t2 are python times, on the same day and t2 is after t1
    h1, m1, s1 = t1.hour, t1.minute, t1.second
    h2, m2, s2 = t2.hour, t2.minute, t2.second
    t1_secs = s1 + 60 * (m1 + 60 * h1)
    t2_secs = s2 + 60 * (m2 + 60 * h2)
    return (t2_secs - t1_secs)


def diff_times_in_hours(t1, t2):
    # caveat emptor - assumes t1 & t2 are python times, on the same day and t2 is after t1
    h1, m1, s1 = t1.hour, t1.minute, t1.second
    h2, m2, s2 = t2.hour, t2.minute, t2.second
    t1_secs = s1 + 60 * (m1 + 60 * h1)
    t2_secs = s2 + 60 * (m2 + 60 * h2)
    seconds = t2_secs - t1_secs;
    print(seconds)
    # hh1=seconds//3600;
    # hh2=seconds//3600;
    hh1 = (t1_secs // 3600);
    hh2 = (t2_secs // 3600);

    return (h2 - h1);


def diff_times_in_minutes(t1, t2):
    # caveat emptor - assumes t1 & t2 are python times, on the same day and t2 is after t1
    h1, m1, s1 = t1.hour, t1.minute, t1.second
    h2, m2, s2 = t2.hour, t2.minute, t2.second
    t1_secs = s1 + 60 * (m1 + 60 * h1)
    t2_secs = s2 + 60 * (m2 + 60 * h2)

    return (m2 - m1);


app.run(debug=True)
