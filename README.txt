Learning outcome
-Project is first created via terminal
-Syncing needs to be done frequently to sync database, by calling migrate on manage.py
----Serialization----
-Serialization is the process of converting an object into a stream of bytes to store the object or transmit it to memory, a database, or a file. Its main purpose is to save the state of an object in order to be able to recreate it when needed. The reverse process is called deserialization.
-serialization is done using serializer, which we can design ourselves the way data is represented
-----View-----
-each database entity can have its own viewset, where individual object can be viewed or edited, to keep it neat
-defaultly sorted by date joined
----URL----
-urls are automatically generated to match the viewsets
-But if more control is needed, can drop to using regular class-based views and write url configurations explicitly
----Setting----
-setting needs to be updated everytime new app/framework is created or used

Question:
What's the testing function for. ie. httpie

---ModelSerializer---
Provided by django, it allows code to be more concise.
Abit confused about the get put post delete functions for serializer
