# Oracle

- [Oracle](#oracle)
  - [Server Structure](#server-structure)
    - [Formatting](#formatting)
    - [Community Tools](#community-tools)
    - [Server Structure Oracle](#server-structure-oracle)
  - [Server Roles](#server-roles)
    - [Role Display](#role-display)
    - [Role Permissions](#role-permissions)
  - [Server Rules](#server-rules)
  - [Server Onboarding](#server-onboarding)
    - [1. Safety Check](#1-safety-check)
    - [2. Deafult Channels](#2-deafult-channels)
    - [3. Customization Questions](#3-customization-questions)
    - [4. Server Guide](#4-server-guide)
    - [5. Review](#5-review)

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
    - _Accept Rules_
      > Thread for new users to write their name to change their discord nickname and accept the rules.
  - **announcements**
  - **info-hub**
    > A resource channel for getting good general information, like opening hours during summer, or how to change nickname, or how to borrow equipment, etc. It is an information hub with resources on how to navigate the discord server.
- **`LAB`**
  - **general**
  - **memes**
  - **discussions**
    - _Games to buy_
    - _Any plans to hold a movie night?_
    - _Etc_
      > A thread channel dedicated to discussions, anyone can create a thread in that channel and the discord bot may reformat the thread to be "`@user` wish to discuss about `#Games to buy`". (Subject to change, it is a very long message for it to be spammed in a single channel).
  - **lab-access**
  - **loan-equipment**
    > A channel dedicated for discord-bot to manage renting equipment. It is read only, but admins can send a command for the discord-bot to keep track of responsibility and return date.
- **`GROUPS`**
  - **3d-print**
  - **ai-arena**
  - **code-crafter**
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
  - **discord-logs** (Subscribed to discord newsletter)
    > Mainly a channel for admins to see new discord features. Could include threads that has the purpose of logging the server or new members joining.
    - _Member Log_
    - _Change Log_
    - _Bot Activity Log_

## Server Roles

A list of roles supported by the discord server. The headers should be surrounded by two "▬" in the server to distinguish them from regular roles. They are not meant to be assignable.  
On the roles that has an emoji present, it is not part of the role title but a way to dictate what should be added to a user's username. The discord bot should automatically assign the emojis when a role changes.

- **▬▬ Admin ▬▬**
  - Ratministrator
    > Role dedicated to manage the discord server itself. It is a dangerous role because it has the same privileges as Lab Director and could change anything. This role is on the top of the list so that it has access to change all other roles.
- **▬▬ Lab Employees ▬▬**
  - Lab Director 🥼
    > Employee responsible for the lab.
  - Lab Researcher 🥼
    > University Professors who are active in creating workshops and making projects.
- **▬▬ Lab Assistants ▬▬**
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
- **▬▬ Lab Visitors ▬▬**
  > Set of roles for members outside the lab. For example, a professor from a different program or an external company employee.
  - BTH
  - Visitor 🎩
- **▬▬ Hobby Groups ▬▬**
  > A dynamic list of roles for dedicated groups within the lab. Such as hobbyist or participents in weekly activities. The **Hobby Groups** roles is the only set of roles that are expected to grow and shrink over time. The discord bot should have a command to manage these groups.
  - Ninja Maker/3D Printmaster
  - Code Crafter
  - AI Arena
  - ...
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

- **Lab Employees** has a blue color to represent the university color. _Lab Director_ has a brighter color `#6996a2` to signify their importance while _Lab Researcher_ has a darker color `#508593`. _Lab Director_ always has both roles. Only _Lab Researcher_ shall enable the "Display role members separately from online members". The color is based on the university color `#055064` but at 30 and 40 percent brighter respectively.
- **Lab Assistants** _Lab Rat_ and _Lab Mouse_ shall display role members seperate from others and anyone should be able to _@mention_ the role.
  - **_Rat King_** shall have a gold color `#FFD700` to represent their royalty as well as be part of _Lab Rat_ to be grouped together.
- **Study Programs** has each field of study represented by a color. Master's has a brighter color of the bachelor's color, this is to follow the similar logic in **Lab Employees**.
- **Lab Visitors** with its _BTH_ role has the blue color `#377383` which is 20% brighter version of the university color `#055064`.

### Role Permissions

If not specified every role has the same permissions as `@everyone`. The exception is the `Ratministrator` role which has the same permissions as `Lab Director`.

| Permission                                 | `@everyone` | Mouse |  Rat  | King  | Researcher | Director |
| :----------------------------------------- | :---------: | :---: | :---: | :---: | :--------: | :------: |
| **General Permissions**                    |             |       |       |       |            |          |
| View Channels                              |      ✅      |   ✅   |   ✅   |   ✅   |     ✅      |    ✅     |
| Manage Channels                            |      ➖      |   ➖   |   ➖   |   ➖   |     ➖      |    ✅     |
| Manage Roles                               |      ➖      |   ➖   |   ➖   |   ✅   |     ➖      |    ✅     |
| Create Expressions                         |      ✅      |   ✅   |   ✅   |   ➖   |     ✅      |    ✅     |
| Manage Expressions                         |      ➖      |   ➖   |   ✅   |   ➖   |     ✅      |    ✅     |
| View Audit Log                             |      ➖      |   ➖   |   ➖   |   ➖   |     ➖      |    ✅     |
| Manage Webhooks                            |      ➖      |   ➖   |   ➖   |   ➖   |     ➖      |    ✅     |
| Manage Server                              |      ➖      |   ➖   |   ➖   |   ✅   |     ➖      |    ✅     |
| **Membership Permissions**                 |             |       |       |       |            |          |
| Create Invite                              |      ➖      |   ➖   |   ➖   |   ➖   |     ➖      |    ✅     |
| Change Nickname                            |      ➖      |   ➖   |   ➖   |   ✅   |     ➖      |    ✅     |
| Manage Nicknames                           |      ➖      |   ➖   |   ➖   |   ✅   |     ➖      |    ✅     |
| Kick Members                               |      ➖      |   ➖   |   ✅   |   ➖   |     ✅      |    ✅     |
| Ban Members                                |      ➖      |   ➖   |   ✅   |   ➖   |     ✅      |    ✅     |
| Timeout Members                            |      ➖      |   ✅   |   ✅   |   ➖   |     ✅      |    ✅     |
| **Text Channel Permissions**               |             |       |       |       |            |          |
| Send Messages                              |      ✅      |   ✅   |   ✅   |   ✅   |     ✅      |    ✅     |
| Send Messages in Threads                   |      ✅      |   ✅   |   ✅   |   ✅   |     ✅      |    ✅     |
| Create Public Threads                      |      ✅      |   ✅   |   ✅   |   ✅   |     ✅      |    ✅     |
| Create Private Threads                     |      ➖      |   ➖   |   ➖   |   ✅   |     ➖      |    ✅     |
| Embed Links                                |      ✅      |   ✅   |   ✅   |   ✅   |     ✅      |    ✅     |
| Attach Files                               |      ✅      |   ✅   |   ✅   |   ✅   |     ✅      |    ✅     |
| Add Reactions                              |      ✅      |   ✅   |   ✅   |   ✅   |     ✅      |    ✅     |
| Use External Emoji                         |      ✅      |   ✅   |   ✅   |   ✅   |     ✅      |    ✅     |
| Use External Stickers                      |      ✅      |   ✅   |   ✅   |   ✅   |     ✅      |    ✅     |
| Mention `@everyone`, `@here` and All Roles |      ➖      |   ➖   |   ✅   |   ➖   |     ✅      |    ✅     |
| Manage Messages                            |      ➖      |   ➖   |   ✅   |   ✅   |     ✅      |    ✅     |
| Manage Threads                             |      ➖      |   ➖   |   ✅   |   ✅   |     ✅      |    ✅     |
| Read Message History                       |      ✅      |   ✅   |   ✅   |   ✅   |     ✅      |    ✅     |
| Send TTS Messages                          |      ➖      |   ➖   |   ➖   |   ➖   |     ➖      |    ➖     |
| Send Voice Messages                        |      ➖      |   ➖   |   ➖   |   ➖   |     ➖      |    ➖     |
| Create Polls                               |      ✅      |   ✅   |   ✅   |   ✅   |     ✅      |    ✅     |
| **Voice Channel Permissions**              |             |       |       |       |            |          |
| Connect                                    |      ✅      |   ✅   |   ✅   |   ➖   |     ✅      |    ✅     |
| Speak                                      |      ✅      |   ✅   |   ✅   |   ➖   |     ✅      |    ✅     |
| Video                                      |      ✅      |   ✅   |   ✅   |   ➖   |     ✅      |    ✅     |
| Use Soundboard                             |      ➖      |   ➖   |   ➖   |   ➖   |     ➖      |    ➖     |
| Use External Sounds                        |      ➖      |   ➖   |   ➖   |   ➖   |     ➖      |    ➖     |
| Use Voice Activity                         |      ✅      |   ✅   |   ✅   |   ➖   |     ✅      |    ✅     |
| Priority Speaker                           |      ➖      |   ➖   |   ✅   |   ➖   |     ✅      |    ✅     |
| Mute Members                               |      ➖      |   ✅   |   ✅   |   ➖   |     ✅      |    ✅     |
| Deafen Members                             |      ➖      |   ➖   |   ✅   |   ➖   |     ➖      |    ✅     |
| Move Members                               |      ➖      |   ➖   |   ✅   |   ➖   |     ➖      |    ✅     |
| Set Voice Channel Status                   |      ✅      |   ✅   |   ✅   |   ➖   |     ✅      |    ✅     |
| **Apps Permissions**                       |             |       |       |       |            |          |
| Use Application Commands                   |      ✅      |   ✅   |   ✅   |   ➖   |     ✅      |    ✅     |
| Use Activities                             |      ✅      |   ✅   |   ✅   |   ➖   |     ✅      |    ✅     |
| Use External Apps                          |      ✅      |   ✅   |   ✅   |   ➖   |     ✅      |    ✅     |
| **Events Permissions**                     |             |       |       |       |            |          |
| Create Events                              |      ✅      |   ✅   |   ✅   |   ✅   |     ✅      |    ✅     |
| Manage Events                              |      ➖      |   ➖   |   ✅   |   ✅   |     ✅      |    ✅     |
| **Administrator**                          |      ➖      |   ➖   |   ➖   |   ➖   |     ➖      |    ✅     |

## Server Rules

```markdown
This is a place for students to hang out, study, chill, and engage in activities. Everyone is welcome, but please follow our guidelines to ensure a positive experience for all. Violating the rules may result in revoked access to the lab.

**Rules:**
**1. Closing Hours:** Ericsson Space closes at 23:00. Do not stay in the lab after closing time.
**2. Food:** Only wrapped candy or bars are allowed in the lab; other food is prohibited.
**3. Drinks:** Water is allowed. Other drinks are permitted as long as they are in resealable containers. Alcohol is not allowed.
**4. Noise Level:** Respect each other by keeping noise levels down. People may be studying.
**5. Tidyness:** Return all chairs to their desks after use. Keep walkways and workspaces clear.
**6. Consoles:** Handle all gaming controls for PS4 and PS5 with care. Return them to the charging stations after use.
**7. Cables:** Do not unplug or move cables. If any cables are missing, contact the labrats.
**8. Contact:** If Ericsson Space is messy, equipment is damaged, or anything is missing, notify `@Lab Rat` to address the issue quickly.

To **accept** these rules, write your name here 👉 {_thread_}
```

## Server Onboarding

This is a discord feature for moderators to handle incoming new members. The Onboarding feature has 5 setup stages to it and we will go through them here.

### 1. Safety Check

In **DM and Spam Protection** there is "_Members must accept rules before they can talk or DM_" configuration. This should be disabled as we already have a `#rules` channel and with Onboarding you can only see the rules once. It could be usefull for c"common sense" rules like do not send adult content, or do not spam, etc. Might be a consideration if someone is really rude, but for now `#rules` should be enough.

### 2. Deafult Channels

The default channels for new comers will be the following categories categories:

- INFORMATION
- LAB
- GROUPS

### 3. Customization Questions

**Pre-join Questions** will be which program the members is studying. It will include both [`Study Programs` and `Lab Visitors` roles](#server-roles). An answer is required and only one is allowed.

- `@sample role` **Sample Answer** Sample Description
- `@SE-BSc` **Software Engineering** Software Engineering
- `@SE-MSc` **Civilingenjör i mjukvaruutveckling** Master of Science in Engineering: Software
Engineering
- `@Sec-BSc` **Högskoleingenjör i IT-säkerhet** Bachelor of Science in Engineering: Computer
Security
- `@Sec-MSc` **Civilingenjör i datorsäkerhet** Master of Science in Engineering: Computer
Security
- `@AI Study` **AI programmet** AI studies
- `@Web Study` **Webbutveckling** Web studies
- `@Game Study` **Spelutveckling** Game studies
- `@Other Study` **Annat program** Other studies
- `@BTH` **Anställd på BTH** BTH Employee
- `@Visitor` **Bara Besöker** Only Visiting

**Post-join Questions** will be [`Hobby Groups` roles](#server-roles) that people can join to get notified about their activities.

### 4. Server Guide

**Welcome Sign** is an automated welcome message sent to new members. A user needs the _Manage Roles_ and _Manage Server_ permissions to be an author. This is a perfect place to utilize Rat King to greet our new members to the lab.

```text
Welcome [@username] to the Ericsson Space Lab!
We’ve created this Discord server as the communication hub for the Space Lab. Here, you can participate in activities and discussions about school, technology, and various projects. The Lab is run by us, the LabRats, so if you have any questions, feel free to reach out by typing @LabRat.
To help you get started, we’ve curated some useful tasks below:
```

**New Member To Do's** consists of 3 to 5 tasks that gets recommended to new members. "Read the rules" is always a task, so technically it is minimum 4 tasks.

- Look at upcoming activities `#announcements`
- Understand the info-hub `#info-hub`
- Check out our equipment `#loan-equipment`
- Visit general chat `#general` (temporary until `#loan-equipment` is functional)
- Read the rules

**Resource Pages** reshapes a chat channel to be more article like. This will be useful for multiple channels in our use case.

- `#rules`
- `#info-hub`
- `#loan-equipment`
- Other program overviews

### 5. Review

Last step in the process. Not much to say here. Review the onboarding configurations and enable the feature.
