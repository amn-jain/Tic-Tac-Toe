let player = "X"
let oponent = "O"
let which_player, Empty, Score;
var board = [];
for(let i = 0; i < 3; i++){
    board.push([" ", " ", " "]);
}

function Toss()
{
    max = 2;
    return Math.floor(Math.random() * Math.floor(max));
}

function display_board(){
    
    for(let row = 0; row < 3; row++){
        for(let col = 0; col < 3; col++){
            board[row][col] = " ";
        }
    }
    
    document.getElementById("zero-zero").innerHTML = "";
    document.getElementById("zero-one").innerHTML = "";
    document.getElementById("zero-two").innerHTML = "";
    document.getElementById("one-zero").innerHTML = "";
    document.getElementById("one-one").innerHTML = "";
    document.getElementById("one-two").innerHTML = "";
    document.getElementById("two-zero").innerHTML = "";
    document.getElementById("two-one").innerHTML = "";
    document.getElementById("two-two").innerHTML = "";

}

function evaluate(board) {
    for (let row = 0; row < 3; row++) {
        if (board[row][0] == board[row][1] && board[row][1] == board[row][2] && board[row][0] != " ") {
            if (board[row][0] == oponent) {
                return 10;
            }
            else {
                return -10;
            }
        }
    }

    for (let col = 0; col < 3; col++) {
        if (board[0][col] == board[1][col] && board[1][col] == board[2][col] && board[0][col] != " ") {
            if (board[0][col] == oponent) {
                return 10;
            }
            else {
                return -10;
            }
        }
    }

    if (board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[0][0] != " ") {
        if (board[0][0] == oponent) {
            return 10;
        }
        else {
            return -10;
        }
    }

    if (board[0][2] == board[1][1] && board[1][1] == board[2][0] && board[0][2] != " ") {
        if (board[0][2] == oponent) {
            return 10;
        }
        else {
            return -10;
        }
    }

    return 0;
}


function isEmpty(board) {
    for (let row = 0; row < 3; row++) {
        for (let col = 0; col < 3; col++) {
            if (board[row][col] == " ") {
                return true;
            }
        }
    }
    return false;
}

function minimizer_maximizer(board, depth, isMaximizer) {
    score = evaluate(board);
    if (score == 10) {
        return 10 - depth;
    }
    else if (score == -10) {
        return depth - 10;
    }

    if (isEmpty(board) == false) {
        return 0;
    }

    if (isMaximizer) {
        let bestScore = -Infinity;
        for (let row = 0; row < 3; row++) {
            for (let col = 0; col < 3; col++) {
                if (board[row][col] == " ") {
                    board[row][col] = oponent;
                    score = minimizer_maximizer(board, depth + 1, !isMaximizer);
                    if (score > bestScore) {
                        bestScore = score;
                    }
                    board[row][col] = " ";
                }
            }
        }

        return bestScore;
    }
    else {
        let bestScore = Infinity;
        for (let row = 0; row < 3; row++) {
            for (let col = 0; col < 3; col++) {
                if (board[row][col] == " ") {
                    board[row][col] = player;
                    score = minimizer_maximizer(board, depth + 1, !isMaximizer);
                    if (score < bestScore) {
                        bestScore = score;
                    }
                    board[row][col] = " ";
                }
            }
        }

        return bestScore;
    }
}

function bestMove(board) {
    let move = null;
    bestScore = -Infinity;
    for (let row = 0; row < 3; row++) {
        for (let col = 0; col < 3; col++) {
            if (board[row][col] == " ") {
                board[row][col] = oponent;
                score = minimizer_maximizer(board, 0, false);
                console.log(score);
                if (score > bestScore) {
                    bestScore = score;
                    move = [row, col];
                }
                board[row][col] = " ";
            }
        }
    }
    if (move != null) {
        let row = move[0]; 
        let col = move[1];
        board[row][col] = oponent;
        let list = [row, col];
        let x = ""
        let y = ""
        for(let i = 0; i < 2; i++){
            switch(list[i]){
                case 0:
                    list[i] = "zero";
                    break;
                case 1:
                    list[i] = "one";
                    break;
                case 2:
                    list[i] = "two";
                    break;
            }
        }
        let id = list[0] + "-" + list[1];
        document.getElementById(id).style.color = "#fcf75e";
        document.getElementById(id).innerHTML = oponent;
    }
    return board;
}

function bot(){
    if(which_player == 0){
        if(level == "Imposible"){
            board = bestMove(board);    
        }
        else{
            board = easy_bot(board);
        }
        Empty = isEmpty(board);
        score = evaluate(board);
        if(Empty && score == 0){
            which_player = 1;
        }
        else{
            if(Empty){
                document.getElementById("banner").innerHTML = "Better Luck Next Time";
            }
            else{
                document.getElementById("banner").innerHTML = "Draw";
            }
        }
    }
}
function playerMove(id) {
    Empty = isEmpty(board);
    score = evaluate(board);
    if(which_player == 1 && Empty && score == 0){
        let list = id.split("-")
        for(let i = 0; i < 2; i++){
            switch(list[i]){
                case "zero":
                    list[i] = 0;
                    break;
                    case "one":
                    list[i] = 1;
                    break;
                    case "two":
                        list[i] = 2;
                    break;
                }
        }
        let row = list[0];
        let col = list[1]; 
        if(board[row][col] == " "){
            document.getElementById(id).style.color = "#ABE6F5";
            document.getElementById(id).innerHTML = player;
            board[row][col] = player;
            score = evaluate(board);
            Empty = isEmpty(board);
            if(score == 0 && Empty){
                which_player = 0;
                bot();
            }
            else{
                if(Empty){
                    document.getElementById("banner").innerHTML = "Winner Winner Chicken Dinner!!!";
                }
                else{
                    document.getElementById("banner").innerHTML = "Draw";
                }
            }
        }
    }
}

let level = "easy"
function level_setter(id){
    level = id;
}

let count = 0;

function easy_bot(board){
    let flag = true;
    while(flag){
        let row = Math.floor(Math.random() * Math.floor(2));
        let col = Math.floor(Math.random() * Math.floor(2));
        if(board[row][col] == " "){
            board[row][col] = oponent;
            flag = false;
            let list = [row, col];
            let x = ""
            let y = ""
            for(let i = 0; i < 2; i++){
                switch(list[i]){
                    case 0:
                        list[i] = "zero";
                        break;
                    case 1:
                        list[i] = "one";
                        break;
                    case 2:
                        list[i] = "two";
                        break;
                }
            }
            let id = list[0] + "-" + list[1];
            document.getElementById(id).style.color = "#fcf75e";
            document.getElementById(id).innerHTML = oponent;
        }
    }
    return board;  
}

function Game(){
    which_player = Toss();
    if(which_player == 1){
        document.getElementById("banner").innerHTML = "Game Difficulty: " + level + "<br>You won the toss!!!";
    }
    else{
        document.getElementById("banner").innerHTML = "Game Difficulty: " + level + "<br>You lose the toss!!!";
    }
    if(count%2 == 0){
        document.getElementById("result").innerHTML = "<h1>Restart Game</h1>";
        if(which_player == 0){
            if(level == "Imposible"){
                board = bestMove(board);
            }
            else{
                board = easy_bot(board);
            }
            Empty = isEmpty(board);
            score = evaluate(board);
            which_player = 1;
        }
    }
    else{
        document.getElementById("result").innerHTML = "<h1>Start Game</h1>";
        document.getElementById("banner").innerHTML = "";
        display_board();
    }
    count++;
}

