const http = require('http');
const { execFile } = require('child_process');
http
  .createServer((_req, res) => {
    execFile('python3', ['hello.py'], (err, stdout, stderr) => {
      res.writeHead(err ? 500 : 200, { 'content-type': 'text/plain' });
      res.end(err ? 'python failed: ' + (stderr || err.message) : 'node says: ' + stdout);
    });
  })
  .listen(Number(process.env.PORT) || 3000, '0.0.0.0');
