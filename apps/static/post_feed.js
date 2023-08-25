// document.addEventListener('DOMContentLoaded', function () {
//     const openModalButtons = document.querySelectorAll('.open-comment-modal');
//     const commentModals = document.querySelectorAll('.comment-modal');
//     const postDialog = document.getElementById('postDialog'); 

//     openModalButtons.forEach((button, index) => {
//         button.addEventListener('click', () => {
//             commentModals[index].style.display = 'block';
//         });
//     });

//     if (postDialog) {
//         postDialog.style.display = 'block';
//     }

//     postDialog.addEventListener('click', (event) => {
//         if (event.target === postDialog) {
//             postDialog.style.display = 'none';
//         }
//     });

//     commentModals.forEach((modal) => {
//         modal.addEventListener('click', (event) => {
//             if (event.target === modal) {
//                 modal.style.display = 'none';
//             }
//         });
//     });

//     // Additional code for handling posts
//     const postContainer = document.getElementById('postContainer');
//     const openPostDialogButton = document.getElementById('openPostDialog');
//     // const postDialog = document.getElementById('postDialog');

//     if (openPostDialogButton) {
//         openPostDialogButton.addEventListener('click', () => {
//             postDialog.style.display = 'block';
//         });
//     }

   
// });
