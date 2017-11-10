var game = new Phaser.Game(document.getElementById("karel-board").offsetWidth, window.innerHeight, Phaser.AUTO, 'karel-board', {
  init: init,
  preload: preload,
  create: create
});

var gameProperties = {
  screenWidth: document.getElementById("karel-board").offsetWidth,
  screenHeight: window.innerHeight,

  tileWidth: 32,
  tileHeight: 32,

  boardWidth: 0,
  boardHeight: 0,

  backgroundColor: "#FFFFFF",
};

var graphicAssets = {
  tile: {
    URL: 'assets/tiles2.png',
    name: 'tile',
    frames: 4
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

fileInput.addEventListener('change', function(e) {
  e.preventDefault();
  var file = fileInput.files[0];
  var textType = /text.*/;

  if (file.type.match(textType)) {
    var reader = new FileReader();

    reader.onload = function(e) {
      table = reader.result;
      table = table.split("\n");
      for (var i = 0; i < table.length; i++) {
        table[i] = table[i].split(" ");
      }
      table.pop();
      gameProperties.boardWidth = table[0].length;
      gameProperties.boardHeight = table.length;
      for (var i = 0; i < gameProperties.boardWidth; i++) {
        for (var j = 0; j < gameProperties.boardHeight; j++) {
          if (table[i][j] == "n" || table[i][j] == "s" || table[i][j] == "e" || table[i][j] == "o") {
            karelPos[0] = i;
            karelPos[1] = j;
            karelOr = table[i][j];
            table[i][j] = "-";
          }
        }
      }
      restartBoard();
      init();
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

function initBoard() {
  board = new Board(gameProperties.boardWidth, gameProperties.boardHeight, table, karelPos, karelOr);
  board.moveTo(boardLeft, boardTop);
  game.stage.backgroundColor = gameProperties.backgroundColor;
}

function refreshBoard() {
  board = new Board(gameProperties.boardWidth, gameProperties.boardHeight, table, karelPos, karelOr);
}

function restartBoard() {
  game.world.removeAll()
}
