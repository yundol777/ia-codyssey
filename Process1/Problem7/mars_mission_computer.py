from dummy_sensor import DummySensor
import time

#1. 미션 컴퓨터 클래스 생성
class MissionComputer:
    def __init__(self):
        #2. env_values 속성 초기화
        self.env_values = {
            "mars_base_internal_temperature": None,
            "mars_base_external_temperature": None,
            "mars_base_internal_humidity": None,
            "mars_base_external_illuminance": None,
            "mars_base_internal_co2": None,
            "mars_base_internal_oxygen": None,
        }
        #3. 이전 시간에 작성한 DummySensor import 후 인스턴스화
        self.ds = DummySensor()
    
    #4. get_sensor_data 메소드 생성
    def get_sensor_data(self):
        while True:
            #5. 센서 값 가져와 env_values에 저장
            self.ds.set_env()
            self.env_values = self.ds.get_env()
            
            #6. json 형식으로 출력
            print("환경 정보 :")
            print("{")
            for key, value in self.env_values.items():
                print(f'  "{key}": {value}')
            print("}")
            
            #7. 5초에 한번씩 반복
            time.sleep(5)
            
            
#8. 인스턴스 생성 및 메소드 호출.
if __name__ == "__main__":
    RunComputer = MissionComputer()
    RunComputer.get_sensor_data()