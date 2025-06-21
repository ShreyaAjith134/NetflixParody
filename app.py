import streamlit as st
import random
import datetime
import base64
import time
import google.generativeai as genai

# Set page title
st.set_page_config(page_title="NetflixParody", page_icon="⭕")

def get_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

def set_bg(image_path):
    img_base64 = get_base64(image_path)
    bg_css = f"""
    <style>
        .stApp {{
            background-image: url("data:image/png;base64,{img_base64}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
    </style>
    """
    st.markdown(bg_css, unsafe_allow_html=True)

#setting bg
set_bg("login.jpg")

hours_per_week = 0
years = 0
monthly_cost = 0

# Adding custom CSS for specific elements
# Adding custom CSS for specific elements with important for color and font changes
st.markdown("""
    <style>
        h1 {
            font-family: 'Impact', serif !important;  /* Custom font for headers */
            font-size: 40px !important;
            color: #ff4b4b !important;  /* Custom color */
        }

        h2 {
            font-family: 'Lexend', sans-serif !important;  /* Font for h2 headers */
            font-size: 25px !important;
            color: #bdf2ff !important;  /* Color for h2 headers */
        }

        p {
            font-family: 'Lexend', sans-serif !important;  /* Font for paragraph text */
            font-size: 18px !important;
            color: #ffffff !important;  /* Color for paragraphs */
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "submitted" not in st.session_state:
    st.session_state["submitted"] = False 

if "romance" not in st.session_state:
    st.session_state["romance"] = False 

if "action" not in st.session_state:
    st.session_state["action"] = False 

if "comedy" not in st.session_state:
    st.session_state["comedy"] = False 

if "documentaries" not in st.session_state:
    st.session_state["documentaries"] = False 

if "chatbot" not in st.session_state:
    st.session_state["chatbot"] = False 

if "hours_per_week" not in st.session_state:
    st.session_state["hours_per_week"] = 0

if "years" not in st.session_state:
    st.session_state["years"] = 0

if "monthly_cost" not in st.session_state:
    st.session_state["monthly_cost"] = 0    


# Custom CSS for buttons
st.markdown("""
    <style>
        /* Change all buttons */
        div.stButton > button {
            background-color: #ff4b4b !important; /* Red color */
            color: white !important;
            font-size: 16px !important;
            border-radius: 10px !important;
            padding: 10px !important;
        }

        /* Hover effect */
        div.stButton > button:hover {
            background-color: #cc0000 !important;
        }
    </style>
""", unsafe_allow_html=True)

# If submitted, show the main page instead of the login page
if st.session_state["submitted"]:

    gif_base64 = get_base64("profilepic.gif")
    st.markdown(
        f"""
        <style>
        .top-right {{
            position: fixed;
            top: 70px;
            right: 30px;
            width: 100px;
            z-index: 9999;
        }}
        </style>
        <img src="data:image/gif;base64,{gif_base64}" class="top-right">
        """,
        unsafe_allow_html=True
    )

    # Always show genre buttons + Home button
    col1, col2, col3, col4, col5, col6 = st.columns([0.8, 1.4, 1.3, 1.4, 1.9, 1.6])

    with col1:
        if st.button("🏠︎"):
            st.session_state["romance"] = st.session_state["action"] = st.session_state["comedy"] = st.session_state["documentaries"]= st.session_state["chatbot"] = False
            st.rerun()

    with col2:
        if st.button("ʀᴏᴍᴀɴᴄᴇ"):
            st.session_state["romance"] = True
            st.session_state["action"] = st.session_state["comedy"] = st.session_state["documentaries"] = st.session_state["chatbot"]= False
            st.rerun()

    with col3:
        if st.button("ᴀᴄᴛɪᴏɴ"):
            st.session_state["action"] = True
            st.session_state["romance"] = st.session_state["comedy"] = st.session_state["documentaries"]= st.session_state["chatbot"] = False
            st.rerun()

    with col4:
        if st.button("ᴄᴏᴍᴇᴅʏ"):
            st.session_state["comedy"] = True
            st.session_state["romance"] = st.session_state["action"] = st.session_state["documentaries"]= st.session_state["chatbot"] = False
            st.rerun()

    with col5:
        if st.button("ᴅᴏᴄᴜᴍᴇɴᴛᴀʀɪᴇs"):
            st.session_state["documentaries"] = True
            st.session_state["romance"] = st.session_state["action"] = st.session_state["comedy"]= st.session_state["chatbot"] = False
            st.rerun()

    with col6:
        if st.button("ᴄʜᴀᴛʙᴏᴛ"):
            st.session_state["chatbot"] = True
            st.session_state["romance"] = st.session_state["action"] = st.session_state["comedy"]= st.session_state["documentaries"] = False
            st.rerun()
    st.divider()  # Separates buttons from content

    # Now check which genre is selected and show content
    if st.session_state["romance"]:
        st.markdown("<h1><span style='font-size: 50px;'>❤️</span> Romance</h1>", unsafe_allow_html=True)
        st.markdown("<span style='font-size: 30px;'>💌</span> Ask someone out (or at least make awkward eye contact)", unsafe_allow_html=True)
        st.markdown("<span style='font-size: 30px;'>🍽️</span> Go on a date (Yes, with an actual human, not your fridge)", unsafe_allow_html=True)
        st.markdown("<span style='font-size: 30px;'>🥂</span> Meet new people (or just talk to your pet like always)", unsafe_allow_html=True)
        st.markdown("<span style='font-size: 30px;'>💃</span> Learn to dance (because 'two left feet' is not a compliment)", unsafe_allow_html=True)

    elif st.session_state["action"]:
        st.markdown("<h1><span style='font-size: 50px;'>🔥</span> Action & Adventure</h1>", unsafe_allow_html=True)
        st.markdown("<span style='font-size: 30px;'>🏄</span> Try an extreme sport (or at least jump off your couch dramatically)", unsafe_allow_html=True)
        st.markdown("<span style='font-size: 30px;'>🚀</span> Travel somewhere new (No, the grocery store doesn't count)", unsafe_allow_html=True)
        st.markdown("<span style='font-size: 30px;'>🦸‍♂️</span> Train like a superhero (or just wear a cape and pretend)", unsafe_allow_html=True)
        st.markdown("<span style='font-size: 30px;'>🎯</span> Take up archery (because every action movie hero does)", unsafe_allow_html=True)

    elif st.session_state["comedy"]:
        st.markdown("<h1><span style='font-size: 50px;'>🤣</span> Comedy</h1>", unsafe_allow_html=True)
        st.markdown("<span style='font-size: 30px;'>😂</span> Hang out with friends (and make fun of each other)", unsafe_allow_html=True)
        st.markdown("<span style='font-size: 30px;'>🎤</span> Try stand-up comedy (your shower audience doesn’t count)", unsafe_allow_html=True)
        st.markdown("<span style='font-size: 30px;'>🎭</span> Play games like Dumb Charades (because looking ridiculous is fun)", unsafe_allow_html=True)
        st.markdown("<span style='font-size: 30px;'>🤣</span> Watch a sitcom with actual people instead of rewatching memes", unsafe_allow_html=True)

    elif st.session_state["documentaries"]:
        st.markdown("<h1><span style='font-size: 50px;'>🎓</span> Documentaries</h1>", unsafe_allow_html=True)
        st.markdown("<span style='font-size: 30px;'>📊</span> Research investing (or pretend you understand stocks)", unsafe_allow_html=True)
        st.markdown("<span style='font-size: 30px;'>💼</span> Learn business strategies (so you can nod wisely at meetings)", unsafe_allow_html=True)
        st.markdown("<span style='font-size: 30px;'>📖</span> Read books (and then aggressively recommend them to friends)", unsafe_allow_html=True)
        st.markdown("<span style='font-size: 30px;'>🔬</span> Discover fun science facts (Did you know bananas are berries?)", unsafe_allow_html=True)

    elif st.session_state["chatbot"]:
        # Securely load API key
        genai.configure(api_key=st.secrets["genai"]["api_key"])

        # Model configuration
        generation_config = {
            "temperature": 0,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }

        safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        ]

        model = genai.GenerativeModel(
            model_name="gemini-1.5-pro",
            safety_settings=safety_settings,
            generation_config=generation_config,
            system_instruction=(
                "You’re not just any assistant—you’re the intervention people don’t know they need. Your job is to analyze binge-watchers, talk to them, understand their habits, and help them regain control. There are all kinds of binge-watchers out there. Some chase the thrill of cliffhangers, convincing themselves that sleep is optional. Others find comfort in rewatching the same shows, using them as a shield against stress or loneliness. Some binge to escape reality, while others are trapped by sheer inertia—autoplay makes the decisions for them. And then there are the FOMO-driven watchers, terrified of being left out of cultural conversations, racing through shows just to keep up. Your goal? Figure out which type they are, dig into their reasons, and offer personalized strategies to help them break free. Not through guilt or nagging, but by guiding them toward self-awareness, setting realistic boundaries, and showing them what actually works for them. You’re not here to take away their favorite shows—you’re here to make sure they are the ones in control, not the algorithm."
                "Dont ask more than 1 question at time...keep it short"
            ),
        )

        # Streamlit UI
        st.title("CHATBOT")
        st.markdown("<h2 style='color:#bdf2ff; font-family: Lexend; font-size: 20px;'>Chat with the AI to help stop binge-watching!</h2>", unsafe_allow_html=True)

        # Initialize chat history
        if "history" not in st.session_state:
            st.session_state.history = []
        if "last_input" not in st.session_state:
            st.session_state.last_input = ""

        # Display chat history
        for message in st.session_state.history:
            role = "👤 You" if message["role"] == "user" else "🤖 Bot"
            st.markdown(f"**{role}:** {message['parts'][0]}")

        # User input
        user_input = st.text_input("Type your message and press Enter:", key="user_input")

        if user_input and user_input != st.session_state.last_input:
            st.session_state.last_input = user_input  # Store the last input to avoid duplication

            # Start a chat session
            chat_session = model.start_chat(history=st.session_state.history)

            # Get AI response
            response = chat_session.send_message(user_input)
            model_response = response.text

            # Update chat history
            st.session_state.history.append({"role": "user", "parts": [user_input]})
            st.session_state.history.append({"role": "model", "parts": [model_response]})

            # Clear input box after submission
            st.rerun()

    else:

        # Header Section
        st.markdown("<div class='main-container'>", unsafe_allow_html=True)
        st.markdown("<h1>📺 STOP BINGE-WATCHING!</h1>", unsafe_allow_html=True)
        st.markdown("<h2>Find out what you could have achieved instead!</h2>", unsafe_allow_html=True)


        total_hours = st.session_state["hours_per_week"] * 52 * st.session_state["years"]
        days_wasted = total_hours / 24
        minutes_wasted = total_hours * 60
        seconds_wasted = total_hours * 3600
        estimated_spent = st.session_state["years"] * 12 * st.session_state["monthly_cost"]
        if total_hours > 10000:
            binge_rank = "🔥 **Legendary Binge Master**"
        elif total_hours > 5000:
            binge_rank = "👑 **Ultimate Couch Potato**"
        elif total_hours > 2500:
            binge_rank = "📺 **Binge-Watcher Pro**"
        elif total_hours > 1000:
            binge_rank = "🍿 **Casual Binger**"
        else:
            binge_rank = "🎬 **Movie Night Enthusiast**"

        st.markdown(f"""
            <h2 style='color:#bdf2ff; font-family: Lexend; font-size: 20px;'>⏳ You've wasted: 
            <span style='color:#ff4b4b; font-family: lexend; font-size: 28px;'>{total_hours:,} hours</span>
            </h2>
        """, unsafe_allow_html=True)
        st.markdown(f"<span style='color:#ff4b4b; font-family: Lexend; font-size: 24px;'>({days_wasted:.1f} days, {minutes_wasted:,} minutes, {seconds_wasted:,} seconds)</span>", unsafe_allow_html=True)
        st.markdown(f"💰 **You've spent ₹{estimated_spent:,} on streaming subscriptions!**")
        
        if total_hours>0:
            alt_spending = [
                "A full gym membership for 3 years 🏋️",
                "Invested in online courses 📚",
                "Multiple vacations ✈️",
                "A new laptop 💻",
                "Started a side hustle 🚀"
            ]
            st.markdown(f"### ➡️ Instead, you could have: {random.choice(alt_spending)}")
        
        # Show calendar breakdown
        start_date = datetime.date.today() - datetime.timedelta(days=int(days_wasted))
        st.markdown(f"📆 **Time Lost Since:** {start_date.strftime('%B %d, %Y')}")
        st.markdown(f"🏆 **Your Binge-Watching Rank:** {binge_rank}")

        st.divider()

        # Trending Now Section
        st.markdown("## 🔥 Trending Now (Things to Do Instead!)")
        trending_activities = [
            "🌿 Go for a nature hike",
            "🏋️ Join a fitness challenge",
            "📖 Take an online course",
            "🎸 Learn to play an instrument",
            "🧘 Practice mindfulness & meditation"
        ]

        for i in trending_activities:
            st.markdown(i)

        st.divider()

        # Screen Time Tracker
        st.markdown("## 📊 Track Your Screen Time & Progress")
        st.markdown("_(Coming Soon: Weekly Progress Tracking!)_ 🕒")
        st.markdown("🔥 _Set goals to cut down your binge-watching hours and replace them with meaningful activities!_")

        st.divider()

        # Productivity Tips
        st.markdown("## 💡 Productivity Tips")
        tips = [
            "📅 Schedule your entertainment time.",
            "🎯 Replace one episode with learning something new.",
            "⏰ Try the 2-day rule: No back-to-back binge days!",
            "💪 Engage in active hobbies like sports, music, or art.",
            "🔄 Swap streaming with audiobooks or podcasts."
        ]
        st.success(random.choice(tips))
        
        # Easter Egg
        if total_hours > 3000:
            st.warning("🎉 Easter Egg Unlocked: You might need a break from screens right now! 😆")
        
        st.markdown("</div>", unsafe_allow_html=True)

        # List of frame paths (adjust folder name if needed)
        frames = [f"images/cropped_image ({i}).png" for i in range(1, 25)]  # Ensure 'images/' folder exists

        # Empty container for animation
        image_container = st.empty()


else:
    # Display Login Form
    st.markdown("""
        <h1 style='font-family:Lexend; font-size: 45px; color:#bdf2ff;'>NETFLIX PARODY</h1>
        <h3 style='font-family:Impact; font-size: 25px; color:#ff4b4b;'>𖣠 Sign in</h3>
    """, unsafe_allow_html=True)

    st.session_state["hours_per_week"] = st.number_input("⌛ Hours binge-watched per week:", min_value=0, step=1)
    st.session_state["years"] = st.number_input("📅 Years of binge-watching:", min_value=0, step=1)
    st.session_state["monthly_cost"] = st.number_input("💰 Your Monthly Streaming Cost (₹):", min_value=0, step=1)

    if st.button("Submit",use_container_width=True):
        st.session_state["submitted"] = True  # Mark submission
        st.rerun()  # Refresh to load the main page
