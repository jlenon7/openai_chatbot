from src.gpt import create_gpt
from src.streamlit import create_streamlit

gpt = create_gpt()
st = create_streamlit()

if "openai_model" not in st.session_state:
  st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
  st.session_state["messages"] = []

for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

if prompt := st.chat_input("Whats up?"):
  instructions = "answer the questions of the user in informal way"

  st.session_state.messages.append({"role":"user","content":prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

  with st.chat_message("assistant"):
    stream = gpt.chat.completions.create(
      model = st.session_state['openai_model'],
      messages = [
        {"role":"user","content":prompt},
        {"role":"system","content":instructions}
      ],
      stream=True
    )
    response = st.write_stream(stream)
    st.session_state.messages.append({"role":"assistant","content":response})
