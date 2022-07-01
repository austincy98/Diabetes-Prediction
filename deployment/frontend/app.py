import streamlit as st
import requests

st.title("Aplikasi Prediksi Diabetes")
HighChol_format = {0:"no high cholesterol",1:"High cholesterol"}
def hichol_format(option):
        return HighChol_format[option]
        
HighBP_format = {0:"no high BP",1:"high BP"}
def highbp_format(option):
        return HighBP_format[option]

CholCheck_format = {0:"no cholesterol check in 5 years",1:"yes cholesterol check in 5 years"}
def cholcheck_format(option):
        return CholCheck_format[option]

Smoke_format = {0:"no",1:"yes"}
def smk_format(option):
        return Smoke_format[option]

Stroke_format = {0:"no",1:"yes"}
def stroke_format(option):
        return Smoke_format[option]

Sex_format = {0:"female",1:"male"}
def sex_format(option):
        return Sex_format[option]

Age_format = {1:"Age 18 - 24",2:"Age 25 to 29", 3:"Age 30 to 34", 4:"Age 35 to 39", 5:"Age 40 to 44", 6:"Age 45 to 49", 7:"Age 50 to 54", 8:"Age 55 to 59", 9:"Age 60 to 64",10:"Age 65 to 69", 11:"Age 70 to 74", 12:"Age 75 to 79", 13:"Age 80 or older"}
def age_format(option):
        return Age_format[option]

Income_format = {1:"Less than $10,000",2:"$10,000 to less than $15,000", 3:"$15,000 to less than $20,000", 4:"$20,000 to less than $25,000", 5:"$25,000 to less than $35,000", 6:"$35,000 to less than $50,000", 7:"$50,000 to less than $75,000", 8:"$75,000 or more"}
def income_format(option):
        return Income_format[option]

BMI = st.number_input("BMI", min_value=1)
HighChol = st.selectbox("HighChol", options=list(HighChol_format.keys()),format_func=hichol_format)
HighBP = st.selectbox("HighBP", options=list(HighBP_format.keys()),format_func=highbp_format)
CholCheck = st.selectbox("CholCheck", options=list(CholCheck_format.keys()),format_func=cholcheck_format)
Smoke = st.selectbox("Have you smoked at least 100 cigarettes in your entire life?", options=list(Smoke_format.keys()),format_func=smk_format)
Stroke = st.selectbox("Stroke", options=list(Smoke_format.keys()),format_func=smk_format)
HeartDiseaseorAttack = st.selectbox("coronary heart disease (CHD) or myocardial infarction (MI) ", options=list(Smoke_format.keys()),format_func=smk_format)
PhysActivity = st.selectbox("physical activity in past 30 days", options=list(Smoke_format.keys()),format_func=smk_format)
Fruits = st.selectbox("Consume Fruit 1 or more times per day", options=list(Smoke_format.keys()),format_func=smk_format)
Veggies = st.selectbox("Consume Vegetables 1 or more times per day", options=list(Smoke_format.keys()),format_func=smk_format)
HvyAlcoholConsump= st.selectbox("Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week)", options=list(Smoke_format.keys()),format_func=smk_format)
AnyHealthcare= st.selectbox("Have any kind of health care coverage, including health insurance, prepaid plans such as HMO, etc", options=list(Smoke_format.keys()),format_func=smk_format)
NoDocbcCost= st.selectbox("Was there a time in the past 12 months when you needed to see a doctor but could not because of cost?", options=list(Smoke_format.keys()),format_func=smk_format)
GenHlth = st.number_input("Would you say that in general your health is: scale 1-5 1 = excellent 2 = very good 3 = good 4 = fair 5 = poor", min_value=1,max_value=5)
MentHlth=st.number_input("Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good?", min_value=1,max_value=30)
PhysHlth = st.number_input("Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good?", min_value=1,max_value=30)
DiffWalk = st.selectbox("Do you have serious difficulty walking or climbing stairs?", options=list(Stroke_format.keys()),format_func=smk_format)
Sex = st.selectbox("Sex", options=list(Sex_format.keys()),format_func=sex_format)
Age = st.selectbox("Age", options=list(Age_format.keys()),format_func=age_format)
Income = st.selectbox("Income", options=list(Income_format.keys()),format_func=income_format)

# inference
data = {'BMI':BMI,
        'HighBP':HighBP,
        'HighChol':HighChol,
        'CholCheck': CholCheck,
        'Smoker':Smoke,
        'Stroke':Stroke, 
        'HeartDiseaseorAttack':HeartDiseaseorAttack,
        'PhysActivity':PhysActivity,
        'Fruits' : Fruits,
        'Veggies' : Veggies,
        'HvyAlcoholConsump' : HvyAlcoholConsump,
        'AnyHealthcare' : AnyHealthcare,
        'NoDocbcCost' : NoDocbcCost,
        'GenHlth' : GenHlth,
        'MentHlth' : MentHlth,
        'PhysHlth' : PhysHlth,
        'DiffWalk' : DiffWalk,
        'Sex' : Sex,
        'Age' : Age,
        'Income' : Income}
        

URL1 = "https://austin-ml2-backend2.herokuapp.com/predict_ada"
URL2 = "https://austin-ml2-backend2.herokuapp.com/predict_rf"

# komunikasi
if st.button('Predict ADA'):
        r = requests.post(URL1, json=data)
        res = r.json()
        if res['code'] == 200:
                st.title(res['result']['classes'])

if st.button('Predict RF'):
        r = requests.post(URL2, json=data)
        res = r.json()
        if res['code'] == 200:
                st.title(res['result']['classes'])
