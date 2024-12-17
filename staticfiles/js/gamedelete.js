const deleteGameModal = new bootstrap.Modal(document.getElementById("deleteGameModal"));
const deleteGameConfirm = document.getElementById("deleteGameConfirm");
const deleteGameButtons = document.getElementsByClassName("btn-delete-game");


for (let button of deleteGameButtons) {
    button.addEventListener("click", function () {
        const gameSlug = this.getAttribute("data-game-slug");
        deleteGameConfirm.href = `/game/${gameSlug}/delete/`; // Set the correct URL
        deleteGameModal.show();
    });
}


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
}
