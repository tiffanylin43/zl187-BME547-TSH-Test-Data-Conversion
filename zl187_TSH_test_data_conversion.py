def read_in_data():
    f = open('test_data.txt')
    file = f.readlines()
    num_line = 0
    for line in file:
        line = line.strip()
        if num_line < len(file):
            file[num_line] = line
            num_line = num_line+1
    return file


def extract_info(file):
    m = len(file) - 1
    n = int(m/4)
    first_name = []
    last_name = []
    age = []
    gender = []
    TSH = []
    for i in range(n):
        name = file[4*i]
        first_name1, last_name1 = name.split()
        first_name.append(first_name1)
        last_name.append(last_name1)
        age1 = file[4*i+1]
        age.append(age1)
        gender1 = file[4*i+2]
        gender.append(gender1)
        TSH_str = file[4*i+3]
        TSH1 = TSH_str.split(',')
        TSH1.pop(0)
        TSH.append(TSH1)
    return first_name, last_name, age, gender, TSH


def diagnosis(TSH):
    n = len(TSH)
    diagnosis = []
    for i in range(n):
        TSH1 = TSH[i]
        normal = 1
        for j in range(len(TSH1)):
            TSH2 = float(TSH1[j])
            if TSH2 < 1.0:
                print('hyperthyroidism')
                normal = 0
                result = 'hyperthyroidism'
                break
            if TSH2 > 4.0:
                print('hypothyroidism')
                normal = 0
                result = 'hypothyroidism'
                break
        if normal == 1:
            print('normal thyroid function')
            result = 'normal thyroid function'
        diagnosis.append(result)


def main_code():
    file = read_in_data()
    first_name, last_name, age, gender, TSH = extract_info(file)
    diagnosis(TSH)


if __name__ == "__main__":
    main_code()
    
        
            
    
    