const dgram = require('dgram');
const Recserver = dgram.createSocket('udp4');


var recMsg = Buffer.from('as');
var sendMsg = Buffer.from('sa');


server.on('error', (err) => {
  console.log(`server error:\n${err.stack}`);
  server.close();
});

server.on('message', (msg, rinfo) => {
  console.log(`server got: ${msg} from ${rinfo.address}:${rinfo.port}`);
    if(msg.toString() === 'sa') {
        server.send(recMsg ,rinfo.port,rinfo.address, function(error) {
            if(error){
                client.close();
            }else{
                console.log('Data sent !!!');
            }
        });
    }else{
        console.log("Invalid msg!");
    }
});

server.bind(3131);
// Prints: server listening 0.0.0.0:3131

const client = dgram.createSocket("udp4");

setTimeout(() => {
    let array = []
    client.bind(3132);
    function send_and_wait(socket, n) {
        if (n!==0){
            let start = Date.now()
            socket.on("message", (message) => {
                let end = Date.now()
                array.push(start-end); //date - date

                send_and_wait()
            });
            // send the message
        } else {
            // save the rtts
        }
    }

    send_and_wait(client, 1000);
}, 20 * 1000);
