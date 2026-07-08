import streamlit as st

st.title("Echo Chamber")
st.write("Fill in your details below and press the Transmit button to send your message.")

name = st.text_input("Enter your Name")
message = st.text_input("Enter your Message")

if st.button("Transmit"):

    if name.strip() == "":
        st.error("Please provide your name.")

    elif message.strip() == "":
        st.warning("Please type a message to transmit.")

    else:
        st.success(
            f"Transmission successful! Greetings, {name}. We received your message: {message}"
        )

        message_length = len(message)
        estimated_tokens = message_length / 4

        st.info(
            f"System Check:Your message will consume approximately {estimated_tokens:.2f} tokens from our context window"
        )