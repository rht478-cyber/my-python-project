height = float(input("키(cm): ")) / 100
weight = float(input("몸무게(kg): "))
bmi = weight / (height * height)
print(f"당신의 BMI는 {bmi:.2f}입니다.")