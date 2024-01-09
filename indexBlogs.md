---
# layout: blogs
permalink: /blogs
title: Blogs
---

talk about the constant post
<p>KEY COMMITS:<br> 
7d977cfa8aba1ec14285059e9325626f8b8f64e4 (budget version of the player setting in case)<br>
41620e1459cb3a3e111f025372111c8d6964bd6b (update board chess)<br>
2772b68255833571d564186479f3a671b367d52a (chat and navbar changes with progress on chess int)<br>
</p>
<a href="_notebooks/2023-11-29-Legalandethicalconcerns.md">hello</a>
<h1>TRIMESTER 1 REFLECTION</h1>
- I started to become more familiar with using vscode or github. I think this type of collaborative way of working will be essential in future coding experiences.
- Overall, the largest part of my takeaway from this trimester is how to work with other to collaborate and produce a product or result that is satisfactory of our original vision. This will definitely be essential in my future 
- The passion project has allowed me to learn a lot about working with backend and frontend. This was probably the largest part of collaboration to literally have two parts come together as one. 
- Although I was mostly frontend, I was able to see how different real life environments operate when it comes to things like this.
- While working on frontend and little bit of backend, I was able to learn how apis and communication between those two parts work.
- The passion project required me to think of ways to solve problems. And through new ways of approaching problems such as brainstorming or developing issues to tackle large projects into smaller sections, I was able to problem solve a lot of the issues.
- Problem solving was essential to my passion project.
- In the future, since I feel like I have the fundamentals down, I think I'll be able to focus more on more advanced concepts to create more learning opportunities from those experiences.
- Overall, I learned most while developing my passion project with my teammates.

<h1>Fixed Errors</h1>
<ul>
    <li style="font-size:15px">
        Image wasn't rendering in:<br>
        <img src="images/image_render_error.png" alt="image_error" style="width:150px;height:80px"><br>
        <img src="images/image_code_error.png" alt="image_code_error" style="width:400px;height:60px"><br><br>
        Fix:<br><br>
        <h4>Fixed the directory</h4>
        <img src="images/image_fix.png" alt="image_code_fix" style="width:500px;height:50px">
    </li>
    <br>
    <li>
        Make isn't working<br>
        Fix:<br>
        <h4>Comment out line 7 in file 'Makefile'</h4>
    </li>
    <br>
    <li>Custom Theme isn't saving on local server
        <br>
        Fix:
        <h4>Make new local server to save changes</h4>
    </li>
    <br>
    <li>The github page leads to incorrect base url
        <br>
        Fix:
        <h4>Change the baseurl in _config.yml</h4>
    </li>
    <br>
    <li>The error "You don't have write permissions for the /var/lib/gems/3.0.0 directory." after trying to install jekyll components
        Fix:
        <h4>Precede it with 'sudo'</h4>
    </li>
</ul>
<h1>Ongoing Errors</h1>
N/A


<h1>Team Teach</h1>
- Worked on the lectures covering functions and classes
- Since I less familiar to OOP, I was able to teach myself and learn a lot about OOP and how this new concept applies to my projects.
- I worked on the parts of the lecture covering the popcorn hacks, the classes, and the hw.
- The part I taught was the classes and how they work. (How is it useful in everyday coding/ what is the purpose?)

<h1>PSEUDO CODE FOR PROJECTS</h1>

> <b>Creating board replica</b><br>
function {<br>
&ensp;    create 2d list<br>
&ensp;for {<br>
&ensp;&ensp;for {<br>
&ensp;&ensp;&ensp;        access the board with corresponding ids and then add it relative to its position to the 2d list<br>
&ensp;&ensp;}<br>
&ensp;}<br>
&ensp;return the list<br>
}

> <b>Sending The Board</b><br>
function {<br>
&ensp; create a dictionary with the updated board, the turn number, black castle chance, and white castle chance    <br>
&ensp; create a post request to post the dictionary to the backend database (the db handles one dictionary at a given moment)<br>
}<br>

> Receiving the Board<br>
function { <br>
&ensp;do a get request that checks whether the current board is different or the same as the gotten board, if equal, skip.<br>
&ensp;set the current board's details with the received data<br>
}<br>
(HAVE THIS CODE RUNNING EVERY 0.1 SECOND IN ORDER TO AUTO UPDATE THE BOARD)

> Updating the Board<br>
function {<br>
    &ensp;for {<br>
        &ensp;&ensp; for every id corresponding to a square on the board, set it as the piece based on the list <br>
    }<br>
}<br>

> Set Color<br>
function {<br>
    &ensp; Assign the user a color to play as
}

> Reset board <br>
function{<br>
&ensp; resets the board with a predefined outline of a board<br>
}<br>

<h1>PLANS FOR PASSION PROJECT</h1>

