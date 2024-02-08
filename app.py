# import streamlit as st
# import whisperx

# def main():
#     st.title("Speech-to-Text with Diarization")

#     # # Sidebar configuration
#     # st.sidebar.header("Parameters")
#     # audio_file = st.sidebar.file_uploader("Upload Audio File", type=["wav"])
#     # device = st.sidebar.selectbox("Device", ["cuda", "cpu"])
#     # batch_size = st.sidebar.number_input("Batch Size", min_value=1, value=4)
#     # compute_type = st.sidebar.selectbox("Compute Type", ["float16", "int8"])

#     # if st.sidebar.button("Transcribe Audio"):
#     #     if audio_file is not None:
#     #         audio = whisperx.load_audio(audio_file)

#     #         # Transcribe audio
#     #         model = whisperx.load_model("large-v2", device, compute_type=compute_type)
#     #         result = model.transcribe(audio, batch_size=batch_size)

#     #         # Align output
#     #         model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=device)
#     #         result = whisperx.align(result["segments"], model_a, metadata, audio, device, return_char_alignments=False)

#     #         # Diarization
#     #         diarize_model = whisperx.DiarizationPipeline(use_auth_token="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", device=device)
#     #         diarize_segments = diarize_model(audio, min_speakers=2, max_speakers=2)

#     #         # Assign speakers to words
#     #         result = whisperx.assign_word_speakers(diarize_segments, result)

#     #         # Write results to file
#     #         with open("result.txt", "w") as f:
#     #             for seg in result["segments"]:
#     #                 f.write(seg["speaker"] + " " + str(seg["start"]) + " " + seg["text"] + "\n")

#     #         st.success("Transcription and diarization completed. Result saved to result.txt.")
#     #     else:
#     #         st.warning("Please upload an audio file.")
            
# import streamlit as st
# import pandas as pd

# # Use pandas to read the CSV file
# df = pd.read_csv(r'D:\Study\github\STT_Interview_Feedback_system\result.csv')

# # Use Streamlit to display the DataFrame
# st.dataframe(df)
    

# if __name__ == "__main__":
#     main()

# import pandas as pd

# # Read the text file line by line
# file_path = r"D:\Study\github\STT_Interview_Feedback_system\result.txt"
# data = []
# with open(file_path, "r") as file:
#     for line in file:
#         line = line.strip().split(" ", 2)  # Split each line into speaker, timestamp, and context
#         data.append(line)
        

# # Create DataFrame
# df = pd.DataFrame(data, columns=["Speaker", "Timestamp", "Context"])
# df["Timestamp"] = pd.to_numeric(df["Timestamp"])# Convert timestamp column to numeric


print(df)

#save the result to csv
df.to_csv(r"D:\Study\github\STT_Interview_Feedback_system\result.csv", index=False)

