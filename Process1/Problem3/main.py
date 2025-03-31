try:
    #1. 파일 읽어들여 출력
    print("1. 파일 읽어들여 출력")

    with open('./Mars_Base_Inventory_List.csv', 'r', encoding='utf-8') as f:
        print(f.read())
    
    #2 콤마 기준으로 리스트 객체로 전환 후 출력
    print("2. 콤마 기준으로 리스트 객체로 전환 후 출력")

    with open('./Mars_Base_Inventory_list.csv', 'r', encoding='utf-8') as f:
        lines = f.readlines()[1:]

    lines_lists = []
    for line in lines:
        lines_lists.append(line.strip().split(','))
    
    print(lines_lists)

    #3 인화성 높은 순으로 정렬
    print("3. 인화성 높은 순으로 정렬")
    lines_lists.sort(key=lambda x: float(x[-1]), reverse=True)
    
    for line in lines_lists:
        print(line)

    # #4 인화성 지수 0.7 이상되는 목록 뽑아서 출력
    print("4. 인화성 지수 0.7 이상 되는 목록 뽑아서 출력")
    lines_over_07 = []
    lines_over_07 = [item for item in lines_lists if float(item[-1]) >= 0.7]
    for line in lines_over_07:
        print(line)
        
    #50.7 이상되는 목록 Mars_Base_Inventory_danger.csv로 저장장

    with open('./Mars_Base_Inventory_danger.csv', 'w', encoding='utf-8') as f:
        for item in lines_over_07:
            line = ','.join(item).strip()  # 리스트를 문자열로 변환 + 개행 제거
            f.write(line + '\n')

except Exception as e:
    error_message = str(e)
    error_file = open('./error_file.txt', 'w')
    error_file.write(error_message)
    error_file.close()