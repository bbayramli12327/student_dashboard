# app.py
import streamlit as st
import pandas as pd
from database import add_student, get_students, get_student
from services import calculate_grade, calculate_statistics

# Səhifə konfiqurasiyası
st.set_page_config(page_title="Student Performance Dashboard", layout="wide")

st.title("🎓 Student Performance Dashboard")

# --- 1. Tələbə Əlavə Etmə Bölməsi ---
st.subheader("➕ Yeni Tələbə Əlavə Et")
with st.form("add_student_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        student_name = st.text_input("Student Name")
    with col2:
        score = st.number_input("Score", min_value=0.0, max_value=100.0, step=1.0)
    
    submit_button = st.form_submit_button("Add Student")

if submit_button:
    if student_name.strip():
        success = add_student(student_name.strip(), score)
        if success:
            st.success(f"Tələbə '{student_name}' uğurla əlavə olundu!")
            st.rerun()
        else:
            st.error("Xəta baş verdi! Verilənlər bazasına qoşulmanı yoxlayın.")
    else:
        st.warning("Xahiş olunur tələbə adını daxil edin.")

st.divider()

# --- 2. Tələbə Axtarışı ---
st.subheader("🔍 Student Search")
search_query = st.text_input("Search Student by Name", placeholder="Tələbə adını daxil edin...")

if search_query.strip():
    students_data = get_student(search_query.strip())
else:
    students_data = get_students()

# --- 3. Statistikalar ---
st.subheader("📊 Statistikalar")
stats = calculate_statistics(students_data)

col_stat1, col_stat2, col_stat3, col_stat4 = st.columns(4)
col_stat1.metric("Total Students", stats["total_students"])
col_stat2.metric("Average Score", stats["average_score"])
col_stat3.metric("Highest Score", stats["highest_score"])
col_stat4.metric("Lowest Score", stats["lowest_score"])

st.divider()

# --- 4. Tələbə Siyahısını Göstərmək ---
st.subheader("📜 Student List")

if students_data:
    # Grade hesablanması
    formatted_data = []
    for item in students_data:
        formatted_data.append({
            "Name": item["name"],
            "Score": item["score"],
            "Grade": calculate_grade(item["score"])
        })
    
    df = pd.DataFrame(formatted_data)
    st.dataframe(df, use_container_width=True)
else:
    st.info("Heç bir tələbə tapılmadı.")
    