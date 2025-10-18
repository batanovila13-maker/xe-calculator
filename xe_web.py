import streamlit as st

st.set_page_config(page_title="Хлебные единицы", page_icon="🍞", layout="centered")

st.title("🍞 Калькулятор Хлебных Единиц (ХЕ)")
st.write("Рассчитывает количество ХЕ по углеводам, белкам и жирам")

carbs = st.number_input("Углеводы (г):", min_value=0.0, step=0.1, placeholder="Введите количество")
protein = st.number_input("Белки (г):", min_value=0.0, step=0.1, placeholder="Введите количество")
fat = st.number_input("Жиры (г):", min_value=0.0, step=0.1, placeholder="Введите количество")

if st.button("Рассчитать ХЕ", use_container_width=True):
    calories = (carbs * 4) + (protein * 4) + (fat * 9)
    xe_carbs = carbs / 10
    xe_total = calories / 100

    st.success("✅ Результаты:")
    st.metric("Общая калорийность", f"{calories:.1f} ккал")
    st.metric("ХЕ по углеводам", f"{xe_carbs:.2f}")
    st.metric("ХЕ по калорийности", f"{xe_total:.2f}")

st.markdown("---")
st.caption("Формулы: 10 г углеводов = 1 ХЕ | 100 ккал = 1 ХЕ")
st.caption("1 г белка = 4 ккал, 1 г жира = 9 ккал")
