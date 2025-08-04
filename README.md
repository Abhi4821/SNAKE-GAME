
🐍 Snake Game (Pygame)
🎮 A classic Snake Game developed using Python and Pygame,
built as a second-year college project by:
Abhishek Yadav, Vivek Yadav, Sushant Singh, and Narayn



📸 Screenshot
<img width="1920" height="1080" alt="Screenshot 2025-08-04 093847" src="https://github.com/user-attachments/assets/846323e8-911c-4f88-8356-3d4ed8123c89" /> <br> <img width="1898" height="766" alt="image" src="https://github.com/user-attachments/assets/2974c57a-f3e3-4c59-97c6-4ad9feae98a3" />



🧠 Features
🕹️ Classic snake movement using arrow keys
🍎 Random food spawning with real-time score updates
🔄 Game Over screen with restart or quit options
🔊 Sound effects:
🎵 Game start
🍎 Eating food
❌ Game over



📁 Project Structure

SNAKE-GAME/
│
├── game.py             # Main game loop and logic
├── settings.py         # Constants: screen size, colors, game speed
├── display.py          # Scoreboard, rendering snake, game visuals
├── food.py             # Food generation and placement
│
├── eat.wav             # Sound: food eaten
├── distory.wav         # Sound: game over
├── MP3.mp3             # Intro music
├── tab.wav             # Optional extra sound
│
├── __pycache__/        # Python cache
└── README.md           # Project info



▶️ How to Run the Game
1. Install Python 3.13+
➡️ Download Python


2. Install Required Libraries
pip install pygame
pip install playsound
pip install random2


3. Run the Game
python game.py



⌨️ Controls
Key	Action
↑	Move Up
↓	Move Down
←	Move Left
→	Move Right
C	Restart after Game Over
Q	Quit after Game Over



🔊 Sound Credits

All sound files are stored locally in the project:
eat.wav – Played when food is eaten
distory.wav – Played on game over
MP3.mp3 – Played at game start




📌 To-Do / Future Improvements

🏅 Add high score tracking
🧩 Welcome/menu screen UI
🌐 Web version using Pyodide or WebAssembly


📚 Libraries Used

pygame – Core game engine
playsound – Background music
random2 – Cross-compatible randomness



🏫 Project Info

🎓 This game was created as a second-year college project to explore:

Python fundamentals  
Game loops
Real-time input handling
Modular coding structure

