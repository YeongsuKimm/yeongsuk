---
layout: default
title: Student Blog

---
<a href="_posts/2023-11-27-Internet.md"><a>


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
<!-- <p style="float:center;clear:center;display:block;text-align:center"><img src="images/about_me.png" alt="about-me" style="width:80%"></p> -->
<!-- <div>    
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
</div> -->
<br><br><br>
<!-- <form>
    <input type="text" id="noteContent" placeholder="Enter Note Content" name="note">
    <input type="submit" class="note_button" id="noteSubmit" placeholder="Enter Note Content" value="Sumit Note">
</form> -->
<br><br>
<button class="note_button" onclick="createItem()">Create Note</button>
<button class="note_button" onclick="clearList()">Clear Notepad</button>

<div class="notepad">
    <h1 style="color:white">Notepad</h1>
    <ol id="note">
    </ol>
</div>
<html>
    <head>
        <style>
            .note_button {
                color:white;
                padding:9px 13px; 
                background-color:#36393F;
                transition-duration:0.4s;
                border-radius:8px;
            }
            .note_button:hover {
                background-color:gray;
            }
            .button_above:hover {
                background-color:gray;
            }
            .button_above {
                border:black;
                transition-duration:0.4s;
                width:210px;
                height:50px;
                border-radius:8px;
                background-color:#36393F;
                /* font-weight:bold; */
                font-size:30px;
                color:white;
                text-shadow: 0 0 1px black, 0 0 3px black;
                outline: solid black;
                outline-width:1px;
                /* gap:100px; */
            }
            .notepad {
                color:white;
                background-color:#36393F;
                padding:5px 25px 75px;
                border-radius:25px;
            }
        </style>
    </head>
    <body>
        <script>
            function createItem() {
                // Prompt the user for a note item
                var item =  prompt("Enter a to-do item:")
                // Ensure that the user entered something before proceeding
                if (item !== null && item.trim() !== "") {
                    // Create a new list item
                    var note = document.createElement("li");
                    note.innerHTML = item;
                    // Append the list item to the DOM
                    var location = document.getElementById("note");
                    location.appendChild(note);
                    // Save the note item to localStorage
                    saveItemToLocalStorage(item);
                }
            }
            function saveItemToLocalStorage(item) {
                // Retrieve the existing notes from localStorage (if any)
                var existingNotes = JSON.parse(localStorage.getItem("notes")) || [];
                // Add the new note to the array of notes
                existingNotes.push(item);
                // Save the updated array back to localStorage
                localStorage.setItem("notes", JSON.stringify(existingNotes));
            }
            // Load saved notes from localStorage when the page loads
            function loadNotes() {
                var location = document.getElementById("note");
                var existingNotes = JSON.parse(localStorage.getItem("notes")) || [];
                existingNotes.forEach(function (item) {
                    var note = document.createElement("li");
                    note.innerHTML = item;
                    location.appendChild(note);
                });
            }
            function clearList() {
                localStorage.removeItem("notes");
                var location = document.getElementById("note");
                location.innerHTML = "";
            }
            // Call loadNotes() when the page loads to populate existing notes
            window.onload = loadNotes;
        </script>
    </body>
</html>

