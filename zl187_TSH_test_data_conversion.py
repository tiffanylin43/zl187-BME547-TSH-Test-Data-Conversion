import json


def read_in_data(filename):
    """Read in the data from .txt file named filename

    Args:
        filename: full name of the file that needs to be read in
                  with suffix of .txt

    returns:
        file: the contents in filename.txt line by line without
              "/n" at the end of each line
    """
    f = open(filename)
    file = f.readlines()
    num_line = 0
    for line in file:
        # get rid of the "/n" at the end of each line
        line = line.strip()
        if num_line < len(file):
            file[num_line] = line
            num_line = num_line+1
    return file


def extract_info(file):
    """Extract the information needed from input file

    Args:
        file: input that contains information of patients,
              which need to be extracted

    returns:
        first_name: a list contains first names of all patients in file
        last_name: a list contains last names of all patients in file
        age: a list contains ages of all patients in file
        gender: a list contains genders of all patients in file
        TSH: a list contains TSH results of all patients in file
    """
    m = len(file) - 1
    n = int(m/4)
    first_name = []
    last_name = []
    age = []
    gender = []
    TSH = []
    for i in range(n):
        # extract the information of names from every 4 lines
        name = file[4*i]
        # split the full name by space to get first and last name respectively
        first_name1, last_name1 = name.split()
        first_name.append(first_name1)
        last_name.append(last_name1)
        # extract the information of ages from every 4 lines
        age1 = file[4*i+1]
        age.append(age1)
        # extract the information of genders from every 4 lines
        gender1 = file[4*i+2]
        gender.append(gender1)
        # extract the information of TSH results from every 4 lines
        TSH_str = file[4*i+3]
        # split the elements by "," to get each TSH test result
        TSH1 = TSH_str.split(',')
        # delete the first element in the list, which is "TSH"
        TSH1.pop(0)
        TSH.append(TSH1)
    return first_name, last_name, age, gender, TSH


def diagnosis(TSH):
    """Diagnose the patients by the input TSH test results

    "hyperthyroidism" - any of their tests results being less than 1.0,
    "hypothyroidism" - any of their test results being greater than 4.0, or
    "normal thyroid function" - all of their test results being
                                between 1.0 and 4.0, inclusive.
    No single patient will have test results both above 4.0 and below 1.0,
    hence will only meet one of the diagnoses above.

    Args:
        TSH: TSH results from patients

    returns:
        diag: diagnoses of all patients from TSH results input
    """
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
    """A class that has attributes of a certain patient in file

    Attributes:
        first_name: first name of the patient
        last_name: last name of the patient
        age: age of the patient
        gender: gender of the patient
        TSH: TSH test results of the patient
        diagnosis: diagnosis of the patient
    """
    def __init__(self, first_name, last_name, age, gender, TSH, diagnosis):
        """Initialize the class "patient"

        Args:
            first_name: first name of the patient
            last_name: last name of the patient
            age: age of the patient
            gender: gender of the patient
            TSH: TSH test results of the patient
            diagnosis: diagnosis of the patient
        """
        self.firstname = first_name
        self.lastname = last_name
        self.age = age
        self.gender = gender
        self.TSH = TSH
        self.diagnosis = diagnosis


def create_patient(firstname, lastname, age1, gender1,
                   TSH_result, diag_result):
    """Create a new variable of class "patient"

    Args:
        firstname: fisrt name of patient
        lastname: last name of patient
        age1: age of patient
        gender1: gender of patient
        TSH_result: TSH results of patient
        diag_result: diagnosis of patient

    returns:
        new_patient: new variable of the class "patient"
    """
    new_patient = patient(firstname, lastname, age1, gender1,
                          TSH_result, diag_result)
    return new_patient


def create_dic(patient):
    """Create a dictionary based on input patient

    Args:
        patient: variable of class "patient"

    returns:
        patient_info: dictionary created containing infomation of patient
    """
    patient_info = {"First name": patient.firstname,
                    "Last name": patient.lastname,
                    "Age": patient.age,
                    "Gender": patient.gender,
                    "TSH": patient.TSH,
                    "Diagnosis": patient.diagnosis}
    return patient_info


def sort_TSH(TSH):
    """Sort the list of TSH values (low to high)

    Args:
        TSH: TSH results of patients

    returns:
        TSH_sorted: sorted TSH results (low to high)
    """
    n = len(TSH)
    TSH1 = []
    TSH_sorted = []
    for i in range(n):
        TSH_numbers = []
        TSH1 = TSH[i]
        for j in range(len(TSH1)):
            TSH2 = float(TSH1[j])
            TSH_numbers.append(TSH2)
            TSH_numbers.sort()
        TSH_sorted.append(TSH_numbers)
    return TSH_sorted


def create_json_and_print(first_name, last_name, age, gender,
                          TSH, diag, i):
    """create json file and print its contents

    Args:
        first_name: first name of the patient
        last_name: last name of the patient
        age: age of the patient
        gender: gender of the patient
        TSH: TSH test results of the patient
        diag: diagnosis of the patient
        i: the number of the patient in the list

    returns:
        none
    """
    firstname = first_name[i]
    lastname = last_name[i]
    age1 = age[i]
    gender1 = gender[i]
    TSH_result = TSH[i]
    diag_result = diag[i]
    ptnt1 = create_patient(firstname, lastname, age1, gender1,
                           TSH_result, diag_result)
    ptnt = create_dic(ptnt1)
    # create the file name
    name = [firstname, lastname]
    connect = '-'
    name_patient = connect.join(name)
    name_file = name_patient + ".json"
    # create the json file
    out_file = open(name_file, "w")
    json.dump(ptnt, out_file)
    out_file.close()
    # read in the json file and print it out
    in_file = open(name_file, "r")
    new_variable = json.load(in_file)
    in_file.close()
    print("****************************************")
    print("Contents in {} are:".format(name_file))
    print(new_variable)
    print("****************************************")


def main_code():
    """main code for the program

    The main code is to call the functions listed above
    to reach the requirements of this assignment.

    Args:
        none

    returns:
        none
    """
    filename = "test_data.txt"
    file = read_in_data(filename)
    first_name, last_name, age, gender, TSH = extract_info(file)
    TSH = sort_TSH(TSH)
    diag = diagnosis(TSH)
    for i in range(len(first_name)):
        create_json_and_print(first_name, last_name, age, gender,
                              TSH, diag, i)


if __name__ == "__main__":
    main_code()
