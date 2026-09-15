import sqlite3
import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

# Initialize Gemini client
client = genai.Client()

def get_gemini_response(question, prompt):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=[prompt[0], question]
    )
    return response.text.strip()

def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

# System Prompt Context
prompt=[
    """
        You are an expert in converting English questions to SQL query!
        The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
        SECTION, MARKS.

        For example:
        Example 1 - How many entries of records are present?, 
        the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;

        Example 2 - Tell me all the students studying in Data Science class?, 
        the SQL command will be something like this SELECT * FROM STUDENT where CLASS="Data Science"; 

        CRITICAL: The output MUST NOT contain ``` or the word 'sql' in markdown block formatting. 
        Return raw SQL query text only.
    """
]

# Streamlit Page Config & Header
st.set_page_config(page_title="NL2SQL Query Assistant")
st.header("NL2SQL: Natural Language Database Query Engine")

question = st.text_input("Ask a question about the student database:", key="input")
submit = st.button("Generate & Run Query")

if submit and question:
    # 1. Generate SQL from Gemini
    sql_query = get_gemini_response(question, prompt)
    st.info(f"**Generated SQL Query:** '{sql_query}'")

    # 2. Query Database
    try:
        response_data = read_sql_query(sql_query, "student.db")
        st.subheader("Query Results")

        if response_data:
            for row in response_data:
                print(row)
                st.write(row)
        else:
            st.warning("No records found matching your query.")
    except Exception as e:
        st.error(f"SQL Execution Error: {e}")


