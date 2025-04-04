pi = 3.141592
material_weight = {
    "유리" : 2.4,
    "알루미늄" : 2.7,
    "탄소강" : 7.85
}

#5. 재료 무게 화성의 중력으로 재측정
def calculate_mars_weight(earth_weight):
    mars_gravity = 3.71
    earth_gravity = 9.81
    mars_weight = earth_weight * (mars_gravity / earth_gravity)
    return round(mars_weight, 3)

#1. 반구체 형태의 돔의 전체 면적 구하는 sphere_area 함수 구현
#2. shpere_area 함수에 재질(material), 두께(thickness)를 파라미터로 입력할 수 있게 만든다.
#4. 재질의의 기본값은 유리, 두께 기본값은 1cm
def sphere_area(diameter, material="유리", thickness=1):
    radius = diameter / 2
    total_area = 3 * pi * radius ** 2
    
    weight = material_weight.get(material)
    volume = total_area * thickness
    sphere_weight = calculate_mars_weight(volume * weight / 1000)
    
    return round(total_area, 3), sphere_weight

while True:
    #3. 재질과 지름은 input()을 사용해서 사용자로부터 입력을 받아야 한다.
    material = input("재료의 재질을 입력해주세요 (기본값: 유리) : ").strip()
    if material == "":
        material = "유리"
    if material not in ["유리", "알루미늄", "탄소강"]:
        print("가지고 있지 않은 재료입니다.")
        continue
    
    diameter = input("지름을 입력해주세요(cm) : ")
    try:
        diameter = float(diameter)
        if diameter <= 0:
            print("지름은 0보다 커야 합니다.")
            continue
    except:
        print("지름은 숫자로 입력해주세요")
        continue
    
    

    #6. 전역변수에 나머지 값 저장
    thickness = 1
    area, weight = sphere_area(diameter, material, thickness)

    #7. 양식에 맞게 출력력
    print(f"재질 ==> {material}, 지름 ==> {round(diameter,3)}cm, 두께 ==> {thickness}cm, 면적 ==> {area}cm², 무게 ==> {weight}kg")


    again = input("이어서 계산하시겠습니까? (y/n): ")
    if again != 'y':
        print("프로그램을 종료합니다.")
        break