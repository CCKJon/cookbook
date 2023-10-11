List of ideas to add to the project:

- Ability to add photos, choose the "primary" photo which is the recipe display picture.
- unit of measurement conversion button
- serving size data
- nutritional facts
- ~~how long it takes to cook~~

Things to work on:

- work on implementing cards - https://flowbite-svelte.com/docs/components/card#mainContent
- ~~add recipe list that gets all recipes in database~~
- ~~Create buttons to remove steps or make it so that if an ingredient or step is empty, remove it/disregard it~~
- add modal for submitted recipe to state that a recipe was successfully added
- ~~fuse search to search for recipes~~
- Create a sort function for recipe type (dessert, entree, appetizer, etc.)
- ~~Create login authentication so that only when logged in can a person update or delete a recipe.~~
- Create a "favorites" list for logged in people - favorites page should have prompt to login if not already logged in.
- create functionality so that you can only favorite a recipe if you're logged in.
- logged in users should only be able to see recipes that they've favorited
- ~~login user page that displays a list of submitted recipes by user, allowing only the author to update or delete recipes submitted by said author~~
- ~~by default, if there is no one logged in, then the UID used for the recipe creation is by default my own~~
- Be able to view other peoples' profiles, their submitted recipes, maybe their favorites? Be able to set profiles to private - to note, this would require a new page that shows a list of users and a search function to find them
- Need to do styling for private dashboard, update recipe, favorites page.
- ~~create a reviews/comments posted for a recipe, allow comment sorting based off recency, stars, dates, etc.~~
- create a sorting function for comments
- to create a favorites list, a button to add a recipe to a favorites list needs to be created.
- ask chatgpt how to hide the scrollbar

Possible features to add:

- private messaging - nah
- ratings on recipes
- user menu drop down - https://flowbite-svelte.com/docs/components/navbar

FIXING NEEDED:

- DELETE recipe function in private dashboard executes the function before clicking on the "Are you sure?" button
- currently when searching, the results of the search only take you to the recipe if you click on the recipe name, shoud be updated to be able to click the whole box

REVIEWS

- reviews should appear on the recipe page itself along with a rating
- reviews authored by a user should show up in their private dashboard

- [x] AI recipe generator
- [ ] Work on integrating the AI recipe to the cookbook app