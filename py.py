def predict_performance():
    student_id = int(input("Enter student ID for prediction: "))

    # Get selected student
    cursor.execute("SELECT percentage FROM students WHERE id = ?", (student_id,))
    result = cursor.fetchone()

    if result is None:
        print("❌ Student not found!")
        return

    student_percentage = result[0]

    # Get class average
    cursor.execute("SELECT AVG(percentage) FROM students")
    avg_result = cursor.fetchone()

    class_average = avg_result[0]

    print(f"\nStudent Percentage: {student_percentage}")
    print(f"Class Average: {class_average:.2f}")

    # Prediction Logic (Simple AI Model)
    if student_percentage > class_average + 10:
        prediction = "📈 Likely to remain Top Performer"
    elif student_percentage < class_average - 10:
        prediction = "📉 Risk of Performance Drop"
    else:
        prediction = "➖ Stable Performance Expected"

    print("🧠 AI Prediction:", prediction)
