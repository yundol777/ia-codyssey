try:
    #1. 파일 읽어들여 출력
    print("1. 파일 읽어들여 출력")

    with open('./mission_computer_main.log', 'r', encoding='utf-8') as f:
        print(f.read())
    
    #2 콤마 기준으로 리스트 객체로 전환 후 출력
    print("2. 콤마 기준으로 리스트 객체로 전환 후 출력")

    with open('./mission_computer_main.log', 'r', encoding='utf-8') as f:
        lines = f.readlines()[1:]

    lines_lists = []
    for line in lines:
        lines_lists.append(line.split(','))
    
    print(lines_lists)

    #3 리스트 객체 시간의 역순으로 정렬
    lines_lists.sort(reverse=True)

    #4 리스트 객체 사전 객체로 전환
    lines_dict = []
    format_key = ["time", "type", "log"]
    for lines_list in lines_lists:
        lines_dict.append(dict(zip(format_key, lines_list)))
    
    #5 mission_computer_main.json 파일로 저장하는데 JSON으로 저장
    lines_json = str(lines_dict).replace("'", '"').replace('\\n', '').replace('rocket"s',"rocket's")  
    print("lines_json 형식")
    print(lines_json)

    with open('./mission_computer_main.json', 'w', encoding='utf-8') as f:
        f.write(lines_json)

except Exception as e:
    error_message = str(e)
    error_file = open('./error_file.txt', 'w')
    error_file.write(error_message)
    error_file.close()


    