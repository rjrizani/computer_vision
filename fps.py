import cv2

video_part = "video.mp4"
output_folder = "frames_output"

def get_properties(video_part):
    video_capture = cv2.VideoCapture(video_part)

    fps = video_capture.get(cv2.CAP_PROP_FPS)  # conversi data type from float to int
    print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

    width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print("Frame width : {0}, Frame height : {1}".format(width, height))

get_properties(video_part)

def get_frames(video_part, output_folder):
    video_capture = cv2.VideoCapture(video_part)

    frame_count = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    print("Frame count : {0}".format(frame_count))

    counter = 0
    success = True

    while success:
        success, frame = video_capture.read()
        if success:
            cv2.imwrite("{}/frame{:d}.jpg".format(output_folder, counter), frame)
            counter += 1

get_frames(video_part, output_folder)