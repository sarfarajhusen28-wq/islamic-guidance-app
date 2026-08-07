import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(
    page_title="Islamic Guidance & Quran App",
    page_icon="📖",
    layout="centered"
)

st.title("📖 Islamic Guidance, Hadith & Quran Finder")
st.write("Ask any question or state any topic to receive authentic guidance from the Holy Quran, Sahih al-Bukhari, and Sahih Muslim in your preferred language.")

# Sidebar for API Key configuration
st.sidebar.header("⚙️ Configuration")
api_key = st.sidebar.text_input("Enter your Google Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    # Initialize the Gemini model for dynamic Islamic knowledge retrieval
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.sidebar.warning("Please enter your Gemini API key in the sidebar to enable unlimited searches across thousands of Islamic topics.")

# Universal User Input
user_query = st.text_input("What problem or topic do you need guidance on? (Type in Hindi, Urdu, English, Roman Urdu, or Nepali)")

if st.button("Find Guidance"):
    if not api_key:
        st.error("Please enter your Gemini API Key in the sidebar first.")
    elif not user_query:
        st.warning("Please type a topic or question first.")
    else:
        with st.spinner("Searching the Holy Quran, Sahih al-Bukhari, and Sahih Muslim..."):
            try:
                # Prompt engineering to fetch authentic primary sources dynamically for any question
                prompt = f"""
                You are an authentic Islamic knowledge assistant. The user is asking a question or seeking guidance on: "{user_query}".
                
                Provide a comprehensive and accurate response sourced strictly from:
                1. The Holy Quran
                2. Sahih al-Bukhari
                3. Sahih Muslim
                
                Detect the language or script of the user's query (English, Hindi, Urdu, Nepali, or Roman Urdu/Hindi) and reply in that exact same language/script style.
                
                Format your response cleanly using these exact sections with markdown:
                
                ### 💡 Moral Lesson
                [Provide a concise spiritual and moral lesson based on Islamic teachings regarding this query]
                
                ### 📖 Mention in the Holy Quran
                **Surah:** [Surah Name] | **Ayah:** [Ayah Number] | **Para:** [Para Number]
                
                <p style='direction: rtl; font-size: 24px; font-family: Traditional Arabic, Amiri, sans-serif; text-align: right; color: #0d3b66;'><b>[Original Arabic Text of the Ayah]</b></p>
                
                **Translation:** [Translation in user's language]
                
                ### 📜 Authentic Hadiths (Sahih al-Bukhari & Sahih Muslim)
                **Step 1:**
                > [Hadith text translated in user's language]
                **Hadith Reference:** [Sahih al-Bukhari or Sahih Muslim book/hadith number]
                ---
                **Step 2:**
                > [Second Hadith text translated in user's language]
                **Hadith Reference:** [Sahih al-Bukhari or Sahih Muslim book/hadith number]
                """
                
                response = model.generate_content(prompt)
                
                st.success("Guidance Found!")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
                
