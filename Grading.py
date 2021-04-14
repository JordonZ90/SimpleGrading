def grading():
    counter = 0
    score_total = 0
    test_score = 0
    class_size_ratio = int(input("Enter class size ")) * 100  # * 100  # class size multiplied by highest test score
    class_size = class_size_ratio // 100
    if class_size_ratio < 0:
        print("Student count cannot be below zero")
        grading()
    else:
        print(f"Max points possible {class_size_ratio}")
        print(f"Class size: {class_size}")

    while test_score != class_size_ratio and counter != class_size:  # test_score != 999
        test_score = int(input("Enter test score "))
        if 0 <= test_score <= 100:  # 0 <= test_score <= 100
            score_total += test_score
            counter += 1
        else:
            print("Discarding score")
            print(f"Total score: {score_total} ")
            continue
        # if score_total >= class_size_ratio:
        #     print("=" * 22)
        #     print("Scoring complete")
        #     print(f"Total score: {class_size_ratio} \nAverage score: {average_score} \nGrade: {grade}")
        #     break
        if counter == class_size:
            print("=" * 22)
            print("Scoring complete")
        if test_score >= 90:
            grade = "A"
        elif test_score >= 80:
            grade = "B"
        elif test_score >= 70:
            grade = "C"
        elif test_score >= 60:
            grade = "D"
        else:
            grade = "F"

        #  Calculate average score
        average_score = round(score_total / counter)
        #  Display results
        print(f"Total score: {score_total} \nAverage score: {average_score} \nGrade: {grade}")


grading()
