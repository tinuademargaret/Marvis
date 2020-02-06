//Client-side Javascript code for handling random numbers
$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/marvis');
    //receive details from server
    socket.on('result', function(msg) {
        console.log("Received result");
        //maintain a list of ten numbers

        $('#log').html(msg.data);
    });
});
