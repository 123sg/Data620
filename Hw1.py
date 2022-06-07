
# coding: utf-8

# In[3]:


import matplotlib.pyplot as pyp
import networkx as nw


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')
G=nw.Graph()

G.add_edge('andre','beverly')
G.add_edge('andre','carol')
G.add_edge('andre','diane')
G.add_edge('beverly','andre')
G.add_edge('beverly','diane')
G.add_edge('beverly','ed')
G.add_edge('carol','andre')
G.add_edge('carol','diane')
G.add_edge('carol','fernando')
G.add_edge('fernando','garth')
G.add_edge('fernando','diane')
G.add_edge('fernando','carol')
G.add_edge('garth','ed')
G.add_edge('garth','diane')
G.add_edge('garth','fernando')
G.add_edge('garth','heather')
G.add_edge('ed','beverly')
G.add_edge('ed','diane')
G.add_edge('ed','garth')
G.add_edge('heather','fernando')
G.add_edge('heather','garth')
G.add_edge('heather','ike')
G.add_edge('ike','heather')
G.add_edge('ike','jane')
G.add_edge('jane','ike')

# Set node positions explicitly 
pos={'andre':(0,1),
     'beverly':(0,-1),
     'carol':(1,2),
     'diane':(1,0),
     'ed':(1,-2),
     'ike':(4,0),
     'garth':(2,-1),
     'jane':(5,0),
     'fernando':(2,1),
     'heather':(3,0)}

# nodes
nw.draw_networkx_nodes(G,pos,node_size=800, node_color='c')

# edges
nw.draw_networkx_edges(G,pos,alpha=0.5,width=6)

# labels
nw.draw_networkx_labels(G,pos,font_size=15,font_family='sans-serif')

pyp.axis('off')
pyp.show()