> What Are we DOin'
- Chat system that works across different devices
- Done by having a database of messages that can have data posted and gotten from it
- This essentially will create a chat system
- Create a chat html page
- Create a chess game that can be played multiplayer

> Chat
- Worked on the html and CSS
- Errors:
- &ensp; I faced errors that were mostly with the css of the project but one thing I did was create a function that takes the chatter to the most recent message.
- &ensp; The css problems included: scaling, text overlapping, or div boxes issues.

> Chess
- Worked on the actual chess logic as well as the multiplayer integration
- The chess board follows simple chess rules
- However, it doesn't calculate or sense checkmates so you have to manually capture the king
- The chess board is integrated into multiplayer by having players choosing a color they want to play as.
- If the chess player is of valid turn and color, it allows the user to make moves that are posted to the database.
- There is a database that keeps track of the most recent chess board positions and the turns and other game logic.
- The functions does a post request every time a piece is moved. 
- In order to stay up to date, the get request runs every 0.1 second.
- The chess board will be copied and sent as the post request
- The received chess board will be applied to the layout of the current board for the database.
- The updated board will be updated on every computer as it is doing a get request every 0.1 second.

<h1>College Board Notes and Corrections</h1>
> Question 17
- What does it mean when it says "digital divide"?
- - The term "digital divide" refers to the gap or disparity in access to and use of digital technologies, such as the internet and digital devices, between different groups or communities. This divide can be based on various factors, including socioeconomic status, geographic location, age, education, and other demographics.
- - I chose all the options as they all sounded plausible to be true of reducing digital divide

> Question 23
- What is redundant rerouting?
- - Redundant routing, also known as network redundancy or routing redundancy, is a networking concept that involves the creation of multiple network paths or routes between devices or network segments. The primary purpose of redundant routing is to enhance network reliability, fault tolerance, and availability by providing alternative paths for data to travel in case of network failures or congestion. Redundant routing can be particularly important in critical or high-availability network environments to minimize downtime and ensure continuous network operation.
- For the question, I put C as my answer which connects P and S in several different ways. I put this because I thought it meant that it could connect it through different pathways.
- The correct answer was B, which connects P to S in only way optional path.
- I understand now because redundant rerouting has the purpose of providing one path between each.

> Question 37
- Comparing code segments to compute average from list
- I got this wrong because I thought program II was unable to provide the intended functionality. It seemed impossible to find the value of the average using that mathematical process.
- But after testing the process with different number values, I have concluded that this method of solving for the average is a possible one.
- So the answer should be that both segments work perfectly fine. 
- But the first option requires more arithmetic processes as it does a calculation every iteration of the while loop. Essentially double the calculations 

> Question 46
-  Infinite loops in undecideable problems
- The answer is A because it is quite impossible to develop a single purpose code that solves all problems or errors that it may encounter when taking in input values.
- I chose A at first because I thought it would be able to determine a way to solve the problem somehow

> Question 47 
- Encrypting and decrypting using public key cryptography
- I wasn't sure what cryptography was
- Cryptography: Cryptography is the science and practice of securing communication and information through the use of codes and ciphers. It is a fundamental technology for protecting data and ensuring the confidentiality, integrity, and authenticity of information in various applications, including secure communication, data storage, and authentication. Cryptography has a long history and plays a crucial role in modern digital security.
- The answer is D because in public cryptography, a message is encrypted with a recipient’s public key and decrypted with the recipient’s private key
- I chose the sender's private key as I thought it would be necessary.
- The choice is wrong because the sender’s private key cannot be used to decrypt the message.

> Question 64
- Cloud computing and the Internet
- Cloud Computing: Cloud computing refers to the delivery of computing services, including storage, processing, networking, and software applications, over the internet. Instead of organizations or individuals managing their own physical servers and infrastructure, they can access and use these resources on a pay-as-you-go basis from cloud service providers. 
- Internet: The internet is a global network of interconnected computer networks. It allows the exchange of data and information between devices and users worldwide. The internet is a vast infrastructure that enables various services and activities, including communication, information sharing, e-commerce, and much more.
- I chose option D, which is wrong. It is wrong because cloud storage sites allow users to share files easily, which could lead to increased concerns about copyrighted materials being illegally distributed online. So basically it is counterintuitive
- The correct option is B because cloud computing has more easily available sharing, communicating, and collaborating between users.
- Easier way to share files and tools


> Question 65 
- Correcting errors in procedure Multiply
- I chose A, which is incorrect because if x and y are both positive, the procedure will correctly calculate the product by adding x to itself y times.
- The correct option is D because if y is negative, then the condition count equals y will never be met since count begins at 0 and repeatedly increases.
- I got this wrong due to the lack of predicting the outcome of program.


<h1>College Board Study Topics</h1>
<h3>Things I have issues with</h3>

- Review simulations and their fundamentals
- Review data compression

