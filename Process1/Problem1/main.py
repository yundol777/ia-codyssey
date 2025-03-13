# 'Hello Mars' 출력
print('Hello Mars')

# mission_computer_main.log 파일 열고 출력
with open('./mission_computer_main.log', 'r', encoding='utf-8') as f:
    print(f.read())

# log_analysis.md 파일에 보고서 작성
with open('./log_analysis.md', 'w', encoding='utf-8') as f:
    f.write('사고 원인 분석 보고서\n')
    f.write('작성자 : 박사 한송희\n')
    f.write('2023-08-27 11:35분 경 산소 탱크 불안정\n')
    f.write('2023-08-27 11:40분 경 산소 탱크 폭발\n')
    f.write('2023-08-27 12:00분 경 산소 탱크 폭발로 인한 센터 및 임무 제어 시스템 전원 오프\n')

# 출력 결과 역순 출력
with open('./mission_computer_main.log', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in reversed(lines):
        print(line.strip())

# 로그 파일 중 문제되는 부분 error.log 파일에 저장
with open('./mission_computer_main.log', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    error = lines[-3:]

with open('./error.log', 'w', encoding='utf-8') as f:
    f.writelines(error)

