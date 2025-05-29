const addIngredientBtn = document.getElementById('addIngredientBtn');
const ingredientPopup = document.getElementById('ingredientPopup');
const closePopupBtn = document.getElementById('closePopupBtn');
const deletedSelectedBtn = document.getElementById('deleteSelectedBtn')
const deleteIngredient = document.querySelectorAll('input[name="delete_ingredient"]')

addIngredientBtn.addEventListener('click', () => {
    ingredientPopup.style.display = 'block';
 });

closePopupBtn.addEventListener('click', () =>{
    ingredientPopup.style.display = 'none';
});


function toggleDeleteButtonState() {
    let checked = false;

    for (const checkbox of deleteIngredient) {
        if (checkbox.checked) {
            checked = true;
            break;
        }
    }
    if (checked) {
        deletedSelectedBtn.style.display = 'inline-block';
    } else {
        deletedSelectedBtn.style.display = 'none';
    }
}

deleteIngredient.forEach(checkbox => {
    checkbox.addEventListener('change', toggleDeleteButtonState);
})

toggleDeleteButtonState();