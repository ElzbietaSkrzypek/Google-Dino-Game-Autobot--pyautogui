# Google-dino-game-autobot
1. Clone repo to Automate the Google Dinosaur Game
 - On Chrome, when you try to access a website and your internet is down, you see a little dinosaur. On this page, there is a hidden game, if you hit space bar you can play the T-rex run game. 
![image](https://user-images.githubusercontent.com/125986679/230074578-8d763282-9107-45f9-a494-c0a9f30a4b4c.png)

  - Alternatively you can access the game directly here: https://offline-dino-game.firebaseapp.com/.

2. Check dinos top of the nose position. - Run check-dino-position.py and within 3 seconds set mose pointer on the dinos top of the nose. (You can extend time by changing time.sleep(3) to other values).
3. Change screenshot region on main.py adequatly to your print(pyautogui.position()) results from previous step, as desribed in comments.
4. Run program main.py and play automatically dino game

# Requirements
pip install -r requirements.txt
