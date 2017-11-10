var group;
var boardTiles;
var Board = function(columns, rows, table, karelPos, karelOr) {

  boardTiles = [];
  group = game.add.group();

  for (var y = 0; y < rows; y++) {
    var row = [];
    for (var x = 0; x < columns; x++) {
      if (karelPos[0] == x && karelPos[1] == y) {
        var tile = new Tile(x, y, group, karelOr);
      } else {
        var tile = new Tile(x, y, group, table[y][x]);
      }
      row.push(tile);
    }

    boardTiles.push(row);
  }

  this.moveTo = function(x, y) {
    group.x = x;
    group.y = y;
  };

};
