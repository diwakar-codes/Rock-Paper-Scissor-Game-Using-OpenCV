Rock–Paper–Scissors with Computer Vision
=========================================

Overview
--------
This project is an interactive Rock–Paper–Scissors game built with Python, OpenCV, and CVZone.  
The player shows hand gestures (rock, paper, or scissors) to the webcam, and the AI generates its own move.  
The game keeps track of scores in real time with a dynamic background interface.  

Features
--------
- Real-time hand gesture detection using CVZone HandTrackingModule  
- Smooth timer-based gameplay (3-second countdown)  
- AI opponent with random move generation  
- Score tracking for both player and AI  
- Graphical background with overlays for enhanced UI  

Tech Stack
----------
Language: Python  
Libraries: OpenCV, CVZone, Random, Time  

Project Structure
-----------------
game.py → Main game script  
Resources/ → Contains background image (BG.png) and AI hand images (1.png, 2.png, 3.png)  
README.md → Project documentation  

How to Run
----------
1. Clone the repository:  
   git clone https://github.com/your-username/rock-paper-scissors-ai.git  
   cd rock-paper-scissors-ai  

2. Install dependencies:  
   pip install opencv-python cvzone  

3. Run the game:  
   python game.py  

4. Controls:  
   Press s → Start the game  
   Press q → Quit the game  

Rules
-----
Rock: All fingers down  
Paper: All fingers up  
Scissors: Only index and middle fingers up  

AI randomly chooses one of the moves. Scores are updated live on screen.  

Future Enhancements
-------------------
- Add difficulty levels for AI  
- Introduce gesture recognition with MediaPipe  
- Build a GUI-based version with Tkinter or Streamlit  
- Deploy as a web application  

Results
-------
- Displays real-time background with scores  
- Declares final winner (Player, AI, or Tie) at the end  

License
-------
This project is open-source and available under the MIT License.  
