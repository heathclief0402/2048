# 2048 Game in Python

This is a **Python implementation** of the classic **2048 game** in a Jupyter Notebook. The game features a **4×4 grid**, where tiles with numbers **merge when moved in the same direction**. The goal is to **reach 2048** before running out of moves.

## 🛠 Features
✅ Randomly initializes with **two "2" numbers**  
✅ Supports **w (up), s (down), a (left), d (right)** for movement  
✅ **Tiles merge** when moved in the same direction  
✅ **Game over detection** when no moves are possible  
✅ **Win detection** when a tile reaches 2048  
✅ **Exception handling** for invalid inputs  

---

## 📜 How to Play
- **Use the keyboard**:  
  - `w` → Move **up**  
  - `s` → Move **down**  
  - `a` → Move **left**  
  - `d` → Move **right**  
  - `q` → Quit the game  
- Tiles **move in the chosen direction** and **merge if they are the same**.  
- A new **random "2" tile** appears after every move.  
- The game **ends if no moves are left** or **if 2048 is reached**.

---

## 🏗 Project Structure
```
2048-game/
│── 2048.ipynb        # Runs the game loop (importing helper functions)
│── helper_2048.py    # Contains game logic (board updates, moves, merging, etc.)
│── README.md         # Game documentation (this file)
```

---

## 🚀 Setup Instructions

### **1️⃣ Install Python (if not already installed)**
Make sure you have **Python 3.8+** installed. If not, download it from [python.org](https://www.python.org/).

### **2️⃣ Install Dependencies (Jupyter Notebook)**
Run the following command in your terminal or command prompt:
```sh
pip install notebook numpy
```

### **3️⃣ Clone the Repository**
If you haven't already, clone this project from **GitHub**:
```sh
git clone https://github.com/your-username/2048-game.git
cd 2048-game
```

### **4️⃣ Run the Game**


#### **Option 1: Run in Jupyter Notebook**
Open the Jupyter Notebook environment and execute the game.

```sh
jupyter notebook
```

---

## 🛠 Function Descriptions
The game logic is implemented in `helper_2048.py`. Below are key functions:

### **🔹 `initialize_game()`**
Creates a **4×4 empty board** and adds **two random "2" numbers**.

### **🔹 `add_new_number(board)`**
Places a **new "2" numbers** in a random empty space.

### **🔹 `move_left(board)`**
Shifts all numbers **to the left**, merging identical ones.

### **🔹 `move_right(board)`**
Flips the board, calls `move_left()`, and flips it back.

### **🔹 `move_up(board)`**
Rotates the board **90° clockwise**, calls `move_left()`, then rotates it back.

### **🔹 `move_down(board)`**
Rotates the board **90° counterclockwise**, calls `move_left()`, then rotates it back.

### **🔹 `is_game_over(board)`**
Checks if **no more moves are possible** or if **2048 is reached**.

### **🔹 `print_board(board)`**
Clears the screen and prints the current **board state**.

---

## 🎯 Winning & Losing Conditions
✅ **You win** if you **merge a tile to 2048**.  
❌ **You lose** if **no more moves are possible**.

---

## 📜 License
This project is open-source and available under the **MIT License**.

---

## 🔗 GitHub Repository
[🔗 Your GitHub Repository Link](https://github.com/heathclief0402/2048)
