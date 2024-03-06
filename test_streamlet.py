import streamlit as st

# Create a title for the app
st.title("My Streamlit App")

# Add a text input field
user_input = st.text_input("Enter some text")

# Display the input text
st.write("You entered:", user_input)

# Add a button
button_clicked = st.button("Click me")

# Execute some action when the button is clicked
if button_clicked:
    st.write("Button clicked!")