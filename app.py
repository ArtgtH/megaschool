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

    context = st.text_input("Дополнительная информация (например, ваш стиль вождения)")

    if st.button("Отправить запрос"):
        if model:
            res = test_ai(model, age, context)
            st.write(f"Результат: {res}")
        else:
            st.write("Пожалуйста, введите запрос перед отправкой.")


if __name__ == "__main__":
    main()
