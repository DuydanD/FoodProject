const addIngredientBtn = document.getElementById('addIngredientBtn');
const ingredientPopup = document.getElementById('ingredientPopup');
const closePopupBtn = document.getElementById('closePopupBtn');

addIngredientBtn.addEventListener('click', () => {
    ingredientPopup.style.display = 'block';
 });

closePopupBtn.addEventListener('click', () =>{
    ingredientPopup.style.display = 'none';
});