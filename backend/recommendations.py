import numpy as np
from util import get_all_patients, disease_mapping, symptom_mapping
class Recommender(object):
    def __init__(self, path):
        self.patients = get_all_patients(path)

    def get_disease_recommendations(self, patient_ids, limit = -1):
        patients = []
        unique_diseases = set([])
        for id in patient_ids: # For every patient
            filtered_patient = [patient for patient in self.patients if patient.id == id][0] # Get Patient data
            unique_diseases.update([d for d in filtered_patient.diseases if filtered_patient.diseases[d] != 0]) # Update set of unique diseases encountered so far
            patients.append(filtered_patient) # Add patient

        unique_diseases = list(unique_diseases)
        patient_diseases = []
        # Create a matrix of patients (rows) and disease occurences (columns)
        for p in patients:
            patient_record = [0 for _ in unique_diseases]
            for disease_idx in range(len(unique_diseases)):
                if unique_diseases[disease_idx] in p.diseases:
                    patient_record[disease_idx] = p.diseases[unique_diseases[disease_idx]]
            patient_diseases.append(patient_record)
        # Get diseases with least absolute deviation from mean and their corresponding scores
        # Scoring mechanism - deviation of 0 is a 1.0 score and deviation of 1 is a 0.0 score
        [least_absdev_diseases, scored_absdevs] = self.get_best_score_combination(unique_diseases, patient_diseases, limit)

        # print least_absdev_diseases
        # print scored_absdevs
        recommended_diseases = self.format_for_marshalling(least_absdev_diseases, scored_absdevs, 'diseases')
        return recommended_diseases

    def get_symptom_recommendations(self, patient_ids, limit = -1):
        patients = []
        relevant_symptoms = set([])
        for id in patient_ids: # For every patient
            filtered_patient = [patient for patient in self.patients if patient.id == id][0] # Get Patient data
            relevant_symptoms.update([d for d in filtered_patient.symptoms if filtered_patient.symptoms[d] != 0]) # Update set of unique diseases encountered so far
            patients.append(filtered_patient) # Add patient

        relevant_symptoms = list(relevant_symptoms)
        patient_symptoms = []
        # Create a matrix of patients (rows) and symptom occurences (columns)
        for p in patients:
            patient_record = [0 for _ in relevant_symptoms]
            for symptom_idx in range(len(relevant_symptoms)):
                if relevant_symptoms[symptom_idx] in p.symptoms:
                    patient_record[symptom_idx] = p.symptoms[relevant_symptoms[symptom_idx]]
            patient_symptoms.append(patient_record)
        # Get diseases with least absolute deviation from mean and their corresponding scores
        # Scoring mechanism - deviation of 0 is a 1.0 score and deviation of 1 is a 0.0 score
        [least_absdev_symptoms, scored_absdevs] = self.get_best_score_combination(relevant_symptoms, patient_symptoms, limit)
        # print least_absdev_symptoms
        # print scored_absdevs
        recommended_symptoms = self.format_for_marshalling(least_absdev_symptoms, scored_absdevs, 'symptoms')
        return recommended_symptoms

    def get_best_score_combination(self, attribute_set, feature_set, limit):
        attribute_set = np.asarray(attribute_set)
        feature_set = np.asarray(feature_set, dtype='float64')
        normalized_feature_set = feature_set / feature_set.sum(axis=0)
        feature_set_deviations = np.sum(np.abs(normalized_feature_set - normalized_feature_set.mean(axis=0)), axis=0)
        if limit > len(attribute_set):
            limit = len(attribute_set)
        least_absdev_indices = feature_set_deviations.argsort()[:limit]
        max_val = feature_set_deviations[least_absdev_indices][-1]
        deviations_for_scoring = max_val - feature_set_deviations[least_absdev_indices] + 0.00001
        first_val = deviations_for_scoring[0]
        scored_absdevs = deviations_for_scoring * 1.0 / first_val
        least_absdev_features = attribute_set[least_absdev_indices]

        return least_absdev_features, scored_absdevs

    def format_for_marshalling(self,recommendations, scores, type):
        marshalled = []
        for idx in range(len(recommendations)):
            curr_obj = {"id" : recommendations[idx], "score" : scores[idx]}
            if type == 'symptoms':
                curr_obj["name"] = symptom_mapping[curr_obj["id"]]
            elif type == 'diseases':
                curr_obj["name"] = disease_mapping[curr_obj["id"]]
            marshalled.append(curr_obj)
        print marshalled
        return marshalled



if __name__ == "__main__":
    recommender = Recommender("testdata.csv")
    diseases = recommender.get_disease_recommendations(['1','2','3','4'], limit=3)
    symptoms = recommender.get_symptom_recommendations(['1', '2', '3', '4'], limit=5)
    # diseases = recommender.get_disease_recommendations(['1','2'], limit=3)
    # symptoms = recommender.get_symptom_recommendations(['1', '2'], limit=5)


