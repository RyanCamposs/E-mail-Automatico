#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pyautogui
import time 
import pyperclip


# In[ ]:


#1 - Abrir nova guia


# In[35]:


pyautogui.hotkey ('ctrl', 't')

time.sleep (4)

pyautogui.click (x=407, y=46)

pyautogui.write ('https://mail.google.com/mail/u/0/#inbox')

pyautogui.hotkey ('enter')

time.sleep (3)

pyautogui.click (x=68, y=165, clicks=2)

time.sleep (2)

pyautogui.click (x=1310, y=429)

pyautogui.write ('klikuacornoff20@gmail.com')

time.sleep (2)

pyautogui.click (x=1284, y=521)

pyautogui.write ('Mensagem enviada')

time.sleep (2)

pyautogui.click (x=1434, y=949)

time.sleep (3)

pyautogui.click (x=682, y=339)

time.sleep (4)

pyautogui.click (x=865, y=336, clicks=2)

time.sleep (4)

pyautogui.click (x=1307, y=943)







# In[34]:


time.sleep(5)
pyautogui.position ()


# In[ ]:




