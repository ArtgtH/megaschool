import streamlit as st

from ml.gigachad import test_ai


def main():
    st.title("Proof of concept для сервиса авто")

    model = st.text_input("Модель автомобиля")

    age = st.number_input(
        label="Сколько лет автомобилю",
        min_value=0,
        step=1,
    )

    mileage = st.number_input("Пробег автомобиля")

    context = st.text_input("Дополнительная информация (например, ваш стиль вождения)")

    if st.button("Отправить запрос"):
        if model and context:
            res = test_ai(model, age, mileage, context)
            st.title("Результат")
            st.subheader(f"РАСХОДЫ НА ТОПЛИВО: {res.fuel}")
            st.subheader(f"РАСХОДЫ НА ТЕХ.ОБСЛУЖИВАНИЕ:: {res.maintenance}")
            st.subheader(f"ПРОЧИЕ РАСХОДЫ: {res.other}")
            st.subheader(f"ИТОГО: {res.other}")
            st.subheader(f"ОБЩАЯ АНАЛИТИКА: {res.fuel}")
        else:
            st.write("Пожалуйста, введите запрос перед отправкой.")


if __name__ == "__main__":
    main()
