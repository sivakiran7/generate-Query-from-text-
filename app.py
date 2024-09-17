from dotenv import load_dotenv
load_dotenv()##take env variables

import streamlit as st
import os
import sqlite3

import google.generativeai  as genai

##config the key
genai.configure(api_key=os.getenv("google_api_key"))


##create a function to load genai model

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

##function to get query from database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows



##define the prompt
prompt=[
    """
    you are an expert in converting english questions to sql code
    the sql database has the name STUDENT nd has the following columns -NAME,
    CLASS,SECTION /n/n For example 1 - How many entries of records are present 
    in the sql command will be something like these SELECT COUNT(*) FROM STUDENT;
    also the sql code should not have ''' in the beginning or end and sql word in output
    For example 2- How many students are from the data science
    in the sql command will be something like these SELECT FROM STUDENT WHERE CLASS="datascience";
    also the sql code should not have ''' in the beginning or end and sql word in output


    """
]

##streamlit app

st.set_page_config(page_title="text to sql query")
st.header("Gemini pro sql query")

question=st.text_input("input: ",key="input")

submit=st.button("Ask the question")

#if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"student.db")
    st.subheader("the response is")
    for row in response:
        print(row)
        st.header(row)