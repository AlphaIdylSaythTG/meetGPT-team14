import streamlit as st
from streamlit_option_menu import option_menu

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
        problem  = "airbag failure" #we will get this from the user (react front end)
        prompt = ""
        #prompt = "give me a fishbone analysis for airbag failure "
        # Make the API call
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]

        )


generated_text = response.choices[0].message.content

print(generated_text)


    elif selected_page == "Chat With Meeting":
        st.write("This is the Chat With Meeting page.")
    
    elif selected_page == "Name Mention":
        st.write("This is the Name Mention page.")

if __name__ == "__main__":
    main()
