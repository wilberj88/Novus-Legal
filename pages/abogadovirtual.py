import streamlit as st
import numpy as np
import random
import time

st.title('Novus legal ⚖️ by Novus Atento 🤖')

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["user"]):
        st.markdown(message["👋Bienvenido a Novus legal ⚖️: pregúntame lo que quieras sobre tu caso"])
# React to user input
if prompt := st.chat_input("Dímelo de una"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        assistant_response = random.choice(
            [
                "Su consulta está ahora en las mejores manos, en breve enviamos reporte de consulta jurídica",
                "Claro que sí, cuente con mi apoyo jurídico en todo su proceso judicial",
                "Por supuesto que sí, estoy para defender todos tus derechos, cuentas conmigo",
            ]
        )
        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.1)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    
