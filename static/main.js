$(document).ready(function() {
    $('#getDataBtn').click(function() {
        $.ajax({
            type: "POST",
            url: "/get_data",  // Маршрут на Flask
            success: function(response) {
                // Очистимо вміст блоку перед показом нових повідомлень
                $('#messages').empty();
                
                // Відображаємо отримані повідомлення
                $.each(response, function(user, message) {
                    $('#messages').append('<p><strong>' + user + ':</strong> ' + message + '</p>');
                });
            },
            error: function(xhr, status, error) {
                console.log("Сталася помилка: " + error);
            }
        });
    });
});