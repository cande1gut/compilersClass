var socket = io();

var game = new Phaser.Game(document.getElementById("karel-board").offsetWidth, window.innerHeight - 135, Phaser.AUTO, 'karel-board', {
  init: init,
  preload: preload,
  create: create
});

var gameProperties = {
  screenWidth: document.getElementById("karel-board").offsetWidth,
  screenHeight: window.innerHeight - 135,

  tileWidth: 64,
  tileHeight: 64,

  boardWidth: 0,
  boardHeight: 0,

  backgroundColor: "#FFFFFF",
};

var graphicAssets = {
  tile: {
    URL: 'assets/frames.png',
    name: 'tile',
    frames: 15
  },
};

function preload() {
  game.load.spritesheet(graphicAssets.tile.name, graphicAssets.tile.URL, gameProperties.tileWidth, gameProperties.tileHeight, graphicAssets.tile.frames);
  game.load.text('text', 'board.txt');
}

var board;
var boardTop;
var boardLeft;

var fileInput = document.getElementById('board-input');
var table;
var karelPos = new Array(2);
var karelOr;
var karelBeepers = 0;
var karelMovements = 0;
var karelLoC = 0;
var active = false;

var karelVelocity = $("#velocity-slider").val();
$('input[type=range]').on('input', function() {
  karelVelocity = $("#velocity-slider").val();
});

$("#bottom-panel,#karelBoard").hide();

var stack = new Array();
var ic;
var chosen = false;

$("#ejecutar").on("click", function() {
  active = true;
  var code = $("#code").val();
  if (chosen) {
    if (code == "") {
      toastError("Please type some valid code");
    } else {
      socket.emit('karelCode', {
        karelInput: code
      });
      karelLoC = 0;
      karelMovements = 0;
      $("#loc").html(karelLoC);
      $("#movements").html(karelMovements);
    }
  } else {
    toastError("Please choose a valid board");
  }
});

$("#reiniciar").on("click", function() {
  active = false;
  karelBeepers = 0;
  karelLoC = 0;
  karelMovements = 0;
  $("#loc").html(karelLoC);
  $("#movements").html(karelMovements);
  $("#beepers").html(karelBeepers);
  var textType = /text.*/;
  var file = fileInput.files[0];
  if (file.type.match(textType)) {
    var reader = new FileReader();

    reader.onload = function(e) {
      table = reader.result;
      table = table.split("\n");
      for (var i = 0; i < table.length; i++) {
        table[i] = table[i].split(" ");
      }
      table.pop();
      /*var lengthTable = table.length[0];
      for (var i = 1; i < table.length; i++) {
        if (table[i].length != lengthTable) {
          toastError("Invalid Board Size");
          break;
        }
      }
      return;*/
      gameProperties.boardWidth = table[0].length;
      gameProperties.boardHeight = table.length;
      //aqui cambie todos los is y js por x y y, asi siempre x se refiere a columnas y y a filas
      //y table siempre será table[y][x] porque primero son arreglos de "filas" y el segundo ya son las columnas, por eso en board.js estaban al reves, pero ya todo esta bien. :*
      for (var x = 0; x < gameProperties.boardWidth; x++) {
        for (var y = 0; y < gameProperties.boardHeight; y++) {
          if (table[y][x] == "n" || table[y][x] == "s" || table[y][x] == "e" || table[y][x] == "o") {
            karelPos[0] = x;
            karelPos[1] = y;
            karelOr = table[y][x];
            table[y][x] = "-";
          }
        }
      }
      loadNewBoard();
      init();
    }

    reader.readAsText(file);
  } else {
    alert("Algo anda mal con el archivo");
  }
});

socket.on('printable', function(ci) {
  if (ci.printable[0] == "[") {
    ic4 = ci.printable;
    ic3 = ic4.slice(1, -1);
    ic2 = ic3.replace(/[, ]+/g, " ");
    ic = ic2.split(" ");
    for (var i = 0; i < ic.length; i++) {
      ic[i] = parseInt(ic[i]);
    }
    console.log(ic4);
    sleep(karelVelocity).then(() => {
      semantic(ic, 0);
    });
  } else {
    Materialize.toast(ci.printable, 3000, 'rounded');
  }
});

function toastError(error) {
  Materialize.toast(error, 3000, 'rounded');
}

//aqui es cuando de alguna forma con los sockets creamos IC con lo que regrese

