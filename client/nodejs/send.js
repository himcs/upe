const dgram = require('dgram');

const port = 5005
const address = '127.0.0.1'
const client = dgram.createSocket('udp4');

function send(msg) {
    const message = Buffer.from('' + msg);
    client.send(message, port, address,);
}

module.exports = send
