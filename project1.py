class Person:
    def data_1(self, name, age, gender):
        self._name = (input("Enter your name : "))    
        self._age = (input("Enter your age : "))
        self._gender = (input("Enter your gender : "))
    
class Patient(Person):
    def data_2(self, patient_id, name, age, gender, illness):
        (name, age, gender)
        self._patient_id = (input("Enter patient id : "))                             
        self._illness = (input("Enter the illness : "))   

class OutPatient(Patient):
    def data_3(self, patient_id, name, age, gender, illness, visit_date):
        (patient_id, name, age, gender, illness)
        self._visit_date = (input("Enter the visit date : "))

class InPatient(Patient):
    def data_4(self, patient_id, name, age, gender, illness, room_no, days_admitted):
        (patient_id, name, age, gender, illness)
        self._room_no = (input("Enter the room no : "))
        self._days_admitted = (input("Enter the days admitted : "))

class Doctor(Person):
    def data_5(self, doctor_id, name, age, gender, specialty):
        (name, age, gender)
        self._doctor_id = (input("Enter the doctor id : "))
        self._specialty = (input("Enter the speciality : "))

class Appointment:
    def data_6(self, patient_name, doctor_name, date):
        self._patient_name = (input("Enter the patient name : "))
        self._doctor_name = (input("Enter the doctor name : "))
        self._date = (input("Enter the date : "))


p = Person()

q = p.data_1('name', 'age', 'gender')
print(q)      

r = Patient()
o = r.data_2('name', 'age', 'gender', 'illness', 'patient_id')
print(o)   

c = OutPatient()
t = c.data_3('patient_id', 'name', 'age', 'gender', 'illness', 'visit_date')
print(t)

f = InPatient()
g = f.data_4('patient_id', 'name', 'age', 'gender', 'illness', 'room_no', 'days_admitted')
print(g)

w = Doctor()
x = w.data_5('doctor_id', 'name', 'age', 'gender', 'speciality')
print(x)

j = Appointment()
k = j.data_6('patient_name', 'doctor_name', 'date')
print(k)
