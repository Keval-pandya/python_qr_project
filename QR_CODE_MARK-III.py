#!/usr/bin/env python
# coding: utf-8

# In[14]:


import qrcode 
input_data=input("Enter url")
qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
a=input('ENter qrname')
img.save(a+'.png')
