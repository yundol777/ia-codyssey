import random

# 1. 더미 센서 클래스 생성
class DummySensor:
    # 2. env_values라는 사전 객체를 멤버로 추가
    def __init__(self):
        self.env_values = {
            "mars_base_internal_temperature": None,
            "mars_base_external_temperature": None,
            "mars_base_internal_humidity": None,
            "mars_base_external_illuminance": None,
            "mars_base_internal_co2": None,
            "mars_base_internal_oxygen": None,
        }

    # 3. 랜덤으로 값 설정
    def set_env(self):
        self.env_values["mars_base_internal_temperature"] = round(random.uniform(18, 30), 2)
        self.env_values["mars_base_external_temperature"] = round(random.uniform(0, 21), 2)
        self.env_values["mars_base_internal_humidity"] = round(random.uniform(50, 60), 2)
        self.env_values["mars_base_external_illuminance"] = round(random.uniform(500, 715), 2)
        self.env_values["mars_base_internal_co2"] = round(random.uniform(0.02, 0.1), 4)
        self.env_values["mars_base_internal_oxygen"] = round(random.uniform(4, 7), 2)

    # 4. get_env() 메소드 (현재 env_values 반환)
    def get_env(self):
        return self.env_values

#5. 인스턴스 생성 및 확인
ds = DummySensor()
ds.set_env()
env_data = ds.get_env()

print("Dummy Sensor Data:")
for key, value in env_data.items():
    print(f"{key}: {value}")