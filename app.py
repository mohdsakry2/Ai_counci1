import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="مجلس الذكاء الاصطناعي", page_icon="☕", layout="wide")
st.title("☕ مجلس الذكاء الاصطناعي (AI Council)")

# الشريط الجانبي لمفتاح API
api_key = st.sidebar.text_input("أدخل مفتاح OpenRouter API:", type="password")

models = {
    "Gemini": "google/gemini-2.0-flash-lite-001:free",
    "Llama": "meta-llama/llama-3.3-70b-instruct:free",
    "DeepSeek": "deepseek/deepseek-r1:free"
}

prompt = st.text_area("أدخل السؤال أو الموضوع للنقاش:")

if st.button("🚀 إطلاق النقاش"):
    if not api_key:
        st.error("يرجى إدخال مفتاح OpenRouter API في الشريط الجانبي لتشغيل التطبيق!")
    elif not prompt.strip():
        st.warning("يرجى كتابة موضوع أو سؤال للنقاش!")
    else:
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
        )
        
        st.write("---")
        for name, model_id in models.items():
            st.subheader(f"🗣️ {name}")
            with st.spinner(f"جاري إحضار رد {name}..."):
                try:
                    response = client.chat.completions.create(
                        model=model_id,
                        messages=[
                            {"role": "user", "content": prompt}
                        ]
                    )
                    st.success(response.choices[0].message.content)
                except Exception as e:
                    st.error(f"خطأ أثناء الاتصال بـ {name}: {e}")
