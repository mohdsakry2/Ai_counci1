
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="مجلس الذكاء الاصطناعي", page_icon="☕")
st.title("☕ مجلس الذكاء الاصطناعي (Ai Council)")

# الشريط الجانبي لمفتاح API
api_key = st.sidebar.text_input("أدخل مفتاح OpenRouter API:", type="password")

models = {
    "ChatGPT": "openai/gpt-4o-mini",
    "Gemini": "google/gemini-2.5-flash",
    "Claude": "anthropic/claude-3.5-sonnet",
    "DeepSeek": "deepseek/deepseek-chat"
}

query = st.text_area("أدخل السؤال أو الموضوع للنقاش:")

if st.button("إطلاق النقاش 🚀") and api_key and query:
    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)
    responses = {}
    
    st.subheader("📌 الجولة الأولى: الردود المباشرة")
    cols = st.columns(4)
    
    for idx, (name, model_id) in enumerate(models.items()):
        with cols[idx]:
            st.markdown(f"### {name}")
            try:
                res = client.chat.completions.create(
                    model=model_id,
                    messages=[{"role": "user", "content": query}]
                )
                text = res.choices[0].message.content
                responses[name] = text
                st.write(text)
            except Exception as e:
                st.error(f"خطأ: {e}")