//put-pick beepers test
//var ic = [100, 2, 1000, 1000, 2000, 1000, 1000, 1000, 3000, 3000, 1000, 2000, 1000, 1000, 1000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 1000, 2000, 4000, 1000, 4000, 4000, 1000, 4000, 4000, 4000, 1000, 4000, 4000, 4000, 4000, 1000, 1000, 1000, 5000];

//if-while test
//var ic = [100, 2, 6000, 6018, 100, 16, 6000, 6004, 100, 13, 2000, 100, 14, 1000, 100, 2, 5000];

//iterate test
//var ic = [100, 2, 6000, 20, 100, 23, 6000, 6004, 100, 13, 2000, 100, 21, 1000, 6000, 6007, 100, 21, 3000, 100, 14, 100, 2, 5000];

//functions test
//var ic = [100, 12, 2000, 2000, 2000, 200, 1000, 1000, 1000, 300, 2, 200, 1000, 300, 6, 1000, 5000];

fileInput.addEventListener('change', function(e) {
  e.preventDefault();
  var file = fileInput.files[0];
  var textType = /text.*/;

  if (file.type.match(textType)) {
    var reader = new FileReader();
    chosen = true;
    reader.onload = function(e) {
      table = reader.result;
      table = table.split("\n");
      for (var i = 0; i < table.length; i++) {
        table[i] = table[i].split(" ");
      }
      table.pop();
      gameProperties.boardWidth = table[0].length;
      gameProperties.boardHeight = table.length;
      //aqui cambie todos los is y js por x y y, asi siempre x se refiere a columnas y y a filas
      //y table siempre será table[y][x] porque primero son arreglos de "filas" y el segundo ya son las columnas, por eso en board.js estaban al reves, pero ya todo esta bien. :*
      for (var x = 0; x < gameProperties.boardWidth; x++) {
        for (var y = 0; y < gameProperties.boardHeight; y++) {
          if (table[y][x] == "n" || table[y][x] == "s" || table[y][x] == "e" || table[y][x] == "o") {
            karelPos[0] = x;
            karelPos[1] = y;
            karelOr = table[y][x];
            table[y][x] = "-";
          }
        }
      }
      loadNewBoard();
      init();
      $("#bottom-panel,#karelBoard").show();
    }

    reader.readAsText(file);
  } else {
    alert("Algo anda mal con el archivo");
  }
});

function init() {
  boardTop = (gameProperties.screenHeight - (gameProperties.tileHeight * gameProperties.boardHeight)) * 0.5;
  boardLeft = (gameProperties.screenWidth - (gameProperties.tileWidth * gameProperties.boardWidth)) * 0.5;
  initBoard();
}

function create() {

}

function update() {

}

function semantic(ic, actual) {
  if (active) {
    karelLoC++;
    $("#beepers").html(karelBeepers);
    $("#loc").html(karelLoC);
    $("#movements").html(karelMovements);
    if (actual < ic.length) {
      switch (ic[actual]) {
        // jump
        case 100:
          semantic(ic, ic[actual + 1]);
          break;
          // move
        case 1000:
          if (frontIsClear()) {
            move();
            refreshBoard();
            sleep(karelVelocity).then(() => {
              karelMovements++;
              semantic(ic, actual + 1);
            });
          } else {
            toastError('Semantic-Error: No space ahead');
          }
          break;
          // turnLeft
        case 2000:
          turnLeft();
          refreshBoard();
          sleep(karelVelocity).then(() => {
            karelMovements++;
            semantic(ic, actual + 1);
          });
          break;
          // pickBeeper
        case 3000:
          if (table[karelPos[1]][karelPos[0]] != "-") {
            pickBeeper();
            sleep(karelVelocity).then(() => {
              karelMovements++;
              semantic(ic, actual + 1);
            });
          } else {
            toastError('Semantic-Error: No beepers to pick');
          }
          break;
          // putBeeper
        case 4000:
          if (karelBeepers == 0) {
            toastError('Semantic-error: No beepers to put');
          } else if (table[karelPos[1]][karelPos[0]] == "9") {
            toastError('Semantic-Error: No more space to put beeper');
          } else {
            putBeeper();
            sleep(karelVelocity).then(() => {
              karelMovements++;
              semantic(ic, actual + 1);
            });
          }
          break;
          // end
        case 5000:
          toastError('Program finished without errors');
          break;
          // if
        case 6000:
          if (evaluate(Number(ic[actual + 1]), ic, actual)) {
            semantic(ic, actual + 4);
          } else {
            semantic(ic, actual + 2);
          }
          break;
          // call
        case 300:
          stack.push(actual + 2);
          semantic(ic, ic[actual + 1]);
          break;
          // ret
        case 200:
          semantic(ic, stack.pop());
          break;
      }
    } else {
      console.log("end");
      toastError('Semantic-Error: No end statement');
    }
  }
}

