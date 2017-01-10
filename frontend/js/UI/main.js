(function(){
  attributes =[
    { "id" :  "222" , "name" :   "id"  , "count" : 1 },
    { "id" :  "223" , "name" :   "First name"  , "count" : 1 },
    { "id" :  "224" , "name" :   "Last name"  , "count" : 1 },
    { "id" :  "225" , "name" :   "Gender"  , "count" : 1},
    { "id" :  "226" , "name" :   "Birth"  , "count" : 1 },
    { "id" :  "227" , "name" :   "location"  , "count" : 1 }
  ]
 diseases = [
  { "name" :  "Chronic renal failure" , "id" :   "90688005"  , "count" : 16227 },
  { "name" :  "Acute renal failure" , "id" :   "155855008"  , "count" : 14454 },
  { "name" :  "Pyelonephritis" , "id" :   "45816000"  , "count" : 12811 },
  { "name" :  "Hemorrhagic stroke monitoring" , "id" :   "417506008"  , "count" : 10856 },
  { "name" :  "Lethargy" , "id" :   "214264003"  , "count" : 6876 },
  { "name" :  "Hyperesthesia" , "id" :   "14151009"  , "count" : 6222 },
  { "name" :  "Paresthesia" , "id" :   "91019004"  , "count" : 5815 },
  { "name" :  "Limb stump pain" , "id" :   "247381009"  , "count" : 5145 },
  { "name" :  "Back pain" , "id" :   "139146005"  , "count" : 4400 },
  { "name" :  "Myocardial infarction" , "id" :   "22298006"  , "count" : 3256 },
  { "name" :  "Type 1 diabetes mellitus" , "id" :   "46635009"  , "count" : 2950 },
  { "name" :  "Severe chronic obstructive pulmonary disease" , "id" :   "313299006"  , "count" : 2729 },
  { "name" :  "Essential hypertension" , "id" :   "59621000"  , "count" : 1607 },
  { "name" :  "Acute renal failure syndrome" , "id" :   "14669001"  , "count" : 1351 },
  { "name" :  "Type 2 diabetes mellitus" , "id" :   "44054006"  , "count" : 1344 },
  { "name" :  "Phantom limb pain" , "id" :   "193115004"  , "count" : 1006 },
  { "name" :  "Congestive heart failure" , "id" :   "42343007"  , "count" : 912 },
  { "name" :  "Knameney stone" , "id" :   "95570007"  , "count" : 890 },
  { "name" :  "Cerebral infarction due to embolism of cerebral arteries" , "id" :   "195190007"  , "count" : 851 },
  { "name" :  "Cerebral hemorrhage" , "id" :   "274100004"  , "count" : 815 },
  { "name" :  "Acute myocardial infarction" , "id" :   "57054005"  , "count" : 808 },

  ];

  symptoms = [
  { "name" :  "Cough" , "id" :   "49727002"  , "count" : 14868 },
  { "name" :  "Foot pain" , "id" :   "47933007"  , "count" : 5928 },
  { "name" :  "Weight loss" , "id" :   "89362005"  , "count" : 5920 },
  { "name" :  "Lightheadedness" , "id" :   "386705008"  , "count" : 2004 },
  { "name" :  "Morning headache" , "id" :   "162310002"  , "count" : 1973 },
  { "name" :  "Ringing in ear" , "id" :   "139621009"  , "count" : 1906 },
  { "name" :  "Chest pain" , "id" :   "29857009"  , "count" : 5676 },
  { "name" :  "Breathlessness" , "id" :   "161937008"  , "count" : 647 },
  { "name" :  "Blurred vision" , "id" :   "240091000000105"  , "count" : 1018 },
  { "name" :  "Palpitations" , "id" :   "139224009"  , "count" : 1559 },
  { "name" :  "Fever" , "id" :   "386661006"  , "count" : 1780 },
  { "name" :  "Dizzy spells" , "id" :   "315018008"  , "count" : 1815 },
  { "name" :  "Tingling of skin" , "id" :   "274676007"  , "count" : 2963 },
  { "name" :  "Increased thirst" , "id" :   "249477003"  , "count" : 6545 },
  { "name" :  "Increased frequency of urination" , "id" :   "162116003"  , "count" : 6361 },
  { "name" :  "Dyspnea" , "id" :   "139201002" , "count" : 31062 },
  { "name" :  "Discomfort" , "id" :   "247347003"  , "count" : 2601 },
  { "name" :  "Swelling" , "id" :   "65124004"  , "count" : 2597 },
  ]

  medicines = [
  { "id" :   "314077"  , "name" :    "Lisinopril 20 MG Oral Tablet"   , "count" : 10607 },
  { "id" :   "313002"  , "name" :    "Sodium Chloride 9 MG/ML Injectable Solution"   , "count" : 8850 },
  { "id" :   "309309"  , "name" :    "Ciprofloxacin 500 MG Oral Tablet"   , "count" : 5327 },
  { "id" :   "211256"  , "name" :    "Alteplase 1 MG/ML Injectable Solution Activase"   , "count" : 4836 },
  { "id" :   "359383"  , "name" :    "Ciprofloxacin 500 MG 24 Hour Extended Release Tablet"   , "count" : 4701 },
  { "id" :   "348831"  , "name" :    "Oxygen 99.2 % Gas for Inhalation"   , "count" : 4289 },
  { "id" :   "238734"  , "name" :    "Protamine Sulfate 10 MG/ML Injectable Solution"   , "count" : 4261 },
  { "id" :   "856569"  , "name" :    "24 HR Propranolol Hydrochloride 80 MG Extended Release Capsule"   , "count" : 3569 },
  { "id" :   "311026"  , "name" :    "Insulin, Isophane, Human 100 UNT/ML Injectable Suspension Humulin N"   , "count" : 3240 },
  { "id" :   "858804"  , "name" :    "Enalapril Maleate 2.5 MG Oral Tablet"   , "count" : 2844 },
  { "id" :   "197770"  , "name" :    "Hydrochlorothiazide 50 MG Oral Tablet"   , "count" : 2577 },
  { "id" :   "197319"  , "name" :    "Allopurinol 100 MG Oral Tablet"   , "count" : 2507 },
  { "id" :   "832718"  , "name" :    "Potassium Chloride 8 MEQ Extended Release Tablet Klor-Con"   , "count" : 2484 },
  { "id" :   "198032"  , "name" :    "Nifedipine 10 MG Oral Capsule"   , "count" : 2481 },
  { "id" :   "316881"  , "name" :    "valsartan 160 MG"   , "count" : 1772 },
  { "id" :   "313988"  , "name" :    "Furosemide 40 MG Oral Tablet"   , "count" : 1379 },
  { "id" :   "51428"  , "name" :    "Insulin, Aspart, Human"   , "count" : 1274 },
  { "id" :   "866514"  , "name" :    "Metoprolol Tartrate 50 MG Oral Tablet"   , "count" : 1265 },
  { "id" :   "328906"  , "name" :    "Morphine 10 MG"   , "count" : 1240 },
  { "id" :   "153666"  , "name" :    "irbesartan 150 MG Oral Tablet Avapro"   , "count" : 1124 },
  { "id" :   "3827"  , "name" :    "Enalapril"   , "count" : 919 },
  { "id" :   "316153"  , "name" :    "Lisinopril 20 MG"   , "count" : 859 },
  { "id" :   "313996"  , "name" :    "Gentamicins 40 MG/ML Injectable Solution"   , "count" : 814 },
  { "id" :   "317403"  , "name" :    "Levofloxacin 500 MG"   , "count" : 767 },
  { "id" :   "198467"  , "name" :    "Aspirin 325 MG Enteric Coated Tablet"   , "count" : 734 },
  { "id" :   "314045"  , "name" :    "Insulin, Extended Zinc, Human 100 UNT/ML"   , "count" : 660 },
  { "id" :   "311036"  , "name" :    "Insulin, Regular, Human 100 UNT/ML Injectable"   , "count" : 644 },
  { "id" :   "261551"  , "name" :    "Lantus"   , "count" : 629 },
  { "id" :   "199247"  , "name" :    "glimepiride 4 MG Oral Tablet"   , "count" : 606 },
  { "id" :   "197737"  , "name" :    "Glyburide 1.25 MG Oral Tablet"   , "count" : 590 },
  { "id" :   "315562"  , "name" :    "Captopril 50 MG"   , "count" : 366 },
  { "id" :   "237178"  , "name" :    "Theophylline 100 MG Extended Release Tablet"   , "count" : 361 },
  { "id" :   "866047"  , "name" :    "28 ACTUAT salmeterol 0.05 MG/ACTUAT Dry Powder Inhaler Serevent"   , "count" : 331 },
  { "id" :   "312615"  , "name" :    "Prednisone 20 MG Oral Tablet"   , "count" : 313 },
  { "id" :   "311450"  , "name" :    "Mannitol 250 MG/ML Injectable Solution"   , "count" : 313 }
  ];

  var dataCallBack = function(){
        startVis(dataset);
  };

  d3.csv("http://localhost:5000/getAllData", function(csv) {
       dataset= csv.slice(0);
       loadAttributSelectors(dataset);
       dataCallBack();
  });

})();