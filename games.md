---
# layout: schedule
units: "1,2,3,4,5,6"
course: Games & Projects
# toc: true
# comments: false
layout: default
title: Games & Projects
# description: Games & Projects
type: hacks
courses: { compsci: {week: 3} }
---
<head>
    <link rel="stylesheet" href="theme.css">
</head>
<h1>Week 0 Projects</h1>
<div class="centered">
    <h1>The Notepad</h1>
    On the home page
</div>
<br><br><br>
<h1>Week 1 Projects</h1>
<!DOCTYPE html>
<html>
<head>
    <style>
        .cal_button {
            background-color: #36393F;
            color: white;
            border-radius: 8px;
            transition-duration: 0.4s;
            font-size: 30px;
            color: white;
            width: 157px;
            height: 100px;
        }
        .cal_button:hover {
            background-color: gray;
        }
        #display {
            text-align: right;
            height: 75px;
            width: 630px;
            font-size: 65px;
        }
        .centered {
            text-align: center;
        }
    </style>
</head>
<body>
<div class="centered">
    <h1>Simple Calculator</h1>
    <input type="text" id="display" disabled><br><br>
    <button onclick="appendToDisplay('7')" class="cal_button">7</button>
    <button onclick="appendToDisplay('8')" class="cal_button">8</button>
    <button onclick="appendToDisplay('9')" class="cal_button">9</button>
    <button onclick="appendToDisplay('+')" class="cal_button">+</button><br>
    <button onclick="appendToDisplay('4')" class="cal_button">4</button>
    <button onclick="appendToDisplay('5')" class="cal_button">5</button>
    <button onclick="appendToDisplay('6')" class="cal_button">6</button>
    <button onclick="appendToDisplay('-')" class="cal_button">-</button><br>
    <button onclick="appendToDisplay('1')" class="cal_button">1</button>
    <button onclick="appendToDisplay('2')" class="cal_button">2</button>
    <button onclick="appendToDisplay('3')" class="cal_button">3</button>
    <button onclick="appendToDisplay('*')" class="cal_button">*</button><br>
    <button onclick="appendToDisplay('0')" class="cal_button">0</button>
    <button onclick="clearDisplay()" class="cal_button">C</button>
    <button onclick="calculateResult()" class="cal_button">=</button>
    <button onclick="appendToDisplay('/')" class="cal_button">/</button><br>
</div>
<script>
    // Add event listeners for keyboard input
    document.addEventListener('keydown', function (event) {
        const key = event.key;
        if (!isNaN(key) || key === '+' || key === '-' || key === '*' || key === '/' || key === '.') {
            appendToDisplay(key);
        } else if (key === 'Enter') {
            calculateResult();
        } else if (key === 'Escape') {
            clearDisplay();
        }
    });
    function appendToDisplay(value) {
        document.getElementById("display").value += value;
    }
    function clearDisplay() {
        document.getElementById("display").value = "";
    }
    function calculateResult() {
        try {
            const expression = document.getElementById("display").value;
            const result = eval(expression);
            document.getElementById("display").value = result;
        } catch (error) {
            document.getElementById("display").value = "Error";
        }
    }
</script>
</body>
</html>
<br><br><br>
<h1>Week 2 Projects</h1>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Word Guessing Game</title>
    <style>
        /* body {
            text-align: center;
        } */
    </style>
