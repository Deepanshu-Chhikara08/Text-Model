from openai import OpenAI
import streamlit as st

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"
)

st.title("Text Model")
prompt = st.text_input("Enter Prompt")

completion = client.chat.completions.create(
  model="meta/llama-3.1-405b-instruct",
  messages=[{"role":"user","content":prompt}],
  temperature=0.2,
  top_p=0.7,
  max_tokens=1024,
  stream=True
)

accumulated_text = ""

for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    accumulated_text += chunk.choices[0].delta.content
    

st.write(accumulated_text)
