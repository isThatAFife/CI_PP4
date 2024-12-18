const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");


const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
 * Initializes edit functionality for the provided edit buttons.
 *
 * For each button in the `editButtons` collection:
 * - Retrieves the associated comment's ID upon click.
 * - Fetches the content of the corresponding comment.
 * - Populates the `commentText` input/textarea with the comment's content for editing.
 * - Updates the submit button's text to "Update".
 * - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
 */
// Add event listeners for all edit buttons
for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        e.preventDefault();
        const commentId = e.target.getAttribute("comment_id");
        const commentContent = document.getElementById(`comment${commentId}`).querySelector('div').innerText.trim();
        commentText.value = commentContent;
        const editUrl = e.target.getAttribute("data-edit-url");
        commentForm.setAttribute("action", editUrl);
        submitButton.innerText = "Update";
        commentForm.scrollIntoView({ behavior: "smooth" });
    });
}


/**
 * Initializes deletion functionality for the provided delete buttons.
 *
 * For each button in the `deleteButtons` collection:
 * - Retrieves the associated comment's ID upon click.
 * - Updates the `deleteConfirm` link's href to point to the
 * deletion endpoint for the specific comment.
 * - Displays a confirmation modal (`deleteModal`) to prompt
 * the user for confirmation before deletion.
 */
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("data-comment-id");
        deleteConfirm.setAttribute("data-comment-id", commentId);
        deleteModal.show();
    });
}

deleteConfirm.addEventListener("click", function(e) {
    e.preventDefault();
    const commentId = this.getAttribute("data-comment-id");
    const gameSlug = document.querySelector('.btn-delete[data-comment-id="' + commentId + '"]').getAttribute("data-game-slug");
    const deleteUrl = `/game/${gameSlug}/comment/${commentId}/delete/`;
    
    fetch(deleteUrl, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'X-Requested-With': 'XMLHttpRequest'
        }
    }).then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    }).then(data => {
        if (data.success) {
            location.reload();
        } else {
            alert('Error deleting comment: ' + data.message);
        }
    }).catch(error => {
        console.error('Error:', error);
        alert('An error occurred while deleting the comment');
    });
});




    /**
    * Initializes deletion functionality for the provided delete game buttons.
    * 
    * For each button in the `deleteGameButtons` collection:
    * - Retrieves the associated game's slug upon click.
    * - Updates the `deleteGameConfirm` link's href to point to the 
    * deletion endpoint for the specific game.
    * - Displays a confirmation modal (`deleteGameModal`) to prompt 
    * the user for confirmation before deletion.
    */
    // Event listener for delete confirmation
deleteGameConfirm.addEventListener("click", function (e) {
    e.preventDefault();
    console.log(deleteGameConfirm.href);
    deleteGameConfirm.disabled = true; // Disable button to prevent multiple clicks

    fetch(this.href, {
        method: 'POST',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': getCookie('csrftoken')
        }
    }).then(response => {
        if (!response.ok) {
            return response.text().then(text => { throw new Error(text); });
        }
        return response.json();
    }).then(data => {
        if (data.status === 'success') {
            window.location.href = data.url; // Redirect to game list after deletion
        } else {
            // Handle unexpected status
            alert('Error deleting game: ' + data.message);
        }
    }).catch(error => {
        console.error('There was a problem with your fetch operation:', error);
        alert('An error occurred: ' + error.message); // Provide user feedback
    }).finally(() => {
        deleteGameConfirm.disabled = false; // Re-enable button after processing
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};