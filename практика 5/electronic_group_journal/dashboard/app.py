import os
import requests
import pandas as pd
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
st.set_page_config(page_title="Электронный журнал групп", page_icon="📚", layout="wide")
st.title("Электронный журнал учебных групп")
st.caption("Сводная информация об учебных группах, оценках и посещаемости")

base_url = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")
token = st.text_input("API-токен Django", value=os.getenv("API_TOKEN", ""), type="password")
if st.button("Загрузить статистику"):
    if not token:
        st.warning("Введите API-токен. Получить его можно через /api/token/.")
    else:
        try:
            response = requests.get(
                f"{base_url}/api/reports/stats/",
                headers={"Authorization": f"Token {token}"},
                timeout=10
            )
            response.raise_for_status()
            data = response.json()
            summary = data["summary"]
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Учебные группы", summary["groups_count"])
            c2.metric("Студенты", summary["students_count"])
            c3.metric("Количество оценок", summary["grades_count"])
            c4.metric("Средний балл", round(summary["average_grade"], 2))
            st.metric("Пропуски занятий", summary["absences_count"])
            st.subheader("Успеваемость по группам")
            if data["groups"]:
                st.dataframe(pd.DataFrame(data["groups"]), use_container_width=True)
            else:
                st.info("Пока нет данных по группам.")
        except requests.RequestException as exc:
            st.error(f"Не удалось получить данные API: {exc}")
