import cv2
import mediapipe as mp
import time
import numpy as np

# --- CONFIGURATION ---
VIDEO_PATH = 'testvideo.mov'
MODEL_COMPLEXITY = 1

def run_benchmark():
    # Initialize MediaPipe
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        model_complexity=MODEL_COMPLEXITY,
        min_detection_confidence=0.5
    )

    cap = cv2.VideoCapture(VIDEO_PATH)
    if not cap.isOpened():
        print(f"Error: Could not open video {VIDEO_PATH}")
        return

    latencies = []
    frame_count = 0

    print(f"Starting Benchmark on: {VIDEO_PATH}...")

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        # Pre-processing
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # --- MEASURE ---
        start_time = time.time()
        results = hands.process(img_rgb)

        # Gesture Recognition
        if results.multi_hand_landmarks:
            for hand_lms in results.multi_hand_landmarks:
                lms = hand_lms.landmark

                index_up = lms[8].y < lms[5].y
                middle_up = lms[12].y < lms[9].y
                ring_up = lms[16].y < lms[13].y
                pinky_up = lms[20].y < lms[17].y
                thumb_out = abs(lms[4].x - lms[5].x) > 0.05
                thumb_up = lms[4].y < lms[3].y and thumb_out

                # Classification
                if index_up and middle_up and not ring_up and not pinky_up:
                    _ = "PEACE"
                elif thumb_up and not index_up and not middle_up:
                    _ = "THUMBS UP"
                elif index_up and middle_up and ring_up and pinky_up:
                    _ = "PALM"
                elif not index_up and not middle_up and not ring_up and not pinky_up:
                    _ = "FIST"

        end_time = time.time()


        latencies.append((end_time - start_time) * 1000)
        frame_count += 1

    cap.release()

    # --- STATS CALCULATION ---
    avg_lat = np.mean(latencies)
    std_lat = np.std(latencies)
    avg_fps = 1000 / avg_lat

    print("\n" + "=" * 30)
    print("   FINAL BENCHMARK RESULTS APPLE M5 ")
    print("=" * 30)
    print(f"Total Frames Processed: {frame_count}")
    print(f"Average Latency:        {avg_lat:.2f} ms")
    print(f"Standard Deviation:     {std_lat:.2f} ms")
    print(f"Average Throughput:     {avg_fps:.2f} FPS")
    print("=" * 30)


if __name__ == "__main__":
    run_benchmark()