function move() {
  switch (karelOr) {
    case "n":
      karelPos[1]--;
      break;
    case "e":
      karelPos[0]++;
      break;
    case "s":
      karelPos[1]++;
      break;
    case "o":
      karelPos[0]--;
      break;
  }
}

function turnLeft() {
  switch (karelOr) {
    case "n":
      karelOr = "o";
      break;
    case "e":
      karelOr = "n";
      break;
    case "s":
      karelOr = "e";
      break;
    case "o":
      karelOr = "s";
      break;
  }
}

function pickBeeper() {
  var currentBeepers = Number(table[karelPos[1]][karelPos[0]]);
  if (currentBeepers == 1) {
    table[karelPos[1]][karelPos[0]] = "-";
  } else {
    table[karelPos[1]][karelPos[0]] = (currentBeepers - 1).toString();
  }
  karelBeepers++;
  console.log("Beepers: " + karelBeepers);
}

function putBeeper() {
  if (table[karelPos[1]][karelPos[0]] == "-") {
    table[karelPos[1]][karelPos[0]] = "1";
  } else {
    table[karelPos[1]][karelPos[0]] = (Number(table[karelPos[1]][karelPos[0]]) + 1).toString();
  }
  karelBeepers--;
  console.log("Beepers: " + karelBeepers);
}

function frontIsClear() {
  switch (karelOr) {
    case "n":
      if (karelPos[1] - 1 < 0) {
        return false;
      } else {
        return (table[karelPos[1] - 1][karelPos[0]] != "p");
      }
    case "e":
      if (karelPos[0] + 1 >= gameProperties.boardWidth) {
        return false;
      } else {
        return table[karelPos[1]][karelPos[0] + 1] != "p";
      }
    case "s":
      if (karelPos[1] + 1 >= gameProperties.boardHeight) {
        return false;
      } else {
        return table[karelPos[1] + 1][karelPos[0]] != "p";
      }
    case "o":
      if (karelPos[0] - 1 < 0) {
        return false;
      } else {
        return table[karelPos[1]][karelPos[0] - 1] != "p";
      }
  }
}

function leftIsClear() {
  turnLeft();
  var conditionState = frontIsClear();
  turnLeft();
  turnLeft();
  turnLeft();
  return conditionState;
}

function rightIsClear() {
  turnLeft();
  turnLeft();
  turnLeft();
  var conditionState = frontIsClear();
  turnLeft();
  return conditionState;
}

function evaluate(condition, ic, actual) {
  switch (condition) {
    case 6001:
      return frontIsClear();
    case 6002:
      return leftIsClear();
    case 6003:
      return rightIsClear();
    case 6004:
      return !frontIsClear();
    case 6005:
      return !leftIsClear();
    case 6006:
      return !rightIsClear();
    case 6007:
      return table[karelPos[1]][karelPos[0]] != "-";
    case 6008:
      return table[karelPos[1]][karelPos[0]] == "-";
    case 6009:
      return karelOr == "n";
    case 6010:
      return karelOr == "s";
    case 6011:
      return karelOr == "e";
    case 6012:
      return karelOr == "o";
    case 6003:
      return karelOr != "n";
    case 6014:
      return karelOr != "s";
    case 6015:
      return karelOr != "e";
    case 6016:
      return karelOr != "o";
    case 6017:
      return karelBeepers > 0;
    case 6018:
      return karelBeepers == 0;
    default:
      if (condition == 0) {
        return false;
      } else {
        ic[actual + 1] = (Number(ic[actual + 1]) - 1).toString();
        return true;
      }
  }
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function initBoard() {
  board = new Board(gameProperties.boardWidth, gameProperties.boardHeight, table, karelPos, karelOr);
  board.moveTo(boardLeft, boardTop);
  game.stage.backgroundColor = gameProperties.backgroundColor;
}

function refreshBoard() {
  loadNewBoard();
  board = new Board(gameProperties.boardWidth, gameProperties.boardHeight, table, karelPos, karelOr);
  board.moveTo(boardLeft, boardTop);
}

function loadNewBoard() {
  game.world.removeAll();
}
