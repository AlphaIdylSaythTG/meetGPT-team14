meetGPT - AI Meeting Assistant
The meetGPT is an AI-powered meeting assistant built with Streamlit and GPT-3.5-turbo. It helps you interact with GPT-3.5-turbo to perform various tasks related to meeting transcripts and email generation.

Setup
Make sure you have installed the required packages in your Python environment:

bash
Copy code
pip install streamlit openai webvtt-py
Getting Started
To get started with meetGPT, follow these steps:

Create an OpenAI account and obtain your API key.
Save your OpenAI API key in a file named api-key.txt.
Usage
To use meetGPT, run the script containing the provided code. It sets up a Streamlit web application with several functionalities.

Supported Functionalities
Summary: Summarize the meeting transcript based on the selected summary level (Quick, Normal, or Detailed).

MeetChat: Interact with GPT-3.5-turbo in a chat-like format. The AI will act as an assistant answering questions about the meeting.

NameMention: Find mentions of a specific name in the meeting transcript along with timestamps.

EmailGen: Generate an email for a specific recipient and subject using the meeting transcript as a source of truth.

Additional Notes
Before using the MeetChat functionality, make sure to upload a meeting video file in mp4, avi, or mov format.

For Summary, NameMention, and EmailGen, ensure that a sample meeting transcript file named sample.txt is available in the same directory.

To use NameMention, provide the meeting transcript in WebVTT format with the filename sample.vtt.

To use EmailGen, input your name, the recipient's name, and the email content in the provided text inputs.

Important
Make sure to keep your OpenAI API key secure and not share it publicly.

This project assumes you have access to the GPT-3.5-turbo model from OpenAI.

Note
The code provided in this README is a simplified version and assumes you have set up the necessary Streamlit components and credentials. Please ensure your environment and dependencies are appropriately configured to run the meetGPT application successfully. Happy AI-assisted meetings!
