#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import *


# In[2]:


qr = QuantumRegister(2)


# In[3]:


cr = ClassicalRegister(2)


# In[4]:


circuit = QuantumCircuit(qr,cr)


# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


circuit.draw()


# In[7]:


circuit.h(qr[0])


# In[8]:


circuit.draw(output='mpl')


# In[9]:


circuit.cx(qr[0], qr[1])


# In[10]:


circuit.draw(output='mpl')


# In[11]:


circuit.measure(qr,cr)


# In[12]:


circuit.draw(output='mpl')


# In[15]:


simulator = Aer.get_backend('qasm_simulator')


# In[17]:


result = execute(circuit, backend=simulator).result()


# In[18]:


from qiskit.tools.visualization import plot_histogram


# In[19]:


plot_histogram(result.get_counts(circuit))


# In[20]:


IBMQ.load_account()


# In[21]:


provider = IBMQ.get_provider('ibm-q')


# In[26]:


qcomp = provider.get_backend('ibm_brisbane')


# In[27]:


job = execute(circuit, backend=qcomp)


# In[28]:


from qiskit.tools.monitor import job_monitor


# In[32]:


job_monitor(job) 


# In[33]:


result=job.result()


# In[34]:


plot_histogram(result.get_counts(circuit))


# In[ ]:




