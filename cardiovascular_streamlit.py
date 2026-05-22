import streamlit as st
import requests

API_URL = 'https://fast-api-1-r596.onrender.com/Predict-cardio'

st.header('Cardiovascular Disease Prediction system')
st.subheader('Using Logistic Regression')

# 'age_years', 'height(55-250)', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke',
# 'alco', 'active'

# age = st.text_input('Age', placeholder = 'Enter your age(25-66)')

# code for creating sidebar
age = st.sidebar.slider(
    'Age',
    min_value = 25,
    max_value = 66,
    value = 25,
    step = 1
)

height = st.sidebar.slider(
    'Height',
    min_value = 55,
    max_value = 250,
    value = 55,
    step = 1
)

weight = st.sidebar.slider(
    'Weight',
    min_value = 10,
    max_value = 200,
    value = 10,
    step = 1
)

ap_hi = st.sidebar.slider(
    'Systolic blood pressure',
    min_value = 90,
    max_value = 200,
    value = 90,
    step = 1
)

ap_lo = st.sidebar.slider(
    'Diastolic blood pressure',
    min_value = 40,
    max_value = 90,
    value = 40,
    step = 1
)

cholesterol_options = {1: 'Healthy', 2: 'Mild', 3: 'High cholesterol'}
cholestrol = st.sidebar.radio(
    'Cholesterol',
    options = list(cholesterol_options.keys()),
    format_func = lambda x: cholesterol_options.get(x)
)

gluc_options = {1: 'Healthy', 2: 'Mild', 3: 'High glucose'}
glucose = st.sidebar.radio(
    'Glucose',
    options = list(gluc_options.keys()),
    format_func = lambda x: gluc_options.get(x)
)

smoke_options = {0: 'Does not smoke', 1: 'Does smoke'}
smoke = st.sidebar.radio(
    'Smoke',
    options = list(smoke_options.keys()),
    format_func = lambda x: smoke_options.get(x)
)

alcohol_options = {0: 'Does not drink Alcohol', 1: 'Does drink alcohol'}
alcohol = st.sidebar.radio(
    'Alcohol',
    options = list(alcohol_options.keys()),
    format_func = lambda x: alcohol_options.get(x)
)

active_options = {0: 'Does not PA', 1: 'Does PA'}
active = st.sidebar.radio(
    'Physical Activities',
    options = list(active_options.keys()),
    format_func = lambda x: active_options.get(x)
)

# ## Predict Button
# if st.button('Predict Cardio'):
#     input_data = pd.DataFrame([[age, height, weight, ap_hi, ap_lo, cholestrol, glucose, smoke, alcohol, active
#     ]], columns = features)
#     # Feature Scaling
#     input_scaler = scaler.transform(input_data)
#     prediction = model.predict(input_scaler)

#     if prediction[0] == 0:
#         st.write('You are not at risk of cardiovascular disease.')
#         st.warning('Maintain a healthy lifestyle to keep your heart healthy! 😊')
#     else:
#         st.write('You are at risk of cardiovascular disease.')
#         st.error('Please consult a healthcare professional for further evaluation and advice🥲.')

#     st.title('Visualization')
#     st.subheader('Confusion Matrix')

#     fig, ax = plt.subplots(figsize = (5, 4))
#     sns.heatmap(cm, annot = True, fmt = '.0f', xticklabels=['Predicted Healthy [0]', 'Predicted Unhealthy [1]'],
#                                                yticklabels=['Actual Healthy [0]', 'Actual Unhealthy [1]'], cmap = 'Blues', ax = ax)
#     st.pyplot(fig)

#     st.subheader('Classification Report')
#     #st.text(cr)

#     cr_df = pd.DataFrame(cr).transpose()
#     st.dataframe(cr_df.style.format(precision = 2))
#     #st.table(cr_df)

if st.button('Predict Cardio'):
    payload = {
        'age_years': age,
        'height': height,
        'ap_hi' : ap_hi,
        'ap_lo': ap_lo,
        'cholestrol': cholestrol,
        'gluc': glucose,
        'smoke': smoke,
        'alco': alcohol,
        'active': active
    }
# requests -> Successful -> status_code -> 200
    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            result = response.json()

            if result['Prediction_status'] ==0:
                st.write('No Cardio Disease Found!')
                st.success('patient is likely to be Healthy😊😊.')
            else:
                st.write('Cardio Disease Found!')
                st.warning('patient is likely to be unhealthy🥲.')   
        else:
            st.error(f'Status_code: {response.status_code} Error.')
    except requests.exceptions.RequestException:
        st.error('API Error, API Loading Failed!!') 