</head>
<body>
    <div class="centered"> 
        <h1>Word Guessing Game</h1>
        <p>Guess the word: <span id="word-display"></span></p>
        <p>Guesses left: <span id="guesses-left"></span></p>
        <input type="text" id="guess-input" placeholder="Enter a letter" style="width:100px;height:44px; font-size:15px">
        <button id="guess-button" style="width:50px;height:50px">Guess</button>
        <p id="message"></p>
    </div>
    <script>
        const words = ["advance","soup","refuse", "fill", "excess", "sun", "reference"];
        let selectedWord = "";
        let guessedWord = [];
        let guessesLeft = 6;
        function selectRandomWord() {
            const randomIndex = Math.floor(Math.random() * words.length);
            return words[randomIndex];
        }
        function initializeGame() {
            selectedWord = selectRandomWord();
            guessedWord = Array(selectedWord.length).fill('_');
            guessesLeft = selectedWord.length;
            updateDisplay();
        }
        function updateDisplay() {
            document.getElementById("word-display").textContent = guessedWord.join(" ");
            document.getElementById("guesses-left").textContent = guessesLeft;
        }
        function isGameWon() {
            return guessedWord.indexOf('_') === -1;
        }
        function handleGuess() {
            const guess = document.getElementById("guess-input").value.toLowerCase();
            if (guess.length !== 1 || !/[a-z]/.test(guess)) {
                document.getElementById("message").textContent = "Please enter a single letter.";
                return;
            }
            if (selectedWord.includes(guess)) {
                for (let i = 0; i < selectedWord.length; i++) {
                    if (selectedWord[i] === guess) {
                        guessedWord[i] = guess;
                    }
                }
            } else {
                guessesLeft--;
            }
            document.getElementById("guess-input").value = "";
            updateDisplay();
            if (isGameWon()) {
                document.getElementById("message").textContent = "Congratulations! You won!";
            } else if (guessesLeft === 0) {
                document.getElementById("message").textContent = "Game over. The word was: " + selectedWord;
            }
        }
        window.addEventListener("load", initializeGame);
        document.getElementById("guess-button").addEventListener("click", handleGuess);
    </script>
</body>
</html>
<br><br>


<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tic Tac Toe</title>
    <style>
        /* body {
            font-family: Arial, sans-serif;
            text-align: center;
        } */
        .container {
            display: inline-grid;
            grid-template-columns: repeat(3, 100px);
            gap: 5px;
            margin-top: 20px;
        }
        .cell {
            width: 100px;
            height: 100px;
            font-size: 24px;
            text-align: center;
            vertical-align: middle;
            border: 2px solid #333;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div style="text-align:center"> 
        <h1>Tic Tac Toe</h1>
        <div class="container " id="board">
            <div class="cell" onclick="makeMove(0)"></div>
            <div class="cell" onclick="makeMove(1)"></div>
            <div class="cell" onclick="makeMove(2)"></div>
            <div class="cell" onclick="makeMove(3)"></div>
            <div class="cell" onclick="makeMove(4)"></div>
            <div class="cell" onclick="makeMove(5)"></div>
            <div class="cell" onclick="makeMove(6)"></div>
            <div class="cell" onclick="makeMove(7)"></div>
            <div class="cell" onclick="makeMove(8)"></div>
        </div>
    </div>
    <br><br><br><br>
    <div id="message"></div>
    <script>
        let currentPlayer = 'X';
        let board = ['', '', '', '', '', '', '', '', ''];
        let gameActive = true;
        const winningCombos = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ];
        function makeMove(cellIndex) {
            if (gameActive && board[cellIndex] === '') {
                board[cellIndex] = currentPlayer;
                document.getElementById('board').children[cellIndex].textContent = currentPlayer;
                if (checkWinner(currentPlayer)) {
                    var note = document.createElement("h1");
                    note.innerHTML = `Player ${currentPlayer} wins!`;
                    var location = document.getElementById('message');
                    var space = document.createElement("br")
                    location.appendChild(space);
                    location.appendChild(note);
                    gameActive = false;
                } else if (!board.includes('')) {
                    document.getElementById('message').textContent = "It's a draw!";
                    gameActive = false;
                } else {
                    currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
                }
            }
        }
        function checkWinner(player) {
            for (const combo of winningCombos) {
                if (combo.every(index => board[index] === player)) {
                    return true;
                }
            }
            return false;
        }
    </script>
</body>
</html>
<h1>Week 3 Projects</h1>
<div class="centered">
    <div style="font-size:200%">
        <a href="CHESS/chess.html">Chess Game</a>
        <br><br><br>
    </div>
    <h1>Updated To-Do List</h1>
    On the Home page
</div>


