#1 NumPy import
import numpy as np

try:
    #2 파일 3개를 numpy 이용하여 가져온다.(ndarray)
    arr1 = np.genfromtxt("mars_base_main_parts-001.csv", delimiter=",", dtype=None, encoding='utf-8-sig', names=True)
    arr2 = np.genfromtxt("mars_base_main_parts-002.csv", delimiter=",", dtype=None, encoding='utf-8-sig', names=True)
    arr3 = np.genfromtxt("mars_base_main_parts-003.csv", delimiter=",", dtype=None, encoding='utf-8-sig', names=True)

    #3 3개의 배열을 merge 후 parts(ndarray) 생성
    parts = np.concatenate((arr1, arr2, arr3))

    #4 parts 이용하여 각 항목의 평균값 측정
    names = parts['parts'].astype(str)
    strengths = parts['strength']
    unique_parts = np.unique(names)

    averages = np.array([
        (part, strengths[names == part].mean())
        for part in unique_parts
    ], dtype=[('parts', 'U30'), ('avg_strength', 'f4')])
    
    
    #5 평균값 50보다 작은 값만 csv 파일로 별도 저장
    filtered = averages[averages['avg_strength'] < 50]

    np.savetxt(
        'parts_to_work_on.csv',    
        filtered,                  
        fmt='%s,%.3f',             
        delimiter=',',             
        header='parts,avg_strength',
    )

    #보너스1 방금 만든 csv 읽어와 parts2에 저장 (ndarray)
    parts2 = np.genfromtxt(
        'parts_to_work_on.csv',
        delimiter=',',
        names=True,
        dtype=None,
        encoding='utf-8'
    )
    
    #보너스2 parts2의 전치 행렬 구하고, parts3에 저장장
    names = parts2['parts']
    strengths = parts2['avg_strength']

    data_matrix = np.vstack((names, strengths))
    parts3 = data_matrix.T

    print(parts3)

except Exception as e:
    error_message = str(e)
    error_file = open('./error_file.txt', 'w')
    error_file.write(error_message)
    error_file.close()