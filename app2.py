import streamlit as st
import pickle
from datetime import datetime
startTime = datetime.now()

filename = "model2.sv"
model = pickle.load(open(filename, 'rb'))
# otwieramy wcześniej wytrenowany model

sex_d = {0: "Kobieta", 1: "Mężczyzna"}
chestpaintype_d = {0: "ATA", 1: "NAP", 2: "ASY", 3: "TA"}
restingecg_d = {0: "Normal", 1: "ST", 2: "LVH"}
exerciseangina_d = {0: "Nie", 1: "Tak"}
st_slope_d = {0: "Dolne", 1: "Płaskie", 2: "Górne"}
fastingbs_d = {0: "Nie", 1: "Tak"}

def main():
    st.set_page_config(page_title="Ryzyko ataku serca")
    overview = st.container()
    left, right = st.columns(2)
    prediction = st.container()

    st.image("https://upload.wikimedia.org/wikipedia/commons/4/4a/AMI_scheme.png")  # grafika

    with overview:
        st.title("Predykcja dla ataku serca")

    with left:
        sex_radio = st.radio("Płeć", list(sex_d.keys()), format_func=lambda x: sex_d[x])
        chestpaintype_radio = st.radio("Rodzaj bólu w klatce piersiowej", list(chestpaintype_d.keys()), format_func=lambda x: chestpaintype_d[x])
        restingecg_radio = st.radio("EKG spoczynkowe", list(restingecg_d.keys()), format_func=lambda x: restingecg_d[x])
        exerciseangina_radio = st.radio("Dusznica bolesna wysiłkowa", list(exerciseangina_d.keys()), format_func=lambda x: exerciseangina_d[x])
        st_slope_radio = st.radio("Nachylenie odcinka ST", list(st_slope_d.keys()), format_func=lambda x: st_slope_d[x])
        fastingbs_radio = st.radio("BS na czczo", list(fastingbs_d.keys()), format_func=lambda x: fastingbs_d[x])
        #embarked_radio = st.radio("Port zaokrętowania", list(embarked_d.keys()), index=2, format_func=lambda x: embarked_d[x])
    
    with right:
        age_slider = st.slider("Wiek", value=50, min_value=18, max_value=90)
        restingbp_slider = st.slider("Ciśnienie tętnicze spoczynkowe", min_value=0, max_value=200, value=120)
        cholesterol_slider = st.slider("Cholesterol", min_value=0, max_value=650, value=100)
        maxhr_slider = st.slider("Maksymalne tętno", min_value=55, max_value=250, value=60)
        oldpeak_slider = st.slider("Szczytowe", min_value=-5, max_value=10, value=0)
        #fare_slider = st.slider("Cena biletu", min_value=0, max_value=600, value=50, step=1)

    data = [[sex_radio, chestpaintype_radio, restingecg_radio, exerciseangina_radio, st_slope_radio, fastingbs_radio, age_slider, restingbp_slider, cholesterol_slider, maxhr_slider, oldpeak_slider]]
    survival = model.predict(data)
    s_confidence = model.predict_proba(data)

    with prediction:
        st.subheader("Czy dana osoba będzie miała atak serca?")
        st.subheader("Tak" if survival[0] == 1 else "Nie")
        st.write("Pewność predykcji {0:.2f} %".format(s_confidence[0][survival][0] * 100))

if __name__ == "__main__":
    main()

