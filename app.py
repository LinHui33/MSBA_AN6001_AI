#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask,request,render_template


# In[2]:


app = Flask(__name__)


# In[ ]:


@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        rate = float(request.form.get('rate'))
        price = round((rate*(-50.60094302) + 90.22858515), 4)
        
        return render_template("index.html", result = price)
    else:
        return render_template("index.html", result = "waiting for exchange rate.............")
if __name__ == "__main__":
    app.run()


# In[ ]:




