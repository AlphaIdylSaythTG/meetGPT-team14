import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_chat import message
import openai
from webvtt import WebVTT

#A confirmation email that says I know my task and will keep him updated
with open("api-key.txt", "r") as file:
    openai.api_key = file.read().strip()


def generate_response(prompt):
    if prompt == "blank_init":
        return "1"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    generated_text = response.choices[0].message.content

    return generated_text


def main():
   # Custom CSS to center the title on the line
    st.markdown(
        """
        <style>
        .block-container {
            text-align: center;

        }

        .title {
            align-self: flex-start;
        </style>
        """,
        unsafe_allow_html=True
    )

    # logo = "logo.png"
    # st.image(logo, use_column_width=True)

    st.title("meetGPT")

    # Upload a video file
    video_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])

    if video_file:
        st.video(video_file)

        
        # Option menu
        selected_page = option_menu(
            menu_title="Select a page",
            options=["Summary", "MeetChat", "NameMention", "EmailGen"],
            icons=["map", "person-circle", "info"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
        )



        if selected_page == "Summary":
            summary_levels = ["Select Summary Level", "Quick", "Normal", "Detailed"]
            summary_level = st.selectbox("Select summary level:", summary_levels, index=0)
            if summary_level != "Select Summary Level":
                st.write(f"### Summary of meeting (Level: {summary_level}):")
                with open("sample.txt", "r") as f:
                    text_data = f.read()

                # Modify the prompt based on the selected summary level
                if summary_level == "Quick":
                    prompt = "Give me a brief summary of this text: " + text_data
                elif summary_level == "Normal":
                    prompt = "Give me a summary of this meeting: " + text_data
                else:  # Detailed
                    prompt = "Provide a detailed summary of the meeting: " + text_data

                generated_text = generate_response(prompt)
                st.write(generated_text)




        elif selected_page == "MeetChat":
        

            st.header("MeetBot - Your AI Meeting Q&A Assistant")

            if 'generated' not in st.session_state:
                st.session_state['generated'] = []

            if 'past' not in st.session_state:
                st.session_state['past'] = []

            def get_text():
                input_text = st.text_input(
                    "You: ", "What are the highlights of the meeting?", key="input")
                return input_text

            user_input = get_text()
            
        
            
            if user_input:
                with open("sample.txt", "r") as f:
                    text_data_transcr = f.read()

                user_input_2=user_input+ "Use this document as your source of truth to answer questions about the meeting. DO NOT refer to anything else, and solely rely on this document to provide answers: "+text_data_transcr
                output = generate_response(user_input_2)
                st.session_state.past.append(user_input)

                
                

                st.session_state.generated.append(output)

            if st.session_state['generated']:
                for i in range(len(st.session_state['generated'])):
                    message(st.session_state['past'][i],
                            is_user=True, key=str(i) + '_user')
                    message(st.session_state['generated'][i], key=str(i))

            
    # ... (previous code remains unchanged)

        elif selected_page == "NameMention":
            print("Name Mention")
            st.markdown("# Name Mention Page")
            # Get the user's name input
            user_name = st.text_input("Enter your name:")

            if user_name:
                with open("sample.txt", "r") as f:
                    text_data_transcr = f.read()

                # Load and parse the WebVTT subtitle file
                vtt_file = "sample.vtt"
                vtt = WebVTT().read(vtt_file)

                # Process the subtitle to find name mentions and related timestamps
                name_mentions = []
                timestamps = []

                # For simplicity, we assume that name mentions are case-insensitive
                user_name_lower = user_name.lower()

                for caption in vtt:
                    if user_name_lower in caption.text.lower():
                        name_mentions.append(caption.text.strip())
                        timestamps.append(caption.start)  # Store the start timestamp of the subtitle

                # Generate the comprehensive report
                st.markdown(f"## Name Mentions for {user_name}")
                if name_mentions:
                    for mention, timestamp in zip(name_mentions, timestamps):
                        st.write(f"{timestamp} - {mention}")
                else:
                    st.write("No mentions of your name found in the meeting transcript.")

        elif selected_page == "EmailGen":
                print("Email Gen")
                st.markdown("# Email Gen Page")
                # Get the user's name input
                your_name = st.text_input("What is your name?")
                if your_name:
                    email_name = st.text_input("Who would you like to email?")
                    if email_name:
                        email_content = st.text_input("What should the email be about?")
                        if email_content:
                            with open("sample.txt", "r") as f:
                                text_data_transcr = f.read()
                            #prompt = "Write an email to "+email_name+"from "+your_name+" about "+email_content+" using the following source of truth "+text_data_transcr
                            prompt = "My name is " + your_name + ". Write one very short paragraph email from me to " + email_name + ", about " + email_content +". Do not repeat anything in the meeting transcript and also generate a subject line for the email: \n" + text_data_transcr
                            generated_text = generate_response(prompt)
                            st.write("Here is your email:")
                            st.write(generated_text)

if __name__ == "__main__":
    x = generate_response("blank_init")
    if x == 1:
        print("Sucessfully loaded")
    else:
        print("Error")
    
    main()
