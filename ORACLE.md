# Oracle

- [Oracle](#oracle)
  - [Server Structure](#server-structure)
    - [Formatting](#formatting)
    - [Community Tools](#community-tools)
    - [Server Structure Oracle](#server-structure-oracle)
  - [Server Roles](#server-roles)
    - [Role Display](#role-display)

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
  > Onboarding is a discord feature that lets newcomers be guided through the personalization process and incentivize a first chat message. Onboarding could be a replacement for a traditional **#roles** channel.
- **Members**
  > The Members Page is a tool for moderators and admins to manage members of the server. Discord gives access to the tool if a user has at least one of the following permissions: administrator, manage server, manage roles, manage nicknames, ban members, timeout members, or kick members.
  > This tool can be useful for changing previous students to alumni after a summer break. For more information regarding the tool, visit [support.discord.com](https://support.discord.com/hc/en-us/articles/15946797617431-Members-Page).

### Server Structure Oracle

- **`INFORMATION`**
  - **rules**
    > Includes opening hours, what food to bring, the user must behave well, etc. The user needs to accept the terms to access the discord server.
  - **announcements**
  - **links**
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
  - **discord** (Subscribed to discord newsletter)
    > Mainly a channel for admins to see new discord features. Could include threads that has the purpose of logging the server or new members joining.
    - _Member Log_
    - _Change Log_
    - _Bot Activity Log_

## Server Roles

A list of roles supported by the discord server. The headers should be surrounded by two "▬" in the server to distinguish them from regular roles. They are not meant to be assignable.  
On the roles that has an emoji present, it is not part of the role title but a way to dictate what should be added to a user's username. The discord bot should automatically assign the emojis when a role changes.

- **▬▬ BTH Employees ▬▬**
  - Lab Director 🥼
    > Employee responsible for the lab.
  - Lab Researcher 🥼
    > University Professors who are active in creating workshops and making projects.
- **▬▬ Lab Assistants ▬▬**
  - Ratministrator 🧀
    > Role dedicated to manage the discord server itself. It is a dangerous role because it has the same privileges as Lab Director and could change anything.
  - Rat King 👑
  - Lab Rat 🐀
  - Lab Mouse 🐁
  - Lab Escapee 🚪
- **▬▬ Study Programs ▬▬**
  - SE-BSc
  - SE-MSc
  - Sec-BSc
  - Sec-MSc
  - AI Study
  - Web Study
  - Game Study
  - Other Study
- **▬▬ Study Year ▬▬**
  - 20
  - 21
  - ...
    > Perhaps too ambitious. Would be nice to see which year a student began their study.
- **▬▬ Miscellaneous ▬▬**
  > A set of roles that are difficult to group with other roles. They could be expertise or role 
  - Alumni 🎓
  - Visitor 🎩
  - Print Master 🏗️
- **▬▬ Rat King Tools ▬▬**
  > A set of roles that Rat King should manage on the fly. None of them should effect the user experience.
  - Test Subject 🧪
    > A role given to newcomers. Will be removed after they've accepted the `#rules`.
  - Lendmaster 📤
  - Borrower 📥
    > Roles given to the labrat lending and the user recieving respectevely.
  - Study Curious
    > A role for displaying all courses and program information.

### Role Display

All roles **not** specified shall have the default role color and keep the extra display options disabled.

- **BTH Employees** has a blue color to represent the university color. _Lab Director_ has a brighter color to signify their importance while _Lab Researcher_ has a darker color. _Lab Director_ always has both roles as _Lab Researcher_ shall be the "Display role members separately from online members" while director does not.
- **Lab Assistants** _Lab Rat_ and _Lab Mouse_ shall display role members seperate from others and anyone should be able to _@mention_ the role.
  - **_Rat King_** shall have a gold color to represent their royalty as well as be part of _Lab Rat_ to be grouped together.
- **Study Programs** has each field of study represented by a color. Master's has a brighter color of the bachelor's color, this is to follow the similar logic in BTH Employees.
