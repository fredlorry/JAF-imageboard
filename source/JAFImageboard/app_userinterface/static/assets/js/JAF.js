function messageHTMLConstructor(messageId, messageText, messageDate, messageURL) {
    if (messageDate == undefined) {
        messageDate = Date();
    };
    document.getElementById("Message list").innerHTML += 
        '<hr> \
            <span class="label label-default"> \
                <h4>#' + messageId +
                    '; <small>'
                    +   messageDate    +
                    '</small> \
                </h4> \
            </span> \
            <p class="carrot">' + messageText + '</p> \
        <hr>';
        if (messageURL.length) {
            document.getElementById("Message list").innerHTML += 
                '<img src="' + messageURL + '"> \
                <hr>';
        }
    return;
}

$(document).ready(function(){

    $('#id_text').addClass('form-control form-control-carrot form-control-carrot-msg');
    $('#id_pic_rel').wrap('<label class="label label-default carrot" </label>');
    $('#id_pic_rel')["style"] = 'display: none;';

    $("#newMessageForm").on("submit", function(event) {
        event.preventDefault();
        $.ajax({
            type: "POST",
            url: window.location.pathname,
            data: new FormData( this ),
            processData: false,
            contentType: false,
            beforeSend: function() {
                $(this).hide();
            },
            success: function(data) {
                if ($("#uselessMessage").length > 0) {
                    $("#uselessMessage").remove();
                };
                for (i = 0; i < data.length; i++) {
                    messageHTMLConstructor(data[i].id, data[i].text, data[i].date, data[i].url);
                    if (i == data.length - 1) {
                        document.getElementById("last_msg_id")["value"] = data[i].id;
                    }
                }
                document.getElementById("id_text")["value"] = "";
                document.getElementById("id_pic_rel")["value"] = "";
                $(this).show();
            }
        })
    });

    $("#refreshButton").on("click", function(event) {
        event.preventDefault();
        if ($("#uselessMessage").length > 0) {
            $("#uselessMessage").remove();
        };
        $.ajax({
            type: "POST",
            url: window.location.pathname,
            data: {
                last_msg_id : document.getElementById("last_msg_id")["value"],
                csrfmiddlewaretoken : document.getElementsByName("csrfmiddlewaretoken")[0]["value"],
            },
            success: function(data) {
                for (i = 0; i < data.length; i++) {
                    messageHTMLConstructor(data[i].id, data[i].text, data[i].date, data[i].url);
                    if (i == data.length - 1) {
                        document.getElementById("last_msg_id")["value"] = data[i].id;
                    }
                }
            }
        })
    });
});