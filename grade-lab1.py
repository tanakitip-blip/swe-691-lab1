def calculate_grade(scores):
    # 1. ตรวจสอบว่ามีข้อมูลใน List หรือไม่ เพื่อป้องกัน ZeroDivisionError
    if not scores:
        return "No scores provided", 0.0

    # 2. ตรวจสอบว่าข้อมูลทุกตัวเป็นตัวเลข (Optional แต่แนะนำ)
    if not all(isinstance(s, (int, float)) for s in scores):
        return "Invalid data type in scores", 0.0

    # 3. ใช้ sum() แทนการเขียน loop เองเพื่อความรวดเร็วและอ่านง่าย
    total = sum(scores)
    average = total / len(scores)
    
    # 4. การคำนวณเกรด
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"
        
    return grade, average

# ทดสอบกรณีปกติ
scores_normal = [85, 92, 78, 88, 95]
print(f"Normal: {calculate_grade(scores_normal)}")

# ทดสอบกรณี List ว่าง (แก้ไข bug แล้ว)
scores_empty = []
print(f"Empty: {calculate_grade(scores_empty)}")

# ทดสอบกรณีมีข้อมูลที่ไม่ใช่ตัวเลข
scores_invalid = [80, "90", 70]
print(f"Invalid: {calculate_grade(scores_invalid)}")
