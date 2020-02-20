$(document).ready(function () {
    var socket_messages = io('http://127.0.0.1:5000/messages');
    var private_socket = io('http://66.42.40.223:8003/private');
    var today = new Date();
    var time = today.getHours() + ":" + today.getMinutes() + ',' + '今天';
    $("#submit_name").on('click', function () {
        var username = $('#username').val();
        private_socket.emit('username', username);
        $("#input_user_").hide();
        var append_element = "<p style='display: block;'>你好: <span id='my_username' style='font-weight: bold'>" + username + "</span></p>";
        $(".user_info").append(append_element);
    });

    $("#recipient_confirm").on('click', function () {
        var recipient = $('#recipient_name').val(),
            message_to_send = $("#my_username").text() + ' connected';
        private_socket.emit('private_message', {'username': recipient, 'message': message_to_send});
        $("#receipt_div").hide();
        var append_element = "<p style='display: block;'>发送者: <span id='recipient_' style='font-weight: bold'>" + recipient + "</span></p>";
        $(".user_info").append(append_element);
    });

    $("#sendbutton").on('click', function () {
        var recipient = $('#recipient_name').val();
        var message_to_send = $('#myMessage').val();
        private_socket.emit('private_message', {'username': recipient, 'message': message_to_send});
        $("#myMessage").val('');
        var element = "<div class='d-flex justify-content-end mb-4'><div class='msg_cotainer_send'>" + message_to_send + "<span class='msg_time_send'>" + time + "<p style='color: white;display: inline'> √</p></span></div><div class='img_cont_msg'><img src='static/img/profile2.jpg' class='rounded-circle user_img_msg'></div></div>";
        $(".msg_card_body").append(element);
        $("#messageBody").animate({scrollTop: 20000000}, "slow");
    });

    private_socket.on('new_private_message', function (msg) {
        if (msg.username != $("#recipient_name").val()) {
            return false;
        }
        var element2 = "<div class='d-flex justify-content-start mb-4'><div class='img_cont_msg'><img src='static/img/profile.jpg' class='rounded-circle user_img_msg'></div><div class='msg_cotainer'>" + msg.message + "<span class='msg_time'>" + time + "</span></div></div>";
        $(".msg_card_body").append(element2);
        $("#messageBody").animate({scrollTop: 20000000}, "slow");
    });

    $("#myMessage").keypress(function (e) {
        if (e.keyCode == 13 && !e.shiftKey) {
            $('#sendbutton').click();
            return false;
        } else {
            return true;
        }
    });
});