#!/usr/bin/env node
var cluster = require('cluster');

if (cluster.isMaster) {
  cluster.fork();
  cluster.fork();
  cluster.fork();
  cluster.fork();
} else {
  var http = require('http');
  var MongoClient = require('mongodb').MongoClient;

  MongoClient.connect(
    'mongodb://127.0.0.1:27017/documents',
    function(err, db) {
      http.createServer(function (req, res) {
        db.collection('items').findOne({}, function (err, data) {
          data = data['data']

          res.writeHead(
            200,
            {
              'Content-Type': 'text/plain',
              'Content-Length': data.length
            }
          );
          res.end(data);
        })
      }).listen(7777, '127.0.0.1');
    }
  )
}
