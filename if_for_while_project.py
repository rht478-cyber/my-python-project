import random

answer = random.randint(1, 10)  # 1~10 사이 랜덤 숫자 뽑기

while True:  # 무한 루프 시작 (맞출 때까지 계속)
    try:
        guess = int(input("1부터 10 사이의 숫자를 맞춰보세요: "))  # 사용자 입력 받기
        
        if guess > answer:
            print("더 작은 수예요!")
        elif guess < answer:
            print("더 큰 수예요!")
        else:
            print("정답입니다!")
            break  # 정답 맞추면 루프 종료
    except ValueError:
        print("유효한 숫자를 입력해주세요.")  # 숫자가 아닌 입력에 대한 예외 처리

