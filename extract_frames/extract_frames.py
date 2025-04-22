import cv2
import os
import re

class VideoEditor:
    def trim_video(self, video_path, start_time, end_time, output_path):
        """
        Trim a video to the specified start and end times and save it to the given output path.

        Args:
            video_path (str): Path to the input video file.
            start_time (float): Start time in seconds.
            end_time (float): End time in seconds.
            output_path (str): Path to save the trimmed video.
        """
        print(f"Processing {video_path}")
        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        start_frame = int(start_time * fps)
        end_frame = int(end_time * fps)

        cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, fps, (int(cap.get(3)), int(cap.get(4))))

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            if cap.get(cv2.CAP_PROP_POS_FRAMES) > end_frame:
                break
            out.write(frame)

        cap.release()
        out.release()

    def extract_frames_evenly(self, video_path, output_folder, num_frames):
        """
        Extract evenly spaced frames from a video and save them as images in the specified folder.

        Args:
            video_path (str): Path to the input video file.
            output_folder (str): Directory where extracted frames will be saved.
            num_frames (int): Number of frames to extract.
        """
        os.makedirs(output_folder, exist_ok=True)

        # Get the highest existing frame number in the folder
        existing_files = os.listdir(output_folder)
        frame_numbers = [
            int(re.search(r'(\d+).jpg', filename).group(1))
            for filename in existing_files if re.search(r'(\d+).jpg', filename)
        ]
        max_existing_frame = max(frame_numbers) if frame_numbers else 0

        cap = cv2.VideoCapture(video_path)
        frame_interval = cap.get(cv2.CAP_PROP_FRAME_COUNT) // num_frames

        for i in range(num_frames):
            cap.set(cv2.CAP_PROP_POS_FRAMES, i * frame_interval)
            ret, frame = cap.read()
            if not ret:
                break
            frame_path = os.path.join(output_folder, f"{max_existing_frame + i + 1}.jpg")
            cv2.imwrite(frame_path, frame)
            print(f"Saved frame: {frame_path}")

        cap.release()


if __name__ == "__main__":
    vide_editor = VideoEditor()
    base_dir = r'/Volumes/NO NAME/NAIST_HAI_research/interview_datas/14'
    os.makedirs(os.path.join(base_dir, "videos"), exist_ok=True)

    # Video 1
    input_video = os.path.join(base_dir, "1.mov")
    output_video = os.path.join(base_dir, "videos", "1.mp4")
    img_folder = os.path.join(base_dir, "extracted_images")
    vide_editor.trim_video(input_video, 2, 20, output_video)
    vide_editor.extract_frames_evenly(output_video, img_folder, 100)
    print("\n\n")

    # Video 2
    input_video = os.path.join(base_dir, "2.mov")
    output_video = os.path.join(base_dir, "videos", "2.mp4")
    img_folder = os.path.join(base_dir, "extracted_images")
    vide_editor.trim_video(input_video, 2, 20, output_video)
    vide_editor.extract_frames_evenly(output_video, img_folder, 100)
    print("\n\n")

    # Video 3
    input_video = os.path.join(base_dir, "3.mov")
    output_video = os.path.join(base_dir, "videos", "3.mp4")
    img_folder = os.path.join(base_dir, "extracted_images")
    vide_editor.trim_video(input_video, 2, 20, output_video)
    vide_editor.extract_frames_evenly(output_video, img_folder, 100)
