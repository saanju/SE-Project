import streamlit as st
import mysql.connector
import webbrowser

# Function to connect to MySQL database and insert user data
def signup(username, email, password):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='dbms',
            password='dbms',
            database='se'
        )
        cursor = conn.cursor()

        # Create the 'users' table if it does not exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL
            )
        """)

        # Insert data into the 'users' table
        cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
        conn.commit()

        st.success("Signup successful!")
        webbrowser.open_new("file:///C:/Users/ADMIN/Downloads/se%20project/SE/homepage.html")
    except Exception as e:
        st.error(f"Error during signup: {e}")
    finally:
        cursor.close()
        conn.close()

# Streamlit app
st.title("Signup")

# Form for signup
username = st.text_input("Username:")
email = st.text_input("Email:")
password = st.text_input("Password:", type="password")

if st.button("Sign Up"):
    signup(username, email, password)
