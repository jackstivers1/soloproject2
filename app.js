const API = "http://localhost/api";
let books = [];
let page = 1;
const perPage = 5;

function loadBooks() {
  fetch(`${API}/get_books.php`)
    .then(r => r.json())
    .then(data => {
      books = data;
      render();
    });
}

function render() {
  renderList();
  renderPagination();
  renderStats();
}

function renderList() {
  const list = document.getElementById("list");
  list.innerHTML = "";

  const start = (page - 1) * perPage;
  const slice = books.slice(start, start + perPage);

  slice.forEach(b => {
    const li = document.createElement("li");
    li.textContent = `${b.name} (${b.date}) - ${b.author}`;
    list.appendChild(li);
  });
}

function renderPagination() {
  const p = document.getElementById("pagination");
  p.innerHTML = "";

  const pages = Math.ceil(books.length / perPage);
  for (let i = 1; i <= pages; i++) {
    const btn = document.createElement("button");
    btn.textContent = i;
    btn.onclick = () => { page = i; renderList(); };
    p.appendChild(btn);
  }
}

function renderStats() {
  const stats = {};
  books.forEach(b => stats[b.genre] = (stats[b.genre] || 0) + 1);

  document.getElementById("stats").innerHTML =
    Object.entries(stats)
      .map(([g, c]) => `${g}: ${c}`)
      .join("<br>");
}

document.getElementById("bookForm").onsubmit = e => {
  e.preventDefault();

  const book = {
    name: name.value,
    author: author.value,
    genre: genre.value,
    date: date.value
  };

  fetch(`${API}/add_book.php`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(book)
  }).then(loadBooks);

  e.target.reset();
};

loadBooks();
