knowledge_base = {
    "Fever": {
        "CommonCold": 0.2,
        "Flu": 0.8
    },
    "Cough": {
        "CommonCold": 0.7,
        "Flu": 0.9
    },
    "SoreThroat": {
        "CommonCold": 0.5,
        "Flu": 0.3,
        "StrepThroat": 0.9
    },
}
def diagnose_symptoms(symptoms, knowledge_base):
    diagnoses = {}

    for disease in knowledge_base[symptoms[0]]:
        confidence = knowledge_base[symptoms[0]][disease]

        for symptom in symptoms[1:]:
            confidence *= knowledge_base[symptom][disease]

        diagnoses[disease] = confidence

    return diagnoses
def main():
    symptoms = []
    print("Enter symptoms (one at a time, or 'done' to finish):")
    while True:
        symptom = input()
        if symptom == "done":
            break
        symptoms.append(symptom)
    if len(symptoms) == 0:
        print("No symptoms entered.")
        return
    diagnoses = diagnose_symptoms(symptoms, knowledge_base)
    sorted_diagnoses = sorted(diagnoses.items(), key=lambda x: x[1], reverse=True)
    print("\nDiagnosis:")
    for disease, confidence in sorted_diagnoses:
        print(f"{disease}: {confidence * 100:.2f}%")
if __name__ == "__main__":
    main()


