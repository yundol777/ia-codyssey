# mars_mission_computer.py

import platform
import os
import json
import subprocess


class MissionComputer:
    def get_mission_computer_info(self):
        try:
            if os.name == 'nt':
                # Windows의 경우 메모리 확인 (ctypes 사용)
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
                # Linux, macOS
                mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
                total_memory = round(mem_bytes / (1024 ** 3), 2)

            info = {
                '운영체계': platform.system(),
                '운영체계 버전': platform.version(),
                'CPU 타입': platform.processor(),
                'CPU 코어 수': os.cpu_count(),
                '메모리 크기 (GB)': total_memory
            }

            print('시스템 정보:', json.dumps(info, indent=2, ensure_ascii=False))
            return info

        except Exception as e:
            print('시스템 정보를 가져오는 중 오류:', e)
            return {}

    def get_mission_computer_load(self):
        try:
            if os.name == 'nt':
                # CPU 사용량 (LoadPercentage)
                cpu_cmd = 'wmic cpu get loadpercentage'
                cpu_output = subprocess.check_output(cpu_cmd, shell=True).decode().splitlines()
                cpu_percent = next(
                    int(line.strip()) for line in cpu_output if line.strip().isdigit()
                )

                # 메모리 사용량
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
                # 유닉스 계열 시스템
                cpu_percent = float(os.popen("top -bn1 | grep 'Cpu(s)'").read().split('%')[0].split()[-1])
                used_percent = float(os.popen("free | grep Mem").read().split()[2]) / float(os.popen("free | grep Mem").read().split()[1]) * 100

            load = {
                'CPU 실시간 사용량 (%)': cpu_percent,
                '메모리 실시간 사용량 (%)': used_percent
            }

            print('시스템 부하 정보:', json.dumps(load, indent=2, ensure_ascii=False))
            return load

        except Exception as e:
            print('시스템 부하 정보를 가져오는 중 오류:', e)
            return {}


if __name__ == '__main__':
    runComputer = MissionComputer()
    runComputer.get_mission_computer_info()
    runComputer.get_mission_computer_load()
