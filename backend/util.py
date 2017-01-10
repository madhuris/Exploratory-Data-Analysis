import patient
symptoms = [
    {"id": "267036007", "name": "Dyspnea", "count": 17985},
    {"id": "49727002", "name": "Cough", "count": 14868},
    {"id": "139201002", "name": "Dyspnea", "count": 13077},
    {"id": "417506008", "name": "Hemorrhagic stroke monitoring", "count": 10856},
    {"id": "214264003", "name": "Lethargy", "count": 6876},
    {"id": "249477003", "name": "Increased thirst", "count": 6545},
    {"id": "162116003", "name": "Increased frequency of urination", "count": 6361},
    {"id": "14151009", "name": "Hyperesthesia", "count": 6222},
    {"id": "47933007", "name": "Foot pain", "count": 5928},
    {"id": "89362005", "name": "Weight loss", "count": 5920},
    {"id": "91019004", "name": "Paresthesia", "count": 5815},
    {"id": "29857009", "name": "Chest pain", "count": 5676},
    {"id": "247381009", "name": "Limb stump pain", "count": 5145},
    {"id": "139146005", "name": "Back pain", "count": 4400},
    {"id": "274676007", "name": "Tingling of skin", "count": 2963},
    {"id": "247347003", "name": "Discomfort", "count": 2601},
    {"id": "65124004", "name": "Swelling", "count": 2597},
    {"id": "386705008", "name": "Lightheadedness", "count": 2004},
    {"id": "162310002", "name": "Morning headache", "count": 1973},
    {"id": "139621009", "name": "Ringing in ear", "count": 1906},
    {"id": "315018008", "name": "Dizzy spells", "count": 1815},
    {"id": "386661006", "name": "Fever", "count": 1780},
    {"id": "59621000", "name": "Essential hypertension", "count": 1607},
    {"id": "139224009", "name": "Palpitations", "count": 1559}
]

diseases = [
    {"id": "90688005", "name": "Chronic renal failure", "count": 16227},
    {"id": "155855008", "name": "Acute renal failure", "count": 14454},
    {"id": "45816000", "name": "Pyelonephritis", "count": 12811},
    {"id": "22298006", "name": "Myocardial infarction", "count": 3256},
    {"id": "46635009", "name": "Type 1 diabetes mellitus", "count": 2950},
    {"id": "313299006", "name": "Severe chronic obstructive pulmonary disease", "count": 2729},
]

medicines = [
    {"id": "314077", "name": "Lisinopril 20 MG Oral Tablet", "count": 10607},
    {"id": "313002", "name": "Sodium Chloride 9 MG/ML Injectable Solution", "count": 8850},
    {"id": "309309", "name": "Ciprofloxacin 500 MG Oral Tablet", "count": 5327},
    {"id": "211256", "name": "Alteplase 1 MG/ML Injectable Solution Activase", "count": 4836},
    {"id": "359383", "name": "Ciprofloxacin 500 MG 24 Hour Extended Release Tablet", "count": 4701},
    {"id": "348831", "name": "Oxygen 99.2 % Gas for Inhalation", "count": 4289},
    {"id": "238734", "name": "Protamine Sulfate 10 MG/ML Injectable Solution", "count": 4261},
    {"id": "856569", "name": "24 HR Propranolol Hydrochloride 80 MG Extended Release Capsule", "count": 3569},
    {"id": "311026", "name": "Insulin, Isophane, Human 100 UNT/ML Injectable Suspension Humulin N",
     "count": 3240},
    {"id": "858804", "name": "Enalapril Maleate 2.5 MG Oral Tablet", "count": 2844},
    {"id": "197770", "name": "Hydrochlorothiazide 50 MG Oral Tablet", "count": 2577},
    {"id": "197319", "name": "Allopurinol 100 MG Oral Tablet", "count": 2507},
    {"id": "832718", "name": "Potassium Chloride 8 MEQ Extended Release Tablet Klor-Con", "count": 2484},
    {"id": "198032", "name": "Nifedipine 10 MG Oral Capsule", "count": 2481},
    {"id": "316881", "name": "valsartan 160 MG", "count": 1772},
    {"id": "313988", "name": "Furosemide 40 MG Oral Tablet", "count": 1379},
    {"id": "51428", "name": "Insulin, Aspart, Human", "count": 1274},
    {"id": "866514", "name": "Metoprolol Tartrate 50 MG Oral Tablet", "count": 1265},
    {"id": "328906", "name": "Morphine 10 MG", "count": 1240},
    {"id": "153666", "name": "irbesartan 150 MG Oral Tablet Avapro", "count": 1124},
    {"id": "3827", "name": "Enalapril", "count": 919},
    {"id": "316153", "name": "Lisinopril 20 MG", "count": 859},
    {"id": "313996", "name": "Gentamicins 40 MG/ML Injectable Solution", "count": 814},
    {"id": "317403", "name": "Levofloxacin 500 MG", "count": 767},
    {"id": "198467", "name": "Aspirin 325 MG Enteric Coated Tablet", "count": 734},
    {"id": "314045",
     "name": "Insulin, Extended Zinc, Human 100 UNT/ML Injectable Suspension Humulin U Ultralente",
     "count": 660},
    {"id": "311036", "name": "Insulin, Regular, Human 100 UNT/ML Injectable Solution Humulin R", "count": 644},
    {"id": "261551", "name": "Lantus", "count": 629},
    {"id": "199247", "name": "glimepiride 4 MG Oral Tablet", "count": 606},
    {"id": "197737", "name": "Glyburide 1.25 MG Oral Tablet", "count": 590}
]

