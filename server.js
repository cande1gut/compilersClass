var http = require('http');
var connect = require('connect');
var serveStatic = require('serve-static');
var PythonShell = require('python-shell');
initWebServer();

function initWebServer() {

  var app = connect().use(serveStatic(__dirname));
  var server = http.createServer(app);
  var io = require('socket.io').listen(server);

  io.on('connection', function(socket) {

    socket.on('karelCode', function(code) {
      var pyshell = new PythonShell('checkProgram.py');
      var karelCode = code.karelInput;
      pyshell.send(JSON.stringify(karelCode));
      pyshell.on('message', function(message) {
        socket.emit('printable', {
          printable: message
        });
      });
      pyshell.end(function(err) {
        if (err) {
          throw err;
        };

        console.log('finished');
      });
    });

    socket.on('depQ', function(depm) {
      db.cypherQuery("MATCH (n:" + depm.depQ + ") WHERE EXISTS(n.category) RETURN DISTINCT 'node' as element, n.category AS category LIMIT 25 UNION ALL MATCH ()-[r]-() WHERE EXISTS(r.category) RETURN DISTINCT 'relationship' AS element, r.category AS category", function(err, result) {
        if (err) throw err;

        socket.emit('depR', {
          depR: result.data
        });
      });
    });

  });

  server.listen(9000, function() {
    console.log('Server started...');
  });

};
