function get_data() {
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:3000/get_data",  
        success: function(response) {
            $('#messages').empty();

            let i = 0
            while (i < response.length){
                $('#messages').append('<p><strong>' + response[i][0] + ':</strong> ' + response[i][1] + '</p>');

                i++;
            }
        },
        error: function(xhr, status, error) {
            console.log("Сталася помилка: " + error);
        }
    });
}

function massege() {
    var user = $('#name').text();
    var message = $('#messageInput').val();

    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:3000/masg",
        data: {
            user: user,
            masg: message
        },
        success: function(response) {
            $('#messageInput').val('');
        },
        error: function(xhr, status, error) {
            console.log("Сталася помилка: " + error);
        }
    });
}