var Tile = function(column, row, group, type) {

  var currentFrame;

  switch (type) {
    case "-":
      currentFrame = 0;
      break;
    case "p":
      currentFrame = 1;
      break;
    case "1":
      currentFrame = 2;
      break;
    case "2":
      currentFrame = 2;
      break;
    case "3":
      currentFrame = 2;
      break;
    case "4":
      currentFrame = 2;
      break;
    case "5":
      currentFrame = 2;
      break;
    case "6":
      currentFrame = 2;
      break;
    case "7":
      currentFrame = 2;
      break;
    case "8":
      currentFrame = 2;
      break;
    case "9":
      currentFrame = 2;
      break;
    case "n":
      currentFrame = 3;
      break;
    case "s":
      currentFrame = 3;
      break;
    case "e":
      currentFrame = 3;
      break;
    case "o":
      currentFrame = 3;
      break;
  }

  var sprite = game.add.sprite(column * gameProperties.tileWidth, row * gameProperties.tileHeight, graphicAssets.tile.name, currentFrame, group);

};
