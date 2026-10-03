# Setting up Local Ollama model with Hermes Agent

## Why setup a local model in the first place?
1. Privacy: Conversations and personal data never have to leave your machine. This helps protect your data from data leaks and misuse, which is an issue with cloud hosted ai agents.
2. Cost: Cloud(API) run on a subscription model whereas in a local ai model the only cost incurred is the electricity cost of running the model and one time investement of GPU's needed for that model. Ollama provides many different models that can run on older gpu's as well. 
3. Offline Access: Local agents work without any internet access forever.

# Obsidian: Personal Note Taking/Knowledge Management System

Obsidian is the best and easiest to use markdown files manager that can be easily connected to any local agent. Obsidian allows for wiki-links to be created so you can have connected notes that are easy to traverse and sort. 

Obsidian can be installed by simpling going to "https://obsidian.md/"

Once installed, a vault can be created and saved at any location preferable to you.


# Installing OLLAMA agent

You can easily install ollama by going to "https://ollama.com/download" - paste the install code in powershell/terminal or install through the website itself.

Once downloaded, check if the installation was successful by running the command "ollama --version" in powershell/terminal.

Next step is installing the ollama model for your device. Here you have to be mindful of your machine specifications (the hardware you have) and which model it can handle. Different models have different parameters and you need to make sure your hardware can handle the model.

I am using Gemma4:e4b on my device. The E4B(Effective Parameters) model can run smoothly on 8GB of RAM/VRAM, so most laptops and computers. If you have a lower end system or want to run ollama on mobile, go with Gemma4:e2b model.

Installing the model is simple as copying its name from the website and pasting this command in the terminal/powershell: "ollama pull <model_name>"

So for Gemma:e4b you would run the command: "ollama pull gemma4:e4b"

After installation you can run "ollama list" to make sure the model was installed properly, you should see all the models installed on your device.


You can run Ollama model with "ollama run gemma4:e4b" - it will think for a while and then you can ask the AI any question and it will respond! Great you have a thinking brain in your system now! You can type /bye to end conversation.


# Fixing context window for HERMES AGENT - Creating a Variant

Hermes agent documentation requires any ollama model to have minimum 64000 token context window. You can check the context window of your model by "ollama ps". It will be 4096 or less.

Simply paste the command:
@"
FROM gemma4:e4b

PARAMETER num_ctx 65536
"@ | Set-Content Modelfile

Then:

ollama create gemma4e-64k -f Modelfile

Then check if gemma4e-64k created by command "ollama list"

# Downloading HERMES AGENT

Simply download the deskop app from "https://hermes-agent.nousresearch.com/"
Once inside the HERMES app, open settingsnd inside the MODEL section click on the dropdown right beneath where it says "Use the model picker in the composer to hot-swap the active chat". Here scroll down and select LOCAL(127.0.0.1:11434) and click setup custom endpoint. In the window that pops up, select Local/custom endpoint and add the address http://127.0.0.1:11434/v1 beneath, click connect.

Once this is done you can go to the landing page of the desktop app and you will see your local models in the dropdown inside your chat. Select gemma4e-64k and you are good to go.

I prefer to use my ollama model with HERMES within the powershell due to desktop app sometimes having trouble accessing the terminal. So for that all you have to do is go to powershell/terminal and type "ollama launch hermes", navigate and select the agent you want to use and run it. All the conversations you have with your agent inside powershell also get saved to the desktop app and you can find them easily there.

# Creating HERMES profile and SKILL

For personal transcription and knowledge management, we setup another profile of HERMES agent that has particular skills and personality to handle our raw transcripts and communicate with Obidian vault.

For this, inside the HERMES desktop app, click on + icon at the bottom left corner to create new profile. Give it any name you like and keep everything same and click CREATE PROFILE.

To give your agent certain skills(which is added to SKILL.md) and personality(which is SOUL.md) you have to find the folder inside your system where HERMES files are saved. This is mostly inside AppData\Local\hermes but you may have to dig around for it.

Once you find the hermes folder, click on profiles folder. There you will see the profile you just created. Inside this folder is where we will make the changes. 

Inside you will see a skills folder. Open it and create a new folder called "Organiser" there. Inside this Organiser folder you will add the SKILL.md file i have uploaded. Feel free to change the file as per your requirements, think of this file as the instructions for you AI agent to follow when you ask it to organise your raw transcripts. 

Return to the profile folder and there update the .env file according to the .env file I have uploaded here. This tells your agent the exact location of the Obsidian vault it is supposed to access.

This is also where you will find the SOUL.md, simply update it with the SOUL.md I have provided. Make sure you change it according to your own specifications. 

With this we are done setting up. You can now go to the HERMES app or inside powershell launch your profile with "hermes --profile <profile-name>". Now you can ask your agent if it can access your obsidian vault and what files are in it as a test. I would suggest you make a file inside your vault with a secret code and ask the agent to retrieve the code to make sure the obsidian vault is properly being accessed.

Then it is as simple as running the batch file I made for the recorder and transcriber, saving files to obsidian vault and then going and triggerring your agent with the trigger phrase and getting your notes sorted and neatly organised. 



























