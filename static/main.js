function get_data() {
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:3000/get_data",  
        success: function(response) {
            $('#textw').empty();

            let i = 0
            while (i < response.length){
                if (i + 1 === response.length) {
                    $('#textw').append('<p><strong>' + response[i][0] + ':</strong> ' + response[i][1] + '</p>');
                } else {
                    $('#textw').append('<p><strong>' + response[i][0] + ':</strong> ' + response[i][1] + '</p><br>');
                }
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
            get_data()
        },
        error: function(xhr, status, error) {
            console.log("Сталася помилка: " + error);
        }
    });
}