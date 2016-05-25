function messageHTMLConstructor(messageId, messageText, messageDate) {
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
    return;
}

$(document).ready(function(){

    $(".label").click( function() {
        $(this).hide();
    });

    $("#newMessageForm").on("submit", function(event) {
        event.preventDefault();
        $.ajax({
            type: "POST",
            url: window.location.pathname,
            data: $(this).serialize(),
            beforeSend: function() {
                $(this).hide();
            },
            success: function(data) {
                for (i = 0; i < data.length; i++) {
                    messageHTMLConstructor(data[i].id, data[i].text, data[i].date);
                    if (i == data.length - 1) {
                        document.getElementById("last_msg_id")["value"] = data[i].id;
                    }
                }
                document.getElementById("id_message_text")["value"] = "";
                $(this).show();
            }
        })
    });

    $("#refreshButton").on("click", function(event) {
        event.preventDefault();
        $.ajax({
            type: "POST",
            url: window.location.pathname,
            data: {
                last_msg_id : document.getElementById("last_msg_id")["value"],
                csrfmiddlewaretoken : document.getElementsByName("csrfmiddlewaretoken")[0]["value"],
            },
            success: function(data) {
                for (i = 0; i < data.length; i++) {
                    messageHTMLConstructor(data[i].id, data[i].text, data[i].date);
                    if (i == data.length - 1) {
                        document.getElementById("last_msg_id")["value"] = data[i].id;
                    }
                }
            }
        })
    });
});