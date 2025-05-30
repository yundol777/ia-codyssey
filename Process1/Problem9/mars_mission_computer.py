# mars_mission_computer.py

import time
import threading
import multiprocessing
import platform
import os
import json
import subprocess


class MissionComputer:
    def get_mission_computer_info(self):
        while True:
            try:
                if os.name == 'nt':
                    import ctypes

                    class MEMORYSTATUSEX(ctypes.Structure):
                        _fields_ = [
                            ('dwLength', ctypes.c_ulong),
                            ('dwMemoryLoad', ctypes.c_ulong),
                            ('ullTotalPhys', ctypes.c_ulonglong),
                            ('ullAvailPhys', ctypes.c_ulonglong),
                            ('ullTotalPageFile', ctypes.c_ulonglong),
                            ('ullAvailPageFile', ctypes.c_ulonglong),
                            ('ullTotalVirtual', ctypes.c_ulonglong),
                            ('ullAvailVirtual', ctypes.c_ulonglong),
                            ('sullAvailExtendedVirtual', ctypes.c_ulonglong),
                        ]

                    memory_status = MEMORYSTATUSEX()
                    memory_status.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
                    ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(memory_status))
                    total_memory = round(memory_status.ullTotalPhys / (1024 ** 3), 2)
                else:
                    mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
                    total_memory = round(mem_bytes / (1024 ** 3), 2)

                info = {
                    '운영체계': platform.system(),
                    '운영체계 버전': platform.version(),
                    'CPU 타입': platform.processor(),
                    'CPU 코어 수': os.cpu_count(),
                    '메모리 크기 (GB)': total_memory
                }

                print('[INFO]', json.dumps(info, indent=2, ensure_ascii=False))
            except Exception as e:
                print('[INFO] 시스템 정보 오류:', e)

            time.sleep(20)  # 20초마다 출력

    def get_mission_computer_load(self):
        while True:
            try:
                if os.name == 'nt':
                    cpu_cmd = 'wmic cpu get loadpercentage'
                    cpu_output = subprocess.check_output(cpu_cmd, shell=True).decode().splitlines()
                    cpu_percent = next(
                        int(line.strip()) for line in cpu_output if line.strip().isdigit()
                    )

                    mem_cmd = 'wmic OS get FreePhysicalMemory,TotalVisibleMemorySize /Value'
                    mem_output = subprocess.check_output(mem_cmd, shell=True).decode().splitlines()
                    mem_values = {}
                    for line in mem_output:
                        if '=' in line:
                            key, value = line.strip().split('=')
                            mem_values[key] = int(value)

                    total = mem_values['TotalVisibleMemorySize']
                    free = mem_values['FreePhysicalMemory']
                    used_percent = round((1 - free / total) * 100, 2)
                else:
                    cpu_percent = float(os.popen("top -bn1 | grep 'Cpu(s)'").read().split('%')[0].split()[-1])
                    used_percent = float(os.popen("free | grep Mem").read().split()[2]) / float(
                        os.popen("free | grep Mem").read().split()[1]) * 100

                load = {
                    'CPU 실시간 사용량 (%)': cpu_percent,
                    '메모리 실시간 사용량 (%)': used_percent
                }

                print('[LOAD]', json.dumps(load, indent=2, ensure_ascii=False))
            except Exception as e:
                print('[LOAD] 부하 정보 오류:', e)

            time.sleep(20)

    def get_sensor_data(self):
        while True:
            # 임시 센서 데이터 예시
            sensor = {'온도 센서': 36.5, '압력 센서': 101.3}
            print('[SENSOR]', json.dumps(sensor, ensure_ascii=False))
            time.sleep(20)


def threading_mode():
    run_computer = MissionComputer()
    threads = [
        threading.Thread(target=run_computer.get_mission_computer_info, name='info', daemon=True),
        threading.Thread(target=run_computer.get_mission_computer_load, name='load', daemon=True),
        threading.Thread(target=run_computer.get_sensor_data, name='sensor', daemon=True),
    ]
    for t in threads:
        t.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('\n[THREAD] 모니터링 종료')


# 프로세스용 함수 정의 (Pickling 문제 방지)
def process_info():
    MissionComputer().get_mission_computer_info()

def process_load():
    MissionComputer().get_mission_computer_load()

def process_sensor():
    MissionComputer().get_sensor_data()


def multiprocessing_mode():
    processes = [
        multiprocessing.Process(target=process_info, name='info'),
        multiprocessing.Process(target=process_load, name='load'),
        multiprocessing.Process(target=process_sensor, name='sensor'),
    ]
    for p in processes:
        p.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        for p in processes:
            p.terminate()
        print('\n[PROCESS] 모니터링 종료')


def main():
    mode = input("모드를 선택하세요 (1: 쓰레드, 2: 프로세스): ")
    if mode == '1':
        threading_mode()
    else:
        multiprocessing_mode()


if __name__ == '__main__':
    main()
