import json


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
    diag = []
    TSH1 = []
    for i in range(n):
        TSH1 = TSH[i]
        normal = 1
        for j in range(len(TSH1)):
            TSH2 = float(TSH1[j])
            if TSH2 < 1.0:
                # print('hyperthyroidism')
                normal = 0
                result = 'hyperthyroidism'
                break
            if TSH2 > 4.0:
                # print('hypothyroidism')
                normal = 0
                result = 'hypothyroidism'
                break
        if normal == 1:
            # print('normal thyroid function')
            result = 'normal thyroid function'
        diag.append(result)
    return diag


class patient():
    def __init__(self, first_name, last_name, age, gender, TSH, diagnosis):
        self.firstname = first_name
        self.lastname = last_name
        self.age = age
        self.gender = gender
        self.TSH = TSH
        self.diagnosis = diagnosis


def create_patient(firstname, lastname, age1, gender1,
                   TSH_result, diag_result):
    new_patient = patient(firstname, lastname, age1, gender1,
                          TSH_result, diag_result)
    return new_patient


def create_dic(patient):
    patient = {"First name": patient.firstname,
               "Last name": patient.lastname,
               "Age": patient.age,
               "Gender": patient.gender,
               "TSH": patient.TSH,
               "Diagnosis": patient.diagnosis}
    return patient


def main_code():
    file = read_in_data()
    first_name, last_name, age, gender, TSH = extract_info(file)
    diag = diagnosis(TSH)
    for i in range(len(first_name)):
        firstname = first_name[i]
        lastname = last_name[i]
        age1 = age[i]
        gender1 = gender[i]
        TSH_result = TSH[i]
        diag_result = diag[i]
        ptnt1 = create_patient(firstname, lastname, age1, gender1,
                               TSH_result, diag_result)
        ptnt = create_dic(ptnt1)
        name = [firstname, lastname]
        connect = '-'
        name_patient = connect.join(name)
        name_file = name_patient + ".json"
        out_file = open(name_file, "w")
        json.dump(ptnt, out_file)
        out_file.close()
        in_file = open(name_file, "r")
        new_variable = json.load(in_file)
        in_file.close()
        print("****************************************")
        print("Contents in {} are:".format(name_file))
        print(new_variable)
        print("****************************************")


if __name__ == "__main__":
    main_code()
