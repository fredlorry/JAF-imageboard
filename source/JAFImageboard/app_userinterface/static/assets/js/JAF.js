function messageHTMLConstructor(messageText, messageDate) {
    if (messageDate == undefined) {
        messageDate = Date();
    };
    document.getElementById("Message list").innerHTML += 
        '<hr> \
            <span class="label label-default"> \
                <h4> \
                    <small>'
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
                messageHTMLConstructor(data.messageText, data.messageDate);
                document.getElementById("id_message_text")["value"] = "";
                $(this).show();
            }
        })
    });
});