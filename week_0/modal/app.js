const startAddBtn = document.querySelector("header button");
const cancelAddBtn = document.querySelector(".btn--passive");
const addBtn = document.querySelector(".btn--success");
const cancelRemoveBtn = document.querySelector("#delete-modal .btn--passive");

const addModal = document.getElementById("add-modal");
const backDrop = document.getElementById("backdrop");
const removeModal = document.getElementById("delete-modal");

const inputs = document.querySelectorAll("input");
const movieListUI = document.getElementById("movie-list");

const movies = [];

const openModalHandler = (modal) => {
  modal.classList.add("visible");
  backDrop.classList.add("visible");
};

const closeModalHandler = (modal) => {
  modal.classList.remove("visible");
  backDrop.classList.remove("visible");
  cleanUpUI();
};

const addNewMovie = () => {
  const newMovie = {
    id: Math.random().toString(),
    title: inputs[0].value,
    image: inputs[1].value,
    rating: inputs[2].value,
  };

  movies.push(newMovie);
  return newMovie;
};

const cleanUpUI = () => {
  inputs.forEach((inp) => {
    inp.value = "";
  });
};

const addMovieToUI = (movie) => {
  const { id, title, image, rating } = movie;
  const newMovieElement = document.createElement("li");
  newMovieElement.className = "movie-element";
  newMovieElement.id = id;
  newMovieElement.insertAdjacentHTML(
    "afterbegin",
    `
    <div class="movie-element__image">
      <img src="${image}" alt="${title}">
    </div>
    <div class="movie-element__info">
      <h2>${title}</h2>
      <p>${rating}/5 stars</p>
    </div>
   
    <button class="btn" id="${id}">Remove</button>
    `
  );
  movieListUI.append(newMovieElement);

  const deleteButton = document.getElementById(`${id}`);
  deleteButton.addEventListener("click", deleteMovie.bind(null, id));
};

function deleteMovie(movieId) {
  openModalHandler(removeModal);

// Workaround to remove all the event listeners previously attached to this button
// (each movie attaches an event listener on a single btn)
  let removeBtn = document.querySelector(".btn--danger");
  removeBtn.replaceWith(removeBtn.cloneNode(true));
  removeBtn = document.querySelector(".btn--danger");

  removeBtn.addEventListener("click", () => {
    deleteMovieHandler(movieId);
  });
}

function deleteMovieHandler(movieId) {
  const movieToDeleteIdx = movies.findIndex((movie) => movie.id === movieId);
  movies.splice(movieToDeleteIdx, 1);
  removeMovieFromUI(movieId);
}

function removeMovieFromUI(movieId) {
  const movieToRemove = document.getElementById(movieId);
  movieToRemove.remove();
  console.log(movieToRemove, movies);
  closeModalHandler(removeModal);
}

// Event Listeners
startAddBtn.addEventListener("click", (e) => {
  openModalHandler(addModal);
});

cancelAddBtn.addEventListener("click", (e) => {
  closeModalHandler(addModal);
});

backDrop.addEventListener("click", (e) => {
  closeModalHandler(addModal);
  closeModalHandler(removeModal);
});

addBtn.addEventListener("click", (e) => {
  const movie = addNewMovie();
  closeModalHandler(addModal);
  cleanUpUI();
  addMovieToUI(movie);
});

cancelRemoveBtn.addEventListener("click", (e) => {
  closeModalHandler(removeModal);
});
