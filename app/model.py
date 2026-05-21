# Binary file to share ML code
import joblib

MODEL_PATH = 'models/cardio_model.pkl'
SCALER_PATH = 'models/cardio_scaler.pkl'

def load_model_scaler():
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    return model, scaler




# import pandas as pd
# import joblib
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.preprocessing import StandardScaler

# df = pd.read_csv('data/Cardiovascular_Disease.csv')

# # convert age from days to years
# df['age_years'] = (df['age'] / 365.25).round(1)
# df_sample = (df['ap_hi'].between(90, 200)) & (df['ap_lo'].between(40, 90))
# df = df[df_sample]

# MODEL_PATH = 'models/cardio_model.pkl'
# SCALER_PATH = 'models/cardio_scaler.pkl'

# def predict_cardio():
#     features = ['age_years', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke',
#                  'alco', 'active']
#     target = 'cardio'
    
#     X = df[features]
#     Y = df[target]

#     X_train, X_test, Y_train, Y_test = train_test_split(
#     X, Y, test_size = 0.2, random_state = 42, stratify = Y
# )
    
#     scaler = StandardScaler()
#     X_train_scale = scaler.fit_transform(X_train)
#     X_test_scale = scaler.transform(X_test)

#     model = LogisticRegression(solver = 'liblinear', random_state = 42,
#                                 class_weight = 'balanced')
#     model.fit(X_train_scale, Y_train)
#     model.predict(X_test_scale)

#     joblib.dump(model, MODEL_PATH)
#     joblib.dump(scaler, SCALER_PATH)


#     return model, scaler