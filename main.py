try:
    with open("mydata.txt", "r", encoding="utf-8") as f:
        data = f.read()
        print(data,end='')
except FileNotFoundError:
    print("X 파일을 찾을 수 없습니다.")
except Exception as e:
    print(f"▲ 알 수 없는 오류 발생: {e}")

f = open("mydata.txt", "w", encoding="utf-8")  # 파일 열기
f.write("\n안녕하세요 조래현입니다.\n\n")  # 내용 쓰기
f.close()  # 파일 닫기