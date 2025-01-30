import streamlit as st

from ml.gigachad import test_ai


def main():
    st.title('Proof of concept для сервиса авто')

    model = st.text_input('Введите полностью модель вашей машины')

    age = st.number_input(
        label='Введите сколько лет вашей машине',
        min_value=0,
        step=1,
    )

    if st.button('Отправить запрос'):
        if model:
            res = test_ai(model, age)
            st.write(f'Результат: {res}')
        else:
            st.write('Пожалуйста, введите запрос перед отправкой.')


if __name__ == '__main__':
    main()
