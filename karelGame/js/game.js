var gameProperties = {
  screenWidth: document.getElementById("karel-board").offsetWidth,
  screenHeight: window.innerHeight,

  tileWidth: 32,
  tileHeight: 32,

  boardWidth: 0,
  boardHeight: 0,

  totalMines: 10,

  backgroundColor: "#FFFFFF",
};

var states = {
  game: "game",
};

var graphicAssets = {
  tile: {
    URL: 'assets/tile.png',
    name: 'tile',
    frames: 1
  },
};

var gameState = function(game) {
  this.boardTop;
  this.boardLeft;
  this.board;
};

gameState.prototype = {

  init: function() {
    this.boardTop = (gameProperties.screenHeight - (gameProperties.tileHeight * gameProperties.boardHeight)) * 0.5;
    this.boardLeft = (gameProperties.screenWidth - (gameProperties.tileWidth * gameProperties.boardWidth)) * 0.5;
  },

  preload: function() {
    game.load.spritesheet(graphicAssets.tile.name, graphicAssets.tile.URL, gameProperties.tileWidth, gameProperties.tileHeight, graphicAssets.tile.frames);
    game.load.text('text', 'board.txt');
  },

  create: function() {
    //var html = game.cache.getText('text');
    //text = html.split(' ');
    $("#crear").on("click", function(e) {
      this.game.initBoard();
    });
  },

  update: function() {

  },

  updateTable: function() {
    //console.log(this.document.getElementById('tableroX').value);
    //this.gameProperties.boardWidth = document.getElementById('tableroX').value;
    //  this.gameProperties.boadHeight = document.getElementById('tableroY').value;
    //this.initBoard();
    console.log("yes");
  },

  initBoard: function() {
    console.log("changes");
    this.board = new Board(gameProperties.boardWidth, gameProperties.boardHeight);
    this.board.moveTo(this.boardLeft, this.boardTop);
    game.stage.backgroundColor = gameProperties.backgroundColor;
  },

  revealTile: function() {

  },

  flagTile: function() {

  },

  render: function() {},

};

var game = new Phaser.Game(gameProperties.screenWidth, gameProperties.screenHeight, Phaser.AUTO, 'karel-board');
game.state.add(states.game, gameState);
game.state.start(states.game);
