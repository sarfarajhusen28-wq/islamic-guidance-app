import streamlit as st

st.set_page_config(page_title="Islamic Guidance & Quran App", page_icon="📖")

st.title("📖 Islamic Guidance, Hadith & Quran Finder")
st.write("Find authentic moral lessons, original Arabic Quranic Aayats, and Sahih Hadiths in your preferred language.")

# Comprehensive Multilingual Database with Original Arabic Quran Text & Translations
guidance_database = [
    {
        "topic_keys": [
            "dost", "dosti", "friendship", "brotherhood", "bhai", "jhagda", "naraz", "faith", "empathy", 
            "mustjina", "galat", "sahi", "karta", "mai", "hu", "kya", "karna", "roj", "yeh", "ye", "aur", "ho",
            "दोस्त", "झगड़ा", "भाई", "ईमान", "محبت", "دوستی", "بھائی", "معاملہ", "ناراض", "सत्य", "मित्रता", "दाजुभाइ"
        ],
        "quran": {
            "surah": "Surah Al-Hujurat",
            "ayah": "Ayah 10",
            "para": "Para 26",
            "arabic": "إِنَّمَا الْمُؤْمِنُونَ إِخْوَةٌ فَأَصْلِحُوا بَيْنَ أَخَيْكُمْ وَاتَّقُوا اللَّهَ لَعَلَّكُمْ تُرْحَمُونَ",
            "explanation": {
                "en": "The believers are but brothers, so make settlement between your brothers and fear Allah that you may receive mercy.",
                "ur": "تمام مومن آپس میں بھائی بھائی ہیں، لہٰذا اپنے دو بھائیوں کے درمیان صلح کرایا کرو اور اللہ سے ڈرو تاکہ تم پر رحم کیا جائے۔",
                "hindi": "सभी मोमिन आपस में भाई-भाई हैं, इसलिए अपने दो भाइयों के बीच सुलह कराया करो और अल्लाह से डरो ताकि तुम पर रहम किया जाए।",
                "roman_ur": "Tamam momin aapas mein bhai bhai hain, lihaza apne do bhaiyon ke darmiyan sulah karaya karo aur Allah se daro taake tum par raham kiya jaye.",
                "ne": "वास्तवमा सबै विश्वासीहरू आपसमा दाजुभाइ हुन्, त्यसैले तिमीहरू आफ्ना दाजुभाइहरू बीच मेलमिलाप गराऊ र अल्लाहसँग डराऊ ताकि तिमीहरूमाथि दया गरियोस्。"
            }
        },
        "hadiths": [
            {
                "number": "Sahih al-Bukhari (Book #2, Hadith #13)",
                "text": {
                    "en": "None of you truly believes until he wishes for his brother what he wishes for himself.",
                    "ur": "تم میں سے کوئی اس وقت تک مومن نہیں ہوتا جب تک وہ اپنے بھائی کے لیے وہی پسند نہ کرے جو اپنے لیے کرتا ہے۔",
                    "hindi": "तुम में से कोई उस वक्त तक मोमिन नहीं होता जब तक वह अपने भाई के लिए वही पसंद न करे जो अपने लिए करता है।",
                    "roman_ur": "Tum mein se koi us waqt tak momin nahi hota jab tak woh apne bhai ke liye wohi pasand na kare jo apne liye karta hai.",
                    "ne": "तपाईंहरू मध्ये कोही पनि तबसम्म पूर्ण विश्वासी बन्न सक्दैन जबसम्म उसले आफ्नो भाइका लागि पनि त्यही कुरा मन पराउँदैन जो उसले आफ्नै लागि मन पराउँछ。"
                }
            },
            {
                "number": "Sahih Muslim (Book #45, Hadith #6586)",
                "text": {
                    "en": "The believers in their mutual kindness, compassion, and sympathy are just like one body.",
                    "ur": "مومن آپس میں ایک دوسرے پر رحم کرنے، محبت کرنے اور شفقت کرنے میں ایک جسم کی طرح ہیں۔",
                    "hindi": "मोमिन आपस में एक दूसरे पर रहम करने, मोहब्बत करने और शिफकत करने में एक जिस्म की तरह हैं。",
                    "roman_ur": "Moman aapas mein aik dusre par raham karne, mohabbat karne aur shafqat karne mein aik jism ki tarah hain.",
                    "ne": "विश्वासीहरू आफ्नो आपसी दया, करुणा र सहानुभूतिमा एक शरीर जस्तै हुन्。"
                }
            },
            {
                "number": "Sahih al-Bukhari (Book #78, Hadith #60)",
                "text": {
                    "en": "It is not permissible for a Muslim to forsake his brother for more than three days.",
                    "ur": "کسی مسلمان کے لیے جائز نہیں کہ وہ اپنے بھائی سے تین دن سے زیادہ بول چال چھوڑ دے۔",
                    "hindi": "किसी मुसलमान के लिए जायज़ नहीं कि वह अपने भाई से तीन दिन से ज़्यादा बोल-चाल छोड़ दे।",
                    "roman_ur": "Kisi musalman ke liye jaiz nahi ke woh apne bhai se teen din se zyada bol chaal chor de.",
                    "ne": "कुनै पनि मुसलमानका लागि आफ्नो भाइसंग तीन दिनभन्दा बढी बोलचाल बन्द गर्नु जायज छैन。"
                }
            }
        ],
        "morals": {
            "en": "Islam strictly emphasizes preserving relationships, purity of actions, eliminating bad habits, and spreading mutual love.",
            "ur": "اسلام رشتوں کو جوڑنے، اعمال کی پاکیزگی، بری عادتوں کو چھوڑنے اور آپس میں محبت پھیلانے پر زور دیتا ہے۔",
            "hindi": "इस्लाम रिश्तों को जोड़ने, आमाल की पाकीज़गी, बुरी आदतों को छोड़ने और आपस में मोहब्बत फैलाने पर ज़ोर देता है。",
            "roman_ur": "Islam rishton ko jorne, amaal ki pakeezgi, buri aadton ko chorne aur aapas mein mohabbat phailane par zor deta hai.",
            "ne": "इस्लामले सम्बन्धहरू جوगाउन, कार्यहरूको शुद्धता, नराम्रा बानीहरू त्याग्न र आपसी प्रेम फैलाउन जोड दिन्छ।"
        }
    },
    {
        "topic_keys": [
            "pride", "arrogance", "ego", "ghamand", "takabbur", "ahankar", "ghamandi", "bada", "غرور", "تكبر", "घमण्ड", "अहंकार"
        ],
        "quran": {
            "surah": "Surah Al-Isra",
            "ayah": "Ayah 37",
            "para": "Para 15",
            "arabic": "وَلَا تَمْشِ فِي الْأَرْضِ مَرَحًا ۖ إِنَّكَ لَنْ تَخْرِقَ الْأَرْضَ وَلَنْ تَبْلُغَ الْجِبَالَ طُولًا",
            "explanation": {
                "en": "And do not walk upon the earth arrogantly. Indeed, you will never tear the earth apart [by walking], and you will never reach the mountains in height.",
                "ur": "اور زمین پر اتراتے ہوئے نہ چلو، بے شک تم نہ زمین کو پھڑ سکتے ہو اور نہ لمبائی میں پہاڑوں کو پہنچ سکتے ہو۔",
                "hindi": "और ज़मीन पर इतराते हुए न चलो, बेशक तुम न ज़मीन को फाड़ सकते हो और न लंबाई में पहाड़ों को पहुँच सकते हो।",
                "roman_ur": "Aur zameen par itratay huwe na chalo, be shak tum na zameen ko phaad saktay ho aur na lambaayi mein paharon ko pahunch saktay ho.",
                "ne": "र पृथ्वीमा घमण्ड गर्दै नहिँड, किनकि तिमीले न त पृथ्वी च्यात्न सक्छौ न उचाइमा पहाडहरूसम्मै पुग्न सक्छौ।"
            }
        },
        "hadiths": [
            {
                "number": "Sahih Muslim (Book #1, Hadith #74)",
                "text": {
                    "en": "He who has in his heart the weight of a mustard seed of pride shall not enter Paradise.",
                    "ur": "جس کے دل میں رائی کے دانے کے برابر بھی تکبر ہوگا، وہ جنت میں داخل نہیں ہوگا۔",
                    "hindi": "जिसके दिल में राई के दाने के बराबर भी तकब्बुर होगा, वह जन्नत में दाखिल नहीं होगा।",
                    "roman_ur": "Jis ke dil mein rai ke daane ke barabar bhi takabbur hoga, woh jannat mein dakhil nahi hoga.",
                    "ne": "जसको हृदयमा रायोको दाना बराबर पनि घमण्ड हुन्छ, ती व्यक्ति स्वर्गमा प्रवेश गर्ने छैनन्。"
                }
            },
            {
                "number": "Sahih al-Bukhari (Book #56, Hadith #826)",
                "text": {
                    "en": "Pride is disdaining the truth and contempt for people.",
                    "ur": "تکبر حق کو جھٹکنا اور لوگوں کو حقیر سمجھنا ہے۔",
                    "hindi": "तकब्बुर हक़ को झटकना और लोगों को हकीर समझना है।",
                    "roman_ur": "Takabbur haq ko jhatkna aur logon ko haqeer samajhna hai.",
                    "ne": "घमण्ड भनेको सत्यलाई अस्वीकार गर्नु र मानिसहरूलाई हेला गर्नु हो।"
                }
            }
        ],
        "morals": {
            "en": "Arrogance destroys spiritual growth; true honor lies in humility before Allah and His creation.",
            "ur": "تکبر روحانی ترقی کو تباہ کرتا ہے؛ اصل عزت اللہ اور اس کی مخلوق کے سامنے عاجزی اختیار کرنے میں ہے۔",
            "hindi": "तकब्बुर रूहानी तरक्की को तबाह करता है; असल इज़्ज़त अल्लाह और उसकी मखलूक के सामने عاجزی اختیار करने में है।",
            "roman_ur": "Takabbur roohani taraqi ko tabaah karta hai; asal izzat Allah aur us ki makhlooq ke samne aajzi ikhtiyar karne mein hai.",
            "ne": "घमण्डले आध्यात्मिक विकास नष्ट गर्छ; वास्तविक सम्मान अल्लाह र उसका सृष्टिका सामु नम्र हुनुमा छ।"
        }
    }
]

