$(document).ready(function () {
    // Обработчик события начала перетаскивания элемента
    $('.task_item').on('dragstart', function (event) {
        // Получаем ID задачи
        var taskId = $(this).data('task-id');
        // Добавляем данные в объект перетаскиваемого элемента
        event.originalEvent.dataTransfer.setData("text/plain", taskId);
    });

    // Обработчик события окончания перетаскивания элемента
    $('.scrum-list').on('drop', function (event) {
        event.preventDefault();
        // Получаем ID задачи из объекта перетаскиваемого элемента
        var taskId = event.originalEvent.dataTransfer.getData("text/plain");
        // Получаем ID статуса колонки, в которую произошло перетаскивание
        var statusId = $(this).closest('.scrum-column').data('status');
        // Отправляем AJAX-запрос на сервер для обновления статуса задачи
        $.ajax({
            type: 'POST',
            url: '/update_task_status/',
            data: {
                'task_id': taskId,
                'status_id': statusId,
                'csrfmiddlewaretoken': '{{ csrf_token }}'
            },
            success: function (data) {
                // Обновляем содержимое страницы после успешного выполнения запроса
                location.reload();
            },
            error: function () {
                alert('Произошла ошибка при обновлении статуса задачи');
            }
        });
    });

    // Обработчик события отмены перетаскивания элемента
    $(document).on('dragover', function (event) {
        event.preventDefault();
    });
});


// ----------------------------------------------------------------------------------------

