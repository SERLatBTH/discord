# Oracle

This document defines structures for how the Discord Server shall be configured. Including comments with reasoning behind selected configuration options. Acts as a backup if the Discord Server gets compromised or an authorized user changes unintended settings without documentation.

## Server Structure

### Formatting

Categories (which acts like folders) are defined as `Markdown code brackets`.
Channel for chatting is defined with **Markdown bold**.
Thread for temporary chatting is defined with _Markdown italics_
A channel only used for threads is defined with **_Markdown bold italics_**.
Comments are defined as `> Markdown quotes`.
See example below:

- **`CATEGORY`**
  > Comment on category
  - **Channel**
    > Comment about channel
  - **_Thread Exclusive Channel_**
    - _Thread name example 1_
    - _Example 2_
      > Comment on individual thread or the thread channel as a whole
  - **Channel-2**
  - ...

### Community Tools

These are tools provided by discord that can help both users and moderators to find information about events, channels and members.

- **Events**
  > Only users who have the "Create Events" or "Manage Events" permissions are allowed to see this tool by default. If there is a planned event or ongoing event, then everyone will be able to see the button with additional information.
- **Browse Channels**
  > Everyone is allowed to browse channels of the Discord Server. It is an accessibility tool intended for massive community servers with personalization. Our server is **not** intended to be massive by any means, the feature is redundant for our use case.
  > Browse Channels do support "Onboarding" which is accessible through `Server Settings > Community > Onboarding` or by right-clicking "Browse Channels" button and then "Edit Onboarding".
  > Onboarding is a discord feature that lets newcomers be guided through the personalization process and incentivizes a first chat message. Onboarding could be a replacement for a traditional **#roles** channel.
- **Members**
  > The Members Page is a tool for moderators and admins to manage members of the server. Discord gives access to the tool if a user has at least one of the following permissions: administrator, manage server, manage roles, manage nicknames, ban members, timeout members, or kick members.
  > This tool can be useful for changing previous students to alumni after a summer break. For more information regarding the tool, visit [support.discord.com](https://support.discord.com/hc/en-us/articles/15946797617431-Members-Page).

### Server Structure Oracle

- **`INFORMATION`**
  - **rules**
    > Includes opening hours, what food to bring, the user must behave well, etc. The user needs to accept the terms to access the discord server.
  - **announcements**
  - **links**
  - **roles**
    > Could be replaced with _Onboarding_ from [Community Tools](#community-tools)
- **`GENERAL`**
  - **general**
  - **memes**
  - **_discussions_**
    - _Games to buy_
    - _Any plans to hold a movie night?_
    - _Etc_
      > A thread channel dedicated to discussions, anyone can create a thread in that channel and the discord bot may reformat the thread to be "`@user` wish to discuss about `#Games to buy`". (Subject to change, it is a very long message for it to be spammed in a single channel).
- **`HELP`**
  - **lab-access**
  - **loan-equipment**
    > A channel dedicated for discord-bot to manage renting equipment. It is read only, but admins can send a command for the discord-bot to keep track of responsibility and return date.
- **`STUDY`**
  - **software-engineering**
  - **other-program-overview**
    > Dedicated channels for students to see their program overview of courses. The channel is read only and is managed by admins through discord-bot commands. Only the users with the specific `@program` role will have access to their dedicated channel. The last message will always be a reaction message to toggle visibility of all program overviews.
  - **_all-courses_**
    - _XX0000 - Web programming_
    - _XX0000 - Introduction to software_
    - _Etc_
      > A dedicated channel for all university courses that are relevant to our discord server. This will act as a registry for any student user to look for struggles and solutions from previous students. Only the discord-bot will manage this channel by creating threads based on program overviews defined above. The last message will always be instructions on how to use Discord's search threads function in the top right corner.
- **`RODENTS`**
  - **general**
  - **lab-suggestions**
    > A forum to discuss how to improve the lab
  - **happenings**
    - _Robotics Workshop_
    - _Open House_
    - _Lab Meeting 2024-08-13_
      > A channel that acts as both announcements and events in one. Admins can announce upcoming meetings. Moderators can create threads to plan upcoming happenings. Here lies an opportunity for the discord bot to summarize past meetings to create an opening speech for a new meeting. Perhaps `/meeting` is a suitable command.
  - **announcements** (Subscribed to discord newsletter)
    > Mainly a channel for admins to see new discord features, maybe can be applied on a thread or removed as the channel itself won't be too useful.
