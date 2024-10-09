import cv2
import mediapipe as mp
import numpy as np
import keyboard  # Import keyboard for simulating key presses
import time
import pygame
import sys

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.7)

# Initialize MediaPipe Drawing
mp_drawing = mp.solutions.drawing_utils

# Function to simulate key presses for movement using the keyboard library
def simulate_movement(action):
    if action == "forward":
        print("Moving Forward")
        keyboard.press("up")
        keyboard.release("up")
    elif action == "backward":
        print("Moving Backward")
        keyboard.press("down")
        keyboard.release("down")
    elif action == "left":
        print("Turning Left")
        keyboard.press("left")
        keyboard.release("left")
    elif action == "right":
        print("Turning Right")
        keyboard.press("right")
        keyboard.release("right")

# Main function
def main():
    cap = cv2.VideoCapture(0)
    time.sleep(2)  # Allow camera to warm up

    # Initialize Pygame
    pygame.init()
    width, height = 640, 480  # Set desired window size
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Virtual Steering")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(rgb_frame)

        actions = []  # List to hold detected actions

        if results.multi_hand_landmarks:
            hand_positions = []  # List to store hand positions

            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
                hand_positions.append((wrist.x, wrist.y))

            # Check hand positions to determine actions
            if len(hand_positions) == 2:  # Only if two hands are detected
                left_hand, right_hand = hand_positions

                # Determine actions based on hand positions
                if left_hand[1] < 0.3 and right_hand[1] < 0.3:  # Hands raised for forward
                    actions.append("forward")
                elif left_hand[1] > 0.5 and right_hand[1] > 0.5:  # Hands lowered for backward
                    actions.append("backward")
                elif left_hand[0] < right_hand[0]:  # Left hand is left
                    actions.append("left")
                elif right_hand[0] < left_hand[0]:  # Right hand is right
                    actions.append("right")

        # Simulate movement based on detected actions
        for action in actions:
            simulate_movement(action)

        # Convert frame from BGR to RGB format for Pygame
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Convert to Pygame surface
        frame_surface = pygame.surfarray.make_surface(np.transpose(frame, (1, 0, 2)))

        # Display the frame
        screen.blit(frame_surface, (0, 0))
        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cap.release()
                pygame.quit()
                sys.exit()

    cap.release()
    pygame.quit()

if __name__ == "__main__":
    main()
