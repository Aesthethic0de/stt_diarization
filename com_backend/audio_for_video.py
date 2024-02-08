from moviepy.editor import VideoFileClip


# Get the original video
original_video = VideoFileClip(r"D:\Study\github\STT_Interview_Feedback_system\test_video.mp4")

# Get the processed video
processed_video = VideoFileClip(r"D:\Study\github\STT_Interview_Feedback_system\output_video.mp4")

# Add the original audio to the processed video
processed_video = processed_video.set_audio(original_video.audio)

# Write the result to a file
processed_video.write_videofile(r"D:\Study\github\STT_Interview_Feedback_system\final_video.mp4")