# https://jyotiskabhattacharjee.medium.com/guide-to-deleting-emails-using-google-gmail-apis-252e4a98572 for context
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import base64


# In[1]:


token='ya29.a0AfH6SMCa0aRk0P_4U9se7l4FLS-nEssII_Z77uRZuaf2ZR_naBQpyrx-H9KMCpHQppvGoGWp9F6cAl2U_97qClMGoTIZUkyue-QvgplUtzVDTvUqzrDAOSDBQ3l-5OBqRKHZAIyfat0fbML1HrY5uOgL1zYfLizXDb6hZJJWvg4'
url='https://gmail.googleapis.com/gmail/v1/users/me/messages?q=from%3Aabcd%40gmail.com'


# In[ ]:


#Email list from url generated from search query
def list_emails(token,url):
    headers = {
      'Authorization': 'Bearer {}'.format(token),
      'Content-Type': 'application/json'
    }
    r=requests.get(url, headers=headers)
    id_list=[]
    for i in r.json().get('messages'):
        id_list.append(i.get('id'))
    return(id_list)
    


# In[ ]:


#Delete Email list from abcd@gmail.com
def delete_emails(token,r):
    headers = {
          'Authorization': 'Bearer {}'.format(token),
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        }
    payload="""{}""".format({"ids":r})
    m=requests.post('https://gmail.googleapis.com/gmail/v1/users/me/messages/batchDelete', headers=headers,data=payload)


# In[ ]:


while True:
    try:
        r=list_emails(token,url)
        delete_emails(token,r)
    except:
        print("No more mails")
        break


# In[ ]:




