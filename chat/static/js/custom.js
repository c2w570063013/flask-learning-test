$(document).ready(function () {

    //initial socket
    var socket = io.connect('http://127.0.0.1:5000');

    socket.on('connect', function () {
        socket.send('User has connected');
    });

    socket.on('message', function (msg) {
        let searchParams = new URLSearchParams(window.location.search);
        let param = searchParams.get('key');
        if (msg.indexOf(param) >= 0) {
            console.log('shit');
        } else {
            length_ = msg.indexOf('<!*!>') + 5;
            msg = msg.substring(length_);
            console.log(msg.indexOf('<!*!>'));
            var element2 = "<div class='d-flex justify-content-start mb-4'><div class='img_cont_msg'><img src='static/img/profile.jpg' class='rounded-circle user_img_msg'></div><div class='msg_cotainer'>" + msg + "<span class='msg_time'>9:00 AM, Today</span></div></div>";
            $(".msg_card_body").append(element2);
            $("#messageBody").animate({scrollTop: 20000000}, "slow");
        }
    });
    $("#sendbutton").on('click', function () {
        var content = $("#myMessage").val();
        var content_ = content.trim(' ');
        if (content_.length == 0) {
            return false;
        }
        let searchParams = new URLSearchParams(window.location.search);
        let param = searchParams.get('key');
        socket.send(param + '<!*!>' + content_);
        $("#myMessage").val('');
        //show messages on the chatting board
        var element = "<div class='d-flex justify-content-end mb-4'><div class='msg_cotainer_send'>" + content_ + "<span class='msg_time_send'>8:55 AM, Today</span></div><div class='img_cont_msg'><img src='static/img/profile2.jpg' class='rounded-circle user_img_msg'></div></div>";
        $(".msg_card_body").append(element);
        //scroll down
        // $("html, body").animate({scrollTop: $(document).height()}, 1000);
        $("#messageBody").animate({scrollTop: 20000000}, "slow");
    });
    $("#myMessage").keypress(function (e) {
        if (e.keyCode == 13 && !e.shiftKey) {
            $('#sendbutton').click();
            return false;
        } else {
            return true;
        }
    })
})