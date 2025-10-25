from datetime import date  # 전역 범위에서 import

def write_diary():
    today = date.today()
    filename = f"{today}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(input("오늘의 일기를 입력하세요: "))
    print("일기가 저장되었습니다.")

def load_diary():
    date_str = input("불러올 일기의 날짜를 입력하세요 (YYYY-MM-DD): ")
    filename = f"{date_str}.txt"
    try:
        with open(filename, "r", encoding="utf-8") as f:
            print("\n📖 해당 날짜의 일기:")
            print(f.read())
    except FileNotFoundError:
        print("해당 날짜의 일기가 존재하지 않습니다.")
    except Exception as e:
        print(f"오류 발생: {e}")

while True:
    print("\n📒 나만의 일기장 프로그램")
    print("1. 오늘의 일기 쓰기")
    print("2. 과거 일기 불러오기")
    print("3. 종료")

    choice = input("원하는 기능을 선택하세요 (1-3): ")

    if choice == "1":
        write_diary()
    elif choice == "2":
        load_diary()
    elif choice == "3":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 선택입니다. 다시 선택해주세요.")
