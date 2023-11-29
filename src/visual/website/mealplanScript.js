
class Recipe extends HTMLElement {
    constructor(data) {

        super();

        const recipeDetails = {
            name: data['name'],
            nutrition: data['nutrition'],
            ingredients: data['ingredients'],
            instructions: data['instructions']
        };
        
        const wrapper = document.createElement('div');
        wrapper.id = 'recipe-container'

        const detailsList = document.createElement('ul');
        detailsList.id = 'recipe-block'
        detailsList.innerHTML = `
            <li><strong>Name:</strong> ${recipeDetails.name}</li>
            <li><strong>Nutrition:</strong> ${recipeDetails.nutrition}</li>
            <li><strong>Ingredients:</strong> ${recipeDetails.ingredients}</li>
            <li><strong>Instructions:</strong> ${recipeDetails.instructions}</li>
        `;

        wrapper.appendChild(detailsList);

        this.appendChild(wrapper)

    }
}
customElements.define('recipe-element', Recipe);

document.getElementsByClassName("search-mealplan-form")[0]
.addEventListener('submit', function (event) {
    console.log("hello");
    event.preventDefault(); // Prevent the default form submission
    var formData = new FormData(this); // Get form data
    document.getElementsByClassName('result-container')[0].innerHTML = ''

    fetch('http://127.0.0.1:5000/mealplanSearch', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Display the response from Flask server
        for(const recipe in data) {
            const recipeElement = new Recipe(data[recipe])
            document.getElementsByClassName('result-container')[0]
            .appendChild(recipeElement);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

