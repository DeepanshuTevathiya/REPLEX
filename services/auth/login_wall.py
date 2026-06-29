import streamlit as st
from services.persistence.exercise_repository import get_or_create_user

def render_login_wall():
    if st.session_state.get("user_id") is not None:
        return True

    st.markdown("""
<div style="display:flex; align-items:center; justify-content: center; gap: 0px;">
    <img src="https://iili.io/CR3tnSV.md.png" width="100">
    <h1 style="margin:0;">REPLEX</h1>
</div>
""", unsafe_allow_html=True)    
    st.markdown("## Your Realtime Ai Gym Trainer")
    st.space()

    st.markdown("<p style='margin-bottom: 0px; color: gray;'>Welcome! Please enter username to start.</p>", unsafe_allow_html=True)

    with st.form("Login form", clear_on_submit=False):
        username = st.text_input("Enter username", placeholder="Steven")
        submit_button = st.form_submit_button("Start session", width="stretch", key="start_button")

    st.divider()

    st.markdown("""
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:20px 0 28px;">

  <div style="background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.09);border-radius:10px;padding:14px 10px;text-align:center">
    <div style="font-size:20px;font-weight:600;color:#9D90FC">5</div>
    <div style="font-size:10px;color:rgba(240,238,248,.38);text-transform:uppercase;letter-spacing:.06em;margin-top:4px">Exercises</div>
  </div>

  <div style="background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.09);border-radius:10px;padding:14px 10px;text-align:center">
    <div style="font-size:20px;font-weight:600;color:#9D90FC">📐</div>
    <div style="font-size:10px;color:rgba(240,238,248,.38);text-transform:uppercase;letter-spacing:.06em;margin-top:4px">Body Angle</div>
  </div>

  <div style="background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.09);border-radius:10px;padding:14px 10px;text-align:center">
    <div style="font-size:20px;font-weight:600;color:#9D90FC">🎙️</div>
    <div style="font-size:10px;color:rgba(240,238,248,.38);text-transform:uppercase;letter-spacing:.06em;margin-top:4px">AI Voice</div>
  </div>

  <div style="background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.09);border-radius:10px;padding:14px 10px;text-align:center">
    <div style="font-size:20px;font-weight:600;color:#9D90FC">⚡</div>
    <div style="font-size:10px;color:rgba(240,238,248,.38);text-transform:uppercase;letter-spacing:.06em;margin-top:4px">Real-time</div>
  </div>

</div>
""", unsafe_allow_html=True)       
        
    st.write("<div style='text-align:center;'>Build with ❤️ by Deepanshu Tevathiya</div>",unsafe_allow_html=True)

    
    if submit_button:
        if not username:
            st.error("Please Enter Username!")
            return
        
        user = get_or_create_user(username)
        st.session_state["user_id"] = user["uid"]
        st.session_state["username"] = user["username"]


        st.rerun()
    return False