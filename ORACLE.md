# Oracle

This document defines structures for how the Discord Server shall be configured. Including comments with reasoning behind selected configuration options. Acts as a backup if the Discord Server gets compromised or an authorized user changes unintended settings without documentation.

## Server Structure

### Formatting

Categories (which acts like folders) are defined as `Markdown code brackets`.  
Channel for chatting is defined with **Markdown bold**.  
Thread for temporary chatting is defined with *Markdown italics*  
A channel only used for threads is defined with ***Markdown bold italics***.  
Comments are defined as `> Markdown quotes`.  
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
  > Only users who have the "Create Events" or "Manage Events" permissions are allowed to see this tool by default. If there is a planned event or ongoing event, then everyone will be able to see button with additional information.
- **Browse Channels**
  > Everyone is allowed to browse channels of the Discord Server. It is an accessibility tool intended for massive community servers with personalization. Our server is **not** intended to be massive by any means, the feature is redundant for our use case.  
  > Browse Channels do support "Onboarding" which is accessible through `Server Settings > Community > Onboarding` or by right-clicking "Browse Channels" button and then "Edit Onboarding".  
  > Onboarding is a discord feature that lets newcomers be guided through the personalization process and incentivizes a first chat message. Onboarding could be a replacement for a traditional **#roles** channel. 
- **Members**
  > 

### Server Structure Oracle
- **`INFORMATION`**
  - **rules**
    > Includes opening hours, what food to bring, the user must behave well, etc. The user needs to accept the terms to access the discord server.
  - **announcements**
  - **links**
  - **roles**
    > Could be replaced with *Onboarding* from [Community Tools](#community-tools)
- **`GENERAL`**
  - **general**
  - **memes**
  - ***discussions***
    - *Games to buy*
    - *Any plans to hold a movie night?*
    - *Etc*
        > A thread channel dedicated to discussions, anyone can create a thread in that channel and the discord bot may reformat the thread to be "`@user` wish to discuss about `#Games to buy`". (Subject to change, it is a very long message for it to be spammed in a single channel).
- **`HELP`**
  - **lab-access**
  - **loan-equipment**
    > A channel dedicated for discord-bot to manage renting equipment. It is read only, but admins can send a command for the discord-bot to keep track of responsibility and return date.
  - 
- **`STUDY`**
  - **software-engineering**
  - **other-program-overview**
    > Dedicated channels for students to see their program overview of courses. The channel is read only and is managed by admins through discord-bot commands. Only the users with the specific `@program` role will have access to their dedicated channel. Unless they toggle the reaction message in `#all-courses`.
  - ***all-courses***
    - *XX0000 - Web programming*
    - *XX0000 - Introduction to software*
    - *Etc*
        > A dedicated channel for all university courses that are relevant to our discord server. This will act as a registry for any student user to look for struggles and solutions from previous students. Only the discord-bot will manage this channel by creating threads based on program overviews defined above. The last message will always be a reaction message to toggle visibility of all program overviews.
- **`RODENTS`**
  - **lab-suggestions**
    > A forum to discuss how to improve the lab
  - **general**
  - ***meeting-notes***
    - *2024-08-12*
        > A discord-bot managed channel to write meeting notes in.
  - **announcements** (Subscribed to discord newsletter)
    > Mainly a channel for admins to see new discord features, maybe can be applied on a thread or removed as the channel itself won't be too useful.

