# Setting up Local Ollama model with Hermes Agent

## Why setup a local model in the first place?
1. Privacy: Conversations and personal data never have to leave your machine. This helps protect your data from data leaks and misuse, which is an issue with cloud hosted ai agents.
2. Cost: Cloud(API) run on a subscription model whereas in a local ai model the only cost incurred is the electricity cost of running the model and one time investement of GPU's needed for that model. Ollama provides many different models that can run on older gpu's as well. 
3. Offline Access: Local agents work without any internet access forever.

# Obsidian: Personal Note Taking/Knowledge Management System

Obsidian is the best and easiest to use markdown files manager that can be easily connected to any local agent. Obsidian allows for wiki-links to be created so you can have connected notes that are easy to traverse and sort. 

Obsidian can be installed by simpling going to "https://obsidian.md/"

Once installed, a vault can be created and saved at any location preferable to the user


# Installing OLLAMA agent

You can easily install ollama by going to "https://ollama.com/download" - paste the install code in powershell or install through the website itself.

Once downloaded, check if the installation was successful by running the command "ollama --version" in powershell.

Next step is installing the ollama model for your device. Here you have to be mindful of your machine specifications(the hardware you have) and which model it can handle. Different models have different parameters and you need to make sure your hardware can handle the model.

I am using Gemma4:e4b on my device. The E4B(Effective Parameters) model can run soothly on 8GB of RAM/VRAM, so most laptops and computers. If you have a lower end system or want to run ollama on mobile, go with Gemma4:e2b model.

Installing the model is simple as copying its name from the website and asting this command in the terminal/powershell:  "ollama pull <model_name>"

So for Gemma:e4b you would run the command: ollama pull gemma4:e4b


After installation you can run "ollama list" to make sure the model was installed properly, you should see all the models installed on your device.


You can run Ollama model with "ollama run gemma4:e4b" - it will think for a while and then you can ask the ai a question and it will respond! Great you have a thinking brain in your system now!


# Fixing context window for HERMES AGENT

Hermes agent documentation requires any ollama model to have minimum 64K context window. The model we installed has only

