meta = [{"id": "223", "name": "First Name"},
        {"id": "224", "name": "Last Name"},
        {"id": "225", "name": "Gender"},
        {"id": "226", "name": "Date of Birth"},
        {"id": "227", "name": "Place"}]

symptom_mapping = {symptom["id"]: symptom["name"] for symptom in symptoms}
disease_mapping = {disease["id"]: disease["name"] for disease in diseases}
medication_mapping = {medication["id"]: medication["name"] for medication in medicines}
meta_mapping = {meta_attr["id"]: meta_attr["name"] for meta_attr in meta}

def get_all_patients(path):
    patients = []
    records = open(path)
    header = []

    for record in records:
        if not header:
            header = record.split(",")
            for item_idx in range(len(header)):
                if header[item_idx] == '222':
                    id_loc = item_idx
                    break
        else:
            patient_info = record.split(",")
            # patient_id = patient_info[-1][:-1]
            patient_id = patient_info[id_loc]
            curr_patient = patient.Patient(patient_id)
            curr_patient_diseases = {}
            curr_patient_symptoms = {}
            curr_patient_medications = {}
            for info_idx in range(len(header)):
                if header[info_idx] in disease_mapping:
                    curr_patient_diseases[header[info_idx]] = int(patient_info[info_idx])
                elif header[info_idx] in medication_mapping:
                    curr_patient_medications[header[info_idx]] = int(patient_info[info_idx])
                elif header[info_idx] in symptom_mapping:
                    curr_patient_symptoms[header[info_idx]] = int(patient_info[info_idx])
                elif header[info_idx] in meta_mapping: # TODO : check what is 222
                    if meta_mapping[header[info_idx]] == "First Name":
                        curr_patient.first_name = patient_info[info_idx]
                    elif meta_mapping[header[info_idx]] == "Last Name":
                        curr_patient.last_name = patient_info[info_idx]
                    elif meta_mapping[header[info_idx]] == "Gender":
                        curr_patient.gender = patient_info[info_idx]
                    elif meta_mapping[header[info_idx]] == "Date of Birth":
                        curr_patient.date_of_birth = patient_info[info_idx]
                    elif meta_mapping[header[info_idx]] == "Place":
                        curr_patient.place = patient_info[info_idx]

            curr_patient.diseases = curr_patient_diseases
            curr_patient.symptoms = curr_patient_symptoms
            curr_patient.medications = curr_patient_medications
            patients.append(curr_patient)

    return patients
