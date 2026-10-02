import streamlit as st
from google import genai
from google.genai import types
import time

from prompts import (
    SYSTEM_PROMPT,
    MEAL_ESTIMATION_INSTRUCTIONS,
    WELCOME_MESSAGE_TEMPLATE,
    SUMMARY_REQUEST_PROMPT,
)

# =========================
# CONFIGURATION
# =========================

API_KEY = st.secrets["Gemini_API_Key"]

# Verify this exact model ID is supported by your API key.
MODEL_NAME = "gemini-3.8-flash"


@st.cache_resource
def get_gemini_client():
    return genai.Client(api_key=API_KEY)


gemini_client = get_gemini_client()


# =========================
# GEMINI CHAT
# =========================

def ask_gemini(parts):
    max_retries = 3

    for attempt in range(max_retries):
        try:
            response = st.session_state.chat.send_message(parts)

            return response.text or (
                "I couldn't generate a response. Please try again."
            )

        except Exception as error:
            error_message = str(error)

            # Retry temporary server errors and rate limits.
            if any(code in error_message for code in [
                "503",
                "UNAVAILABLE",
                "429",
                "RESOURCE_EXHAUSTED",
            ]):
                if attempt < max_retries - 1:
                    wait_time = 2 ** (attempt + 1)

                    time.sleep(wait_time)
                    continue

                st.warning(
                    "⚠️ Gemini is temporarily busy or the request "
                    "limit has been reached. Please try again later."
                )
                return None

            # Handle other errors without retrying.
            st.error(f"Gemini API error: {error}")
            return None

    return None

# =========================
# CHAT DISPLAY
# =========================

def render_message(message):
    with st.chat_message(message["role"]):
        if message["kind"] == "text":
            st.markdown(message["content"])

        elif message["kind"] == "image":
            st.image(message["content"])


def add_message(role, kind, content):
    message = {
        "role": role,
        "kind": kind,
        "content": content,
    }

    st.session_state.messages.append(message)
    render_message(message)


# =========================
# USER ONBOARDING
# =========================

if "onboarded" not in st.session_state:

    st.title("🥗 NutriLens")
    st.caption("📸 Snap it. Track it. Eat smarter. 💚")

    with st.form("onboarding_form"):

        name = st.text_input("Your name")

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=18,
        )

        sex = st.selectbox(
            "Sex (optional)",
            ["Prefer not to say", "Male", "Female"],
        )

        height = st.number_input(
            "Height (cm)",
            min_value=50.0,
            max_value=250.0,
            value=None,
            placeholder="Enter your height",
        )

        weight = st.number_input(
            "Weight (kg)",
            min_value=2.0,
            max_value=500.0,
            value=None,
            placeholder="Enter your weight",
        )

        activity_level = st.selectbox(
            "Activity level",
            [
                "Sedentary",
                "Lightly active",
                "Moderately active",
                "Very active",
            ],
        )

        goal = st.selectbox(
            "Your goal",
            [
                "Lose weight",
                "Maintain weight",
                "Gain weight",
            ],
        )

        submitted = st.form_submit_button("Let's go 🚀")

    if submitted:

        if not name.strip():
            st.warning("Please enter your name.")

        elif height is None or weight is None:
            st.warning("Please enter your height and weight.")

        else:
            st.session_state.name = name.strip()
            st.session_state.age = age

            st.session_state.sex = (
                None if sex == "Prefer not to say" else sex
            )

            st.session_state.height = height
            st.session_state.weight = weight
            st.session_state.activity_level = activity_level
            st.session_state.goal = goal

            # Give Gemini the user's profile without an extra API call.
            profile_context = f"""
            USER PROFILE:
            Name: {st.session_state.name}
            Age: {st.session_state.age}
            Sex: {st.session_state.sex or "Not provided"}
            Height: {st.session_state.height} cm
            Weight: {st.session_state.weight} kg
            Activity level: {st.session_state.activity_level}
            Goal: {st.session_state.goal}

            Use this profile for personalised nutrition guidance.
            Treat calculated nutrition targets as estimates.
            """

            st.session_state.chat = gemini_client.chats.create(
                model=MODEL_NAME,
                config=types.GenerateContentConfig(
                    system_instruction=(
                        SYSTEM_PROMPT + "\n\n" + profile_context
                    )
                ),
            )

            st.session_state.messages = []
            st.session_state.meals = []

            st.session_state.onboarded = True

            st.rerun()

    st.stop()


# =========================
# MAIN HEADER
# =========================

header_col, button_col = st.columns(
    [5, 2],
    vertical_alignment="center",
)

with header_col:
    st.title("🥗 NutriLens")

with button_col:
    if st.button(
        "📊 Daily Summary",
        use_container_width=True,
    ):
        with st.spinner("Summarizing your nutrition..."):

            summary = ask_gemini(
                [SUMMARY_REQUEST_PROMPT]
            )

            if summary:
                st.session_state.daily_summary = summary


st.caption(
    f"👋 Hey {st.session_state.name}! "
    f"🎯 Your Goal: {st.session_state.goal}"
)


# =========================
# DAILY SUMMARY
# =========================

if "daily_summary" in st.session_state:

    with st.container(border=True):

        st.subheader("📊 Your Daily Nutrition Summary")

        st.markdown(st.session_state.daily_summary)

        if st.button("✖️ Close Summary"):
            del st.session_state.daily_summary
            st.rerun()


# =========================
# CHAT HISTORY
# =========================

if not st.session_state.messages:

    add_message(
        "assistant",
        "text",
        WELCOME_MESSAGE_TEMPLATE.format(
            name=st.session_state.name
        ),
    )

else:

    for message in st.session_state.messages:
        render_message(message)


# =========================
# USER INPUT
# =========================

user_input = st.chat_input(
    "Ask me about nutrition or upload a meal photo 🥗",
    accept_file=True,
    file_type=["jpg", "jpeg", "png"],
)


if user_input:

    photo = user_input.files[0] if user_input.files else None
    text = user_input.text

    parts = []

    # Process an uploaded image.
    if photo is not None:

        photo_bytes = photo.getvalue()

        add_message(
            "user",
            "image",
            photo_bytes,
        )

        parts.append(
            types.Part.from_bytes(
                data=photo_bytes,
                mime_type=photo.type,
            )
        )

    # Process text input.
    if text:

        add_message(
            "user",
            "text",
            text,
        )

        parts.append(text)

    elif photo is not None:

        parts.append(MEAL_ESTIMATION_INSTRUCTIONS)

    # Generate the response.
    if parts:

        with st.spinner("🔍 Analysing your nutrition..."):

            answer = ask_gemini(parts)

        if answer:

            add_message(
                "assistant",
                "text",
                answer,
            )