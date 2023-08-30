---
layout: default
title: Student Blog

---



<!-- ## Overview of Hacks, Study and Tangibles
Blogging in GitHub pages is a way to learn and code at the same time. 

- Plans, Lists, [Scrum Boards](https://clickup.com/blog/scrum-board/) help you to track key events, show progress and record time.  Effort is a big part of your class grade.  Show plans and time spent!
- [Hacks(Todo)](https://levelup.gitconnected.com/six-ultimate-daily-hacks-for-every-programmer-60f5f10feae) enable you to stay in focus with key requirements of the class.  Each Hack will produce Tangibles.
- Tangibles or [Tangible Artifacts](https://en.wikipedia.org/wiki/Artifact_(software_development)) are things you accumulate as a learner and coder.  -->

<!-- ## MY PAGE -->

<button class="button_above" onclick="window.location.href='https://nighthawkcoders.github.io/teacher/csp';">Schedule</button>
<button class="button_above" onclick="window.location.href='https://poway.instructure.com/courses/141645';">Canvas</button>
<button class="button_above" onclick="window.location.href='https://app.slack.com/client/TUDAF53UJ/CUU064ACX';">Slack</button>

<h2>About Me:</h2>
<p style="float:right;clear:right;display:block;text-align:right"><img src="images/about_me.png" alt="about-me" style="width:220px;height:280px"></p>
<div>    
    <ol style="font-size:15px">
        <li>I was born in South Korea</li>
        <br>
        <li>I have a dog <br><img src="images/dog.jpg" alt = "dog" style="width:70px;height:100px"> </li>
        <br>
        <li>I like music</li>
        <br>
        <li>I play the violin</li>
        <br>
        <li>I enjoy coding<br><img src="images/code.jpg" alt="codeImage" width="280" height="157"></li>
    </ol>
</div>
<br><br><br>
<button class="note_button" onclick="createItem()">Create a note</button>
<h1>Notepad</h1>
<ol id="note">
</ol>

<html>
    <head>
        <!-- <link rel="stylesheet" href="theme.css"> -->
        <style>
            .note_button {
                padding:9px 13px; 
                background-color:#93bd20;
                transition-duration:0.4s;
                border-radius:8px;
            }
            .note_button:hover {
                background-color:white;
            }
            .button_above {
                border:black;
                width:210px;
                height:50px;
                border-radius:8px;
                background-color:#93bd20;
                font-weight:bold;
                font-size:30px;
                color:white;
                text-shadow: 0 0 1px black, 0 0 3px black;
            }
        </style>
    </head>
    <body>
        <script>
            function createItem()
            {
                var note = document.createElement("li");
                var item = prompt("Enter note item");
                note.innerHTML = item;
                // console.log(note);
                var location = document.getElementById("note");
                // note.appendChild(document.createTextNode(item)); -- set item to note
                location.appendChild(note);
            }
        </script>
    </body>
</html>

