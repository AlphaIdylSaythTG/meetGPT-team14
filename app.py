import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_chat import message
import openai


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
    st.title("Video Uploader and Option Menu")

    # Upload a video file
    video_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])

    if video_file:
        st.video(video_file)

    
    # Option menu
    selected_page = option_menu(
        menu_title="Select a page",
        options=["Summary", "Chat With meeting", "Name Mention"],
        icons=["map", "person-circle", "info"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )


    # Show content based on the selected option
    if selected_page == "Summary":
        st.write("This is the Summary page.")
        with open("sample.txt", "r") as f:
            text_data = f.read()

        prompt = "give me a summary of this: " + text_data
        generated_text = generate_response(prompt)
        
        print(generated_text)
        
        st.write(generated_text )


    elif selected_page == "Chat With meeting":
       

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

    elif selected_page == "Name Mention":
        st.markdown("# Name Mention Page")
        # Get the user's name input
        user_name = st.text_input("Enter your name:")

        if user_name:
            with open("sample.txt", "r") as f:
                text_data_transcr = f.read()

            # Process the transcript to find name mentions and related tasks
            name_mentions = []
            tasks = []

            # For simplicity, we assume that task-related keywords are "task" and "action item"
            task_keywords = ["task", "action item"]

            lines = text_data_transcr.split("\n")
            for line in lines:
                if user_name.lower() in line.lower():
                    name_mentions.append(line.strip())
                    for keyword in task_keywords:
                        if keyword in line.lower():
                            tasks.append(line.strip())
                            break

            # Generate the comprehensive report
            st.markdown(f"## Name Mentions for {user_name}")
            if name_mentions:
                for mention in name_mentions:
                    st.write(mention)
            else:
                st.write("No mentions of your name found in the meeting transcript.")

            st.markdown(f"## Tasks for {user_name}")
            if tasks:
                for task in tasks:
                    st.write(task)
            else:
                st.write("No tasks associated with your name found in the meeting transcript.")

            # Suggest what to do next based on the tasks
            if tasks:
                st.markdown("## Suggestions")
                st.write("You have the following tasks to complete:")
                for task in tasks:
                    st.write(f"- {task}")

                st.write("You should prioritize these tasks and work on them accordingly.")

        else:
            st.write("Please enter your name to generate the comprehensive report.")


    # ... (rest of the code remains unchanged)


if __name__ == "__main__":
    x = generate_response("blank_init")
    if x == 1:
        print("Sucessfully loaded")
    else:
        print("Error")
    
    main()