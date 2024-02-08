import streamlit as st 
import pandas as pd

st.sidebar.title('STT + Diarization')
st.sidebar.markdown('STT (Speech-to-Text) converts speech into text, while diarization segments speech by speaker.')
option = st.sidebar.radio('Choose an option', ('Demo', 'Try it'), index=0)
if option=="Demo":
# Title
    st.title('STT + Diarization (Demo)')
    # st.write('STT (Speech-to-Text) converts speech into text, while diarization segments speech by speaker. Integrating the two allows for accurate transcriptions with speaker identification, essential for tasks like meeting summaries and call center analytics.')
    # File uploader
    # uploaded_file = st.file_uploader("Choose a file")

    # Button
    # if st.button('Transcribe'):
    #     if uploaded_file is not None:
    #         st.write('File uploaded')
    #     else:
    #         st.write('No file uploaded')
    st.write("Original Video")
    st.markdown(
            """
            <iframe width="700" height="400" src="https://www.youtube.com/embed/FRTpI2Gu1KA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            """,
            unsafe_allow_html=True,
        )
    st.header("Transcribed Video without Diarization")
    #read from txt and display
    with open(r'D:\Study\github\STT_Interview_Feedback_system\result_without.txt', 'r') as file:
        data = file.read().replace('\n', '')
    st.text_area("Transcription", data, height=400, label_visibility="hidden")
    
    
    st.header("Transcribed Video + Diarization")
    
    st.write("STT + Diarization (Video)")
    #show video from local
    st.video(r"D:\Study\github\STT_Interview_Feedback_system\final_video.mp4")
    #read and show csv as dataframe
    df = pd.read_csv(r'D:\Study\github\STT_Interview_Feedback_system\result.csv')
    st.dataframe(df, height=400, width=700)
    
else:
    st.title('STT + Diarization (Try it)')
    st.write('STT (Speech-to-Text) converts speech into text, while diarization segments speech by speaker. Integrating the two allows for accurate transcriptions with speaker identification, essential for tasks like meeting summaries and call center analytics.')
    # File uploader
    st.header("Upload your audio file (Mp3, Wav)")
    uploaded_file = st.file_uploader("Choose a file", label_visibility="hidden")

    # Button
    
    

# from stl_backend.core.stt_model import STTModelWithoutDia

# stt = STTModelWithoutDia()
# stt.main(r"D:\Study\github\STT_Interview_Feedback_system\stl_backend\podcast.mp3")