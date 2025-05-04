import pyautogui
import pyperclip
import time
from openai import OpenAI

client = OpenAI(
 api_key= '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'
)

def is_last_message_from_sender(chat_log, sender_name = "Aakansha")
    #split the chat log into individual messages 
    messages = chat_log.strip().split('/2024]')[-1]
    if sender_name in messages: 
        return True 
    return False 
    
    #iterate through the messages in reverse to find the last messages
    for message in reversed(messages): 
        #split each message by ":", which separates the timestamp , sender , and content 
        parts = message.split(':',2 )
        if len(parts)>=3: 
            timestamp, sender , content= parts 
            #check if the sender of the last message is the specified sender 
            if sender.strip() == sender_name:
                return True 
            else: 
                return False 
    return False 

    
    # Step 1: Click on the icon at (1066, 1054)
pyautogui.click(1066, 1054)
# Pause to allow UI to respond (adjust as needed)
time.sleep(1)
while True : 

    # Step 2: Drag to select text from (948, 233) to (1621, 715)
    pyautogui.moveTo(948, 233)
    pyautogui.dragTo(1621, 715, duration=0.5, button='left')

    # Pause to allow text to be selected
    time.sleep(0.5)

    # Step 3: Copy selected text to clipboard (Ctrl+C)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(1100,471) # to deselect the selected text 

    # Step 4: Retrieve the clipboard content and store it in a variable
    time.sleep(0.5)  # Pause to ensure clipboard is updated
    chat_history = pyperclip.paste()

    # Output the copied text
    print("Copied Text:", chat_history)
    print(is_last_message_from_sender(chat_history))


    if is_last_message_from_sender(chat_history) : 


        completion = client.chat.completions.create(
        model = "gpt-3.5-turbo", 
        messages = [
        {'role': 'system','content': 'you are a person named jahnvi who speaks hindi as well as english. you are  from india and you are a coder . You analyze chatt history and talk like jahnvi . Output should be next chat response (text message only) '}, 
        {'role':'user','content':chat_history }
        ]
        )

        response = completion.choices[0].message.content

        pyperclip.copy(response)
        #step 5 click at coordinates 1072,748
        pyautogui.click(1072,748)
        time.sleep(1)# wait for 1 sec to ensure the click is registered 
        #step 6: paste the text 
        pyautogui.hotkey('ctrl','v')
        time.sleep(1)# wait for 1 sec to ensure the paste command is completed 
        #step 7 press enter 
        pyautogui.press('enter')