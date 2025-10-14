def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "0으로 나눌 수 없습니다."
    return a / b

while True:  # 메인 루프 시작
    try:
        num1 = float(input("첫 번째 숫자를 입력하세요: "))
        num2 = float(input("두 번째 숫자를 입력하세요: "))
    except ValueError:
        print("잘못된 숫자 형식입니다. 숫자를 다시 입력해주세요.")
        continue  # 숫자 입력 단계로 다시 시작

    while True:  # 연산 선택 루프 시작
        print("연산을 선택하세요:")
        print("1. 덧셈")
        print("2. 뺄셈")
        print("3. 곱셈")
        print("4. 나눗셈")
        print("5. 전부 다 (All)")
        print("6. 종료")

        choice = input("선택 (1/2/3/4/5/6): ")

        if choice == '6':
            print("계산기를 종료합니다.")
            break  # 메인 루프 종료
        elif choice in ('1', '2', '3', '4', '5'):
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2):.2f}")  # 소수점 2자리 제한
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2):.2f}")  # 소수점 2자리 제한
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2):.2f}")  # 소수점 2자리 제한
            elif choice == '4':
                result = divide(num1, num2)
                if isinstance(result, str):  # "0으로 나눌 수 없습니다." 경우 처리
                    print(f"{num1} / {num2} = {result}")
                else:
                    print(f"{num1} / {num2} = {result:.2f}")  # 소수점 2자리 제한
            elif choice == '5':
                print(f"{num1} + {num2} = {add(num1, num2):.2f}")  # 소수점 2자리 제한
                print(f"{num1} - {num2} = {subtract(num1, num2):.2f}")  # 소수점 2자리 제한
                print(f"{num1} * {num2} = {multiply(num1, num2):.2f}")  # 소수점 2자리 제한
                result = divide(num1, num2)
                if isinstance(result, str):  # "0으로 나눌 수 없습니다." 경우 처리
                    print(f"{num1} / {num2} = {result}")
                else:
                    print(f"{num1} / {num2} = {result:.2f}")  # 소수점 2자리 제한
            break  # 연산 선택 루프 종료, 메인 루프 다시 시작
        else:
            print("잘못된 선택입니다. 다시 선택해주세요.")
            continue  # 연산 선택 루프 다시 시작
    break #여기에 break가 하나 더있어야함