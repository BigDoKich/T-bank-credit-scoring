import streamlit as st
import requests

st.title('Credit Scoring App')
st.write("Введите данные клиента:")

with st.form('Подать заявку'):
    gender = st.selectbox("Пол", ["Мужчина", "Женщина"])
    age = st.slider("Возраст", 18, 100, 18)
    car_own = st.checkbox("Наличие автомобиля")
    work = st.checkbox("Наличие официальной работы")
    high_edu = st.checkbox("Наличие высшего образования")
    income = st.number_input("Официальный доход", min_value=0.0, value=0.0)

    gender_bool = True if gender == "Male" else False
    
    submit = st.form_submit_button('Подать заявку')

if submit:

    data = {
        "gender": gender_bool,
        "age": age,
        "car_own": car_own,
        "work": work,
        "income": income,
        "high_edu": high_edu
    }

    try:
        response = requests.post(
            "http://localhost:8000/score",
            json=data
        )

        result = response.json()

        if result["approved"]:
            st.success("Кредит одобрен ✅")
        else:
            st.error("Кредит отклонён ❌")

    except Exception as e:
        st.error("Ошибка подключения к API")
        st.write(e)



