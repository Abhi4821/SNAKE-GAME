
🐍 Snake Game (Pygame)
🎮 A classic Snake Game developed using Python and Pygame, built as a second-year college project by:
Abhishek Yadav, Vivek Yadav, Sushant Singh, and Narayn

📸 Screenshot
<img width="1920" height="1080" alt="Screenshot 2025-08-04 093847" src="https://github.com/user-attachments/assets/846323e8-911c-4f88-8356-3d4ed8123c89" />
<img width="1898" height="766" alt="image" src="https://github.com/user-attachments/assets/2974c57a-f3e3-4c59-97c6-4ad9feae98a3" />



🧠 Features
Classic snake movement using arrow keys

Random food spawning with real-time score updates

Game Over screen with option to:

Press C to restart

Press Q to quit

Built-in sound effects:

🎵 Game start

🍎 Eating food

❌ Game over

📁 Project Structure
bash
Copy
Edit
SNAKE-GAME/
│
├── game.py             # Main game loop and logic
├── settings.py         # Constants: screen size, colors, game speed
├── display.py          # Scoreboard, rendering snake, game visuals
├── food.py             # Food object generation and placement logic
│
├── eat.wav             # Sound when food is eaten
├── distory.wav         # Sound on game over
├── MP3.mp3             # Intro music when game starts
├── tab.wav             # (Optional: Additional sound effect)
│
├── __pycache__/        # Python cache files
▶️ How to Run the Game
Install Python 3.13+

Download Python

Install Required Libraries

bash
Copy
Edit
pip install pygame
pip install playsound
pip install random2
Run the Game

bash
Copy
Edit
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
All sound files used in the game are stored locally:

eat.wav – Played when food is eaten

distory.wav – Played on game over

MP3.mp3 – Intro music

📌 To-Do / Future Improvements
 High score saving and tracking

 Add a welcome/menu screen UI

 Mobile support (e.g., Kivy framework)

 Web version via Pyodide or WebAssembly

📚 Libraries Used
pygame – Core game engine

playsound – For background music

random2 – Enhanced randomness (Python 2 and 3 compatible alternative)

🏫 Project Info
🎓 This game was created as part of a college second-year project focused on practical application of Python programming, game loops, real-time input handling, and modular code architecture.
