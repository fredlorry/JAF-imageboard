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
function submitFakeMessage() {
    var form = document.getElementById("newMessageForm");
    messageHTMLConstructor(form.elements[1].value);
    form.elements[1].value = "";
}