import cv2

# Load video file
video_file = r"D:\Study\github\STT_Interview_Feedback_system\test_video.mp4"
cap = cv2.VideoCapture(video_file)

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)  # Get the frame rate of the input video
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define font and position for displaying text
font = cv2.FONT_HERSHEY_COMPLEX  # Change to a more aesthetically pleasing font
font_scale = 0.5  # Reduce the font size
font_color = (255, 255, 255)  # White color
line_thickness = 2
text_position = (50, 50)  # Adjust as needed

# Open text file containing results
result_file = "result.txt"
with open(result_file, "r") as f:
    lines = f.readlines()

# Initialize video writer
output_video_file = "output_video.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4 files
out = cv2.VideoWriter(output_video_file, fourcc, fps, (frame_width, frame_height))  # Use the same frame rate as input video

# Initialize a variable to keep track of the current line in the results file
current_line = 0

# Initialize a variable to keep track of the current frame
current_frame = 0

# Initialize a variable to keep track of the current overlay text
overlay_text = ""

# Iterate through each frame of the input video
while True:
    # Read video frame
    ret, frame = cap.read()
    if not ret:
        break

    # Get the current timestamp of the video
    current_timestamp = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000

    # If the current timestamp matches the timestamp in the current line of the results file, update the overlay text
    if current_line < len(lines):
        speaker_id, timestamp, text = lines[current_line].strip().split(" ", 2)
        timestamp = float(timestamp)
        if current_timestamp >= timestamp:
            overlay_text = f"{speaker_id}: {text}"
            current_line += 1

    # Overlay the current text on the frame
    frame = cv2.putText(frame, overlay_text, text_position, font, font_scale, font_color, line_thickness)

    # Write frame to output video
    out.write(frame)

    # Increment the current frame
    current_frame += 1

# Release video writer
out.release()

# Release video capture
cap.release()

# Close OpenCV windows
cv2.destroyAllWindows()

print(f"Processed video saved as {output_video_file}")
