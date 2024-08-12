# Oracle

This document defines structures for how the Discord Server shall be configured. Including comments with reasoning behind selected configuration options. Acts as a backup if the Discord Server gets comprimised or an athoritized user changes unintended settings without documentation.

## Server Structure

### Formating

Categories (which acts like folders) are defined as `markdown code brackets`.  
Channel for chatting is defined with **markdown bold**.  
Thread for temporary chatting is defined with *markdown italics*  
A channel only used for threads is defined with ***markdown bold italics***.  
Comments are defined as `> markdown quotes`.  
See example below:

- **`CATEGORY`**
  > Comment on category
  - **Channel**
    > Comment about channel
  - ***Thread Exclusive Channel***
    - *Thread name example 1*
    - *Example 2*
        > Comment on individual thread or the thread channel as a whole
  - **Channel-2**
  - ...

### Community Tools
These are tools provided by discord that can help both users and moderators to find information about events, channels and members. 
- **Events**
  > Only users who has the "Create Events" or "Manage Events" permissions are allowed to see this tool by default. If there is a planned event or on going event, then everyone will be able to see button with additional information.
- **Browse Channels**
  > Everyone is allowed to browse channels of the Discord Server. It is an accessability tool intended for massive community servers with personalization. Our server is **not** intended to be massive by any means, the feature is redundant for our use case.  
  > Browse Channels do support "Onboarding" which is accessable through `Server Settings > Community > Onboarding` or by right-clicking "Browse Channels" button and then "Edit Onboarding".  
  > Onboarding is a discord feature that lets newcomers to be guided through the personalization process and incentivizes a first chat message. Onboarding could be a replacement for a traditional **#roles** channel. 
- **Members**
  > 

