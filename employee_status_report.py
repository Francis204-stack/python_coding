employee_name = input("Enter employee name: ")
attendance = [
    "P", "P", "P", "A", "P", "P", "P", "P", "P", "P", "P", "A", "A", "A", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P"
]

def attendance_status(count):
    if count >= 28:
        return "Excellent"
    elif count >= 25:
        return "Good"
    else:
        return "Poor"

present_count = 0
absent_count = 0
three_days_absent = False
consecutive = 0
for day in attendance:
    if day == "P":
        present_count += 1
        consecutive = 0
    elif day == "A":
        absent_count += 1
        consecutive += 1
        if consecutive == 3:
            three_days_absent = True

def employee_report(name, attendance_list):
    present = attendance_list.count("P")
    absent = attendance_list.count("A")

    status = attendance_status(present)

    consecutive = 0
    alert = False
    for day in attendance_list:
        if day == "A":
            consecutive += 1
            if consecutive == 3:
                alert = True

    print("Employee name: ", employee_name)
    print("Days Present: ", present_count)
    print("Days Absent: ", absent_count)
    print("Status: ", status)

    if status == "Excellent":
        print("Excellent Work! Eligible for bonus!")
    elif status == "Good":
        print("Quite Impressive!")
    elif status == "Poor":
        print("Warning required")

    if alert:
        print(f"{employee_name} has been absent for 3 consecutive days!")

employee_report(employee_name, attendance)
