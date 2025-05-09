#!/usr/bin/env python
# coding: utf-8

# In[4]:


# get_ipython().system('pip install streamlit')


# In[47]:


get_ipython().run_cell_magic('writefile', 'relationship.py', "import streamlit as st\n\n# Input\na = st.selectbox('人物1', ('唐恺仪','何博文','蔡伯源'))\nb = st.selectbox('人物2', ('唐恺仪','何博文','蔡伯源'))\n\n#process\nif a == '蔡伯源':\n    if  b == '何博文':\n        c = (a + '\u3000是\u3000' + b + '\u3000的大儿')\n    elif b == '唐恺仪':\n        c = (a + '\u3000是\u3000' + b + '\u3000的大儿')\n    else:\n        c = ('本人')\n\nelif a == '何博文':\n    if  b == '蔡伯源':\n        c = (a + '\u3000是\u3000' + b + '\u3000的大爹')\n    elif b == '唐恺仪':\n        c = (a + '\u3000是\u3000' + b + '\u3000的恋人')\n    else:\n        c = ('本人')\nelse:\n    if  b == '何博文':\n        c = (a + '\u3000是\u3000' + b + '\u3000的恋人')\n    elif b == '蔡伯源':\n        c = (a + '\u3000是\u3000' + b + '\u3000的母亲')\n    else:\n        c = ('本人')\n\n#output\nst.write('三个人的关系')\nst.write(c)\n")


# In[ ]:


get_ipython().system("echo 'test@email'| streamlit run relationship.py")

