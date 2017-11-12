var Tile = function(column, row, group, type) {

  var currentFrame;

  switch (type) {
    case "1":
      currentFrame = 0;
      break;
    case "2":
      currentFrame = 1;
      break;
    case "3":
      currentFrame = 2;
      break;
    case "4":
      currentFrame = 3;
      break;
    case "5":
      currentFrame = 4;
      break;
    case "6":
      currentFrame = 5;
      break;
    case "7":
      currentFrame = 6;
      break;
    case "8":
      currentFrame = 7;
      break;
    case "9":
      currentFrame = 8;
      break;
  	case "-":
      currentFrame = 9;
      break;
    case "p":
      currentFrame = 10;
      break;
    case "n":
      currentFrame = 11;
      break;
    case "e":
      currentFrame = 12;
      break;
  	case "s":
      currentFrame = 13;
      break;
    case "o":
      currentFrame = 14;
      break;
  }

  var sprite = game.add.sprite(column * gameProperties.tileWidth, row * gameProperties.tileHeight, graphicAssets.tile.name, currentFrame, group);

};
