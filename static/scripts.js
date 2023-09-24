document.addEventListener('DOMContentLoaded', function () {
    const openModalButtons = document.querySelectorAll('.open-comment-modal');
    const commentModals = document.querySelectorAll('.comment-modal');
    const postDialog = document.getElementById('postDialog');
    const postContainer = document.getElementById('postContainer');
    const openPostDialogButton = document.getElementById('openPostDialog');

    openModalButtons.forEach((button, index) => {
        button.addEventListener('click', () => {
            commentModals[index].style.display = 'block';
        });
    });

    if (openPostDialogButton) {
        openPostDialogButton.addEventListener('click', () => {
            postDialog.style.display = 'block';
        });
    }

    if (postDialog) {
        postDialog.addEventListener('click', (event) => {
            if (event.target === postDialog) {
                postDialog.style.display = 'none';
            }
        });
    }

    commentModals.forEach((modal) => {
        modal.addEventListener('click', (event) => {
            if (event.target === modal) {
                modal.style.display = 'none';
            }
        });
    });


});
