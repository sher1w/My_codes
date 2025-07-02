# Step 1: Define simple disease database
diseases = {
    "Flu": {
        "symptoms": ["fever", "cough", "sore throat", "body aches", "runny nose", "fatigue"],
        "advice": "Rest and stay hydrated. May need antiviral medicine."
    },
    "COVID-19": {
        "symptoms": ["fever", "cough", "shortness of breath", "loss of taste", "headache", "fatigue"],
        "advice": "Get tested. Isolate and monitor your oxygen."
    },
    "Measles": {
        "symptoms": ["fever", "rash", "runny nose", "cough"],
        "advice": "See a doctor immediately. Avoid contact with others."
    },
    "Common Cold": {
        "symptoms": ["cough", "sore throat", "runny nose", "headache"],
        "advice": "Rest and drink warm fluids."
    },
    "Dengue": {
        "symptoms": ["fever", "rash", "headache", "body aches"],
        "advice": "Check platelets. Go to hospital if symptoms are severe."
    },
    "Malaria": {
        "symptoms": ["fever", "headache", "body aches", "chills"],
        "advice": "Get a blood test. Go to clinic."
    }
}

# Step 2: Ask user for symptoms
print("=== Welcome to the Simple Medical Expert System ===")
user_symptoms = []

print("\nAnswer YES or NO to the following symptoms:")

all_symptoms = ["fever", "cough", "sore throat", "body aches", "rash", "headache",
                "runny nose", "shortness of breath", "loss of taste", "fatigue", "chills"]
for symptom in all_symptoms:
    answer = input(f"Do you have {symptom}? ").strip().lower()
    if answer == "yes":
        user_symptoms.append(symptom)
# Step 3: Match symptoms with diseases
matches = {}
for disease in diseases:
    symptoms = diseases[disease]["symptoms"]
    common = 0
    for sym in user_symptoms:
        if sym in symptoms:
            common += 1
    if common > 0:
        percent = int((common / len(symptoms)) * 100)
        matches[disease] = percent
# Step 4: Show result
if not matches:
    print("\n❌ No matching disease found. Please see a doctor.")
else:
    print("\n✅ Possible Diagnoses:")
    for disease in sorted(matches, key=matches.get, reverse=True):
        print(f"- {disease} ({matches[disease]}% match)")
        print("  Advice:", diseases[disease]["advice"])
    print("\n⚠️ Always consult a real doctor for confirmation.")
