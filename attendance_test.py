
# attendance_test.py
# Sample tests for AttendX attendance marking

def test_mark_attendance():
    student_id = "STU101"
    status = "Present"

    if student_id and status in ["Present", "Absent"]:
        print("PASS: Valid attendance data")
    else:
        print("FAIL: Invalid attendance data")


def test_invalid_attendance():
    student_id = ""
    status = "Unknown"

    if not student_id or status not in ["Present", "Absent"]:
        print("PASS: Invalid attendance data detected")
    else:
        print("FAIL: Invalid attendance data accepted")


if __name__ == "__main__":
    test_mark_attendance()
    test_invalid_attendance()
    test_username_only()
