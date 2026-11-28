const form = document.getElementById("search-form");
const results = document.getElementById("results");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const query = document.getElementById("query").value.trim();
  if (!query) return;

  const res = await fetch(
    "https://api.tvmaze.com/search/shows?q=" + encodeURIComponent(query),
  );
  const data = await res.json();

  // clear the old results
  results.innerHTML = "";

  if (data.length === 0) {
    results.textContent = `No series found for "${query}"`;
    return;
  }

  data.forEach((tvShow) => {
    const show = tvShow.show;

    const article = document.createElement("article");

    // name in <h2>
    const h2 = document.createElement("h2");
    h2.textContent = show.name;

    // url in <a target="_blank">
    const a = document.createElement("a");
    a.href = show.url;
    a.target = "_blank";
    a.textContent = "Show details";

    // medium image (optional chaining: some shows have no image)
    const img = document.createElement("img");
    img.src = show.image?.medium ?? "";
    img.alt = show.name;

    // summary in <div> (the summary already contains <p>)
    const div = document.createElement("div");
    div.innerHTML = show.summary ?? "No summary available.";

    article.append(h2, a, img, div);
    results.appendChild(article);
  });
});
