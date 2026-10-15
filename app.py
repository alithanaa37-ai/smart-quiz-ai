import os
import streamlit as st
import google.generativeai as genai

# إعداد الصفحة وتصميم الواجهة
st.set_page_config(
    page_title="SmartQuiz AI",
    page_icon="🤖",
    layout="centered"
)

st.title("🧠 SmartQuiz AI - مولد الأسئلة الذكي")
st.markdown("قم بإدخال أي نص تعليمي أو درس، وسيقوم الذكاء الاصطناعي بتوليد أسئلة امتحانات تلقائية مع الإجابات النموذجية!")

# إدخال المفتاح
api_key = st.text_input("أدخل مفتاح الـ API الخاص بك:", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
    except Exception as e:
        st.error(f"خطأ في إعداد المفتاح: {e}")
    
    # اختيار نوع الأسئلة وعددها
    col1, col2 = st.columns(2)
    with col1:
        num_questions = st.slider("عدد الأسئلة:", min_value=3, max_value=10, value=5)
    with col2:
        question_type = st.selectbox("نوع الأسئلة:", ["اختيار من متعدد (MCQ)", "صح وخطأ", "أسئلة مقالية"])

    # إدخال النص
    article_text = st.text_area("أدخل النص أو محتوى الدرس هنا:", height=200, placeholder="اكتب أو الصق النص هنا...")

    if st.button("🚀 توليد الأسئلة الآن", type="primary"):
        if not article_text.strip():
            st.warning("الرجاء إدخال نص أولاً!")
        else:
            with st.spinner("جاري تحليل النص وتوليد الأسئلة بواسطة الذكاء الاصطناعي..."):
                try:
                    # استخدام النموذج الثابت والمستقر
                    model = genai.GenerativeModel('gemini-1.0-pro')
                    
                    prompt = f"""
                    بناءً على النص التالي، قم بتوليد {num_questions} من نوع {question_type}.
                    اجعل الأسئلة واضحة واحترافية، وارفق مع كل سؤال الإجابة الصحيحة وشرحاً بسيطاً لها.
                    
                    النص:
                    {article_text}
                    """
                    
                    response = model.generate_content(prompt)
                    
                    st.success("تم توليد الأسئلة بنجاح!")
                    st.markdown("### النتائج:")
                    st.markdown(response.text)
                    
                except Exception as e:
                    st.error(f"حدث خطأ أثناء الاتصال بالذكاء الاصطناعي: {e}")
else:
    st.info("الرجاء إدخال المفتاح للمتابعة.")
