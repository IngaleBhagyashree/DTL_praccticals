# Rule-Based Expert System

symptom1 = input("Enter first symptom: ").lower()
symptom2 = input("Enter second symptom (or none): ").lower()

if symptom1 == "fever" and symptom2 == "cough":
    print("Possible Diagnosis: Flu")
elif symptom1 == "fever" and symptom2 == "headache":
    print("Possible Diagnosis: Viral Infection")
elif symptom1 == "stomach pain" or symptom2 == "stomach pain":
    print("Possible Diagnosis: Food Poisoning")
else:
    print("Diagnosis: Consult a Doctor")


symptom1 = input("Enter first symptom: ").lower()
symptom2 = input("Enter second symptom (or none): ").lower()

if symptom1 == "fever" and symptom2 == "cough":
    print("Possible Diagnosis: Flu")
elif symptom1 == "fever" and symptom2 == "headache":
    print("Possible Diagnosis: Viral Infection")
elif symptom1 == "stomach pain" or symptom2 == "stomach pain":
    print("Possible Diagnosis: Food Poisoning")
else:
    print("Diagnosis: Consult a Doctor")
