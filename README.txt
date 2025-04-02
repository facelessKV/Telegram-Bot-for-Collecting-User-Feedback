📢 Telegram-bot-collection-User-Feedback

Want to know what users think? 📋

The bot helps to collect reviews from customers and users directly to Telegram!


✅ What does he know?

 • ✍️ Allows customers to leave text reviews

 • 🗂️ Saves all the reviews in the database

 • 📥 sends notifications to the administrator about a new review


🔧 Functionality

✅ Convenient form for sending a review

✅ Ability to view and sort reviews

✅ easy integration with CRM



📩 Want to receive honest reviews from customers?


Contact me in Telegram, and I will help you set up this bot! 🚀


# Instructions for installing and starting a bot for collecting reviews


## What does the bot do


This bot collects reviews from users in Telegram and saves them into the database. The administrator can view all the reviews.


## Installation on Windows


### Step 1: Installation Python 3.9



1. Download Python 3.9.13 from the official site:

   https://www.python.org/downloads/release/python-3913/

2. Select "Windows Installer (64-bit)" and download the file.

3. Run the installer and be sure to mark the checkplace "Add Python 3.9 to Path" at the bottom of the installer window.

4. Click "Install Now".

5. Wait for the completion of the installation and click "Close".

### Step 2: Download Bot files

1. Create a folder with the name "Feedback_bot" on the desktop.

2. Copy a file with the bot code in this folder and name it "Bot.py".

### Step 3: Installation of the necessary libraries

1. Press Win+R, enter the CMD and click Enter to open the command line.

2. On the command line go to the folder with the bot, gaining:

   `` `

   CD C: Users -Militer Detesktop Eedback_bot

   `` `
   (Replace the name of the_Per in the name of your user in Windows)

3. Install the necessary library by introducing:

   `` `
   Pip Install Aiogram == 3.0.0

   `` `
## installation on Linux

### Step 1: Installation Python 3.9

1. Open the terminal using Ctrl+Alt+T.

2. Update the list of packages:

   `` `

   Sudo Apt Update

   `` `

3. Install the necessary tools:
   `` `
   SUDO APT Install Software-Properties-Common

   `` `

4. Add the repository with Python:
   `` `
   Sudo Add-Apt-Repository PPA: DeadSnakes/PPA
   `` `

5. Install Python 3.9:

   `` `

   SUDO APT Install Python3.9 Python3.9-Venv Python3-Pip

   `` `

### Step 2: Create a folder and a bot file

1. Create a folder for the bot:
   `` `
   mkdir ~/fedback_bot

   `` `



2. Go to this folder:

   `` `

   CD ~/fedback_bot

   `` `



3. Create a BOT.PY file using a text editor (for example, Nano):

   `` `

   Nano Bot.py

   `` `



4. Insert the bot code, click Ctrl+O to save, then Enter and Ctrl+X for exit.



### Step 3: Library installation



1. Install Aiogram:

   `` `

   Pip3 Install aiogram == 3.0.0

   `` `



## Settings of the bot



### Step 1: Obtaining a bot token



1. Open Telegram and find @botfather.



2. Send message: /Newbot



3. Follow the Botfather instructions:

   - Indicate the name for the bot (for example, "Feedback Collector")

   - Indicate username for the bot (should end at "BOT", for example, "My_FEDBACK_BOT")



4. Botfather will send you token, looking something like this: 1234567890: AABBCCCDDEEFGHIIJEGKLMNNOOPPQQQ



5. Copy this token.



### Step 2: Determination of your Telegram ID (for admin)



1. Find @userinfobot in Telegram



2. Send him any message



3. The bot will respond to you with a message in which your ID will be indicated (for example, "Your ID: 123456789")



4. Remember or write down this id



### Step 3: Bota File Setting



1. Open the BOT.PY file in any text editor.



2. Find the line:

   `` `

   API_TOKEN = 'Your_BOT_TOKEN'

   `` `

   

   Replace 'your_bot_token' with the token that you received from Botfather (be sure to save quotes).



3. Find the line:

   `` `

   Admin_id = 123456789

   `` `

   

   Replace 123456789 with your Telegram ID, which you received from @userinfobot (without quotes).



4. Save the file.



## launch of the bot



### in Windows:



1. Open the command line (Win+R, enter "CMD" and click Enter).



2. Go to the folder with the bot:

   `` `

   CD C: Users -Militer Detesktop Eedback_bot

   `` `



3. Run the bot:

   `` `

   Python Bot.py

   `` `



4. The bot is launched! Do not close the command line window until you want the bot to work.



### in linux:



1. Open the terminal (Ctrl+Alt+T).



2. Go to the folder with the bot:

   `` `

   CD ~/fedback_bot

   `` `



3. Run the bot:

   `` `

   Python3.9 Bot.py

   `` `



4. The bot is launched! Do not close the terminal until you want the bot to work.



## The use of the bot



1. Open Telegram and find your bot by the name you indicated when creating.



2. Send the `/star 'command to get a welcoming message.



3. To leave a review, send the `/fedback` command, and then write your review.



4. Administrator (whose ID is indicated in the settings) can view all the reviews by sending the bottle of `/all_FEDBACKS`.



## important comments



1. The bot will work only while the script is launched in the command line/terminal.



2. If you want the bot to work constantly, you will need hosting or VPS.



3. All reviews are stored to the file of the Feedback.db database in the same folder where the Bot.py file is located.



## Elimination of problems



1. If the error "Modulenotfounderror: No Module Named 'Aiogram'" "occurs, check that you correctly installed Aiogram:

   `` `

   Pip Install Aiogram == 3.0.0

   `` `

   

2. If the bot does not respond to commands, check that you indicated the correct token.



3. If you cannot view the reviews as an administrator, check that you indicated the correct administrator ID.



4. If the bot has stopped responding to the commands, restart it (close the command line/terminal and run it again).
