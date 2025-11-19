from pyscript import document, display

def performance_button (e):

    #These document.getElementById's avoid repeating results.
    document.getElementById("studentInfo").innerHTML = " "
    document.getElementById("attendance_place").innerHTML = " "
    document.getElementById("quizBreakdown").innerHTML = " "
    document.getElementById("finalPerformanceRating").innerHTML = " "

    #These variables collect form inputs.
    studentFirst = document.getElementById('firstName').value 
    studentLast = document.getElementById('lastName').value

    #ATTENDANCE
    schoolDays = float(document.getElementById('total_days').value)
    presentDays = float(document.getElementById('present_days').value)

    #ASSESSMENT SCORES


    drill_1 = float(document.getElementById('grades_Drill1').value)
    drill_2 = float(document.getElementById('grades_Drill2').value)
    sw_1 = float(document.getElementById('grades_SW1').value)
    sw_2 = float(document.getElementById('grades_SW2').value)
    skillsTest = float(document.getElementById('grades_Skills').value)


    #Below is a list
    requirements = [drill_1, drill_2, sw_1, sw_2, skillsTest]

    weights = (0.01, 0.01, 0.15, 0.15, 0.15, 0.20)

    rating_weights = (0.1, 0.90)

    #Attendance Computation
    attendance_percentage = (presentDays / (schoolDays + (schoolDays == 0))) * (schoolDays != 0)

    weighted_assessment_score = (
        requirements[0] * weights[0] + 
        requirements[1] * weights[1] +
        requirements[2] * weights[2] +
        requirements[3] * weights[3] +
        requirements[4] * weights[4] 
        )

    #FINAL PERFORMANCE RATING
    final_rating = attendance_percentage * rating_weights[0] + weighted_assessment_score * rating_weights[1]

    #OUTPUT DISPLAY AREA
    display(f'Name: {studentFirst} {studentLast}', target="studentInfo")
    display(f'Attendance: {attendance_percentage}', target="attendance_place")
    display(weighted_assessment_score, target="quizBreakdown")
    display(final_rating, target="finalPerformanceRating")