# Universal User Input
user_query = st.text_input("What problem or topic do you need guidance on? (Type in Hindi, Urdu, English, or Nepali)")

if st.button("Find Guidance"):
    if user_query:
        query_lower = user_query.lower()
        matched_item = None
        
        # Scan database for matching topics
        for item in guidance_database:
            for kw in item["topic_keys"]:
                if kw in query_lower:
                    matched_item = item
                    break
            if matched_item:
                break
        
        if not matched_item:
            matched_item = guidance_database[0]
            
        # Advanced script and language detector
        is_nepali = any('\u0900' <= c <= '\u097F' for c in query_lower)
        is_urdu_script = any('\u0600' <= c <= '\u06FF' for c in query_lower)
        
        # Check if Devangari script is used (indicates Hindi language when not Nepali)
        is_hindi_script = any('\u0900' <= c <= '\u097F' for c in query_lower) and not is_nepali
        
        # Roman Urdu / Hindi / English identifiers
        roman_words = ["mai", "hu", "hain", "kya", "karna", "karta", "galat", "sahi", "dost", "jhagda", "bhai", "naraz", "ho", "aur", "bana", "roj", "yeh", "ye", "kaise", "nahi", "hota"]
        is_roman = any(word in query_lower.split() for word in roman_words)

        # Map to precise language output dictionary keys
        if is_nepali:
            lang_key = "ne"
        elif is_urdu_script:
            lang_key = "ur"
        elif is_hindi_script or any(h_word in query_lower for h_word in ["kya", "hai", "kaise", "mein", "se", "par", "karna"]):
            lang_key = "hindi"
        elif is_roman:
            lang_key = "roman_ur"
        else:
            lang_key = "en"

        st.success("Guidance Found!")
        
        # 1. Moral Lesson First
        st.markdown("### 💡 Moral Lesson")
        st.write(matched_item["morals"][lang_key])
        
        # 2. Quranic Reference (With Original Arabic Text & Translation)
        if "quran" in matched_item:
            q = matched_item["quran"]
            st.markdown("### 📖 Mention in the Holy Quran")
            st.markdown(f"**Surah:** {q['surah']} | **Ayah:** {q['ayah']} | **Para:** {q['para']}")
            
            # Display Original Arabic Quran Verse (Right-to-left stylized styling)
            st.markdown(f"<p style='direction: rtl; font-size: 26px; font-family: Traditional Arabic, Amiri, sans-serif; text-align: right; color: #0d3b66;'><b>{q['arabic']}</b></p>", unsafe_allow_html=True)
            
            # Display Translation based on user language
            st.info(q["explanation"][lang_key])

        # 3. Authentic Hadiths Step-wise with Numbers
        st.markdown("### 📜 Authentic Hadiths (Sahih al-Bukhari & Sahih Muslim)")
        for idx, h in enumerate(matched_item["hadiths"], 1):
            st.markdown(f"**Step {idx}:**")
            st.info(h["text"][lang_key])
            st.markdown(f"**Hadith Reference:** {h['number']}")
            st.write("---")
            
    else:
        st.warning("Please type a topic or problem first.")