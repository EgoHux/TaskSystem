let draggedItem = null;

function handleDragStart(e) {
    draggedItem = e.target;
}

function handleDragOver(e) {
    e.preventDefault();
}

function handleDrop(e) {
    e.preventDefault();
    const dropzone = e.target;
    dropzone.appendChild(draggedItem);

    const taskId = draggedItem.dataset.taskId;
    const newStatus = dropzone.dataset.status;

    // Отправляем AJAX-запрос на сервер, чтобы обновить статус задачи
    $.ajax({
        url: "/update-task-status/",
        type: "POST",
        data: {
            task_id: taskId,
            new_status: newStatus,
        },
        success: function (response) {
            console.log(response);
        },
        error: function (xhr) {
            console.log(xhr.responseText);
        }
    });
}

const taskItems = document.querySelectorAll(".task_item");
taskItems.forEach((item) => {
    item.addEventListener("dragstart", handleDragStart);
});

const dropzones = document.querySelectorAll(".scrum-list");
dropzones.forEach((dropzone) => {
    dropzone.addEventListener("dragover", handleDragOver);
    dropzone.addEventListener("drop", handleDrop);
});