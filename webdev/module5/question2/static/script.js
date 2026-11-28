  
  
  
  document.getElementById("form1").addEventListener("submit", async (e) => {
      e.preventDefault();   // stop the browser from leaving the page

      const query = document.getElementById("query").value.trim();
      if (!query) 
        return;

      const res = await fetch("https://api.tvmaze.com/search/shows?q=" + query);
      const data = await res.json();

      //keeping only exact matches 
      const exact = data.filter(item => item.show.name.toLowerCase() === query.toLowerCase());

    // nothing matched exactly
      if (exact.length === 0) {
      const msg = `No exact match found for "${query}"`;
      console.log(msg);
      document.getElementById("results").textContent = msg;
      return;
  
    }

      let text = "";
      let html="";
      data.forEach(item => {
        const s = item.show;
        text += `Name: ${s.name} Premiered: ${s.premiered}Genres: ${s.genres.join(", ")}\nRating: ${s.rating.average}\nStatus: ${s.status}\n\n`;
        html+=`
              <p>
                <b> Name: </b> ${s.name}<br>
                <b> Premiered: </b> ${s.premiered}<br>
                <b> Genres: </b> ${s.genres.join(", ")}<br>
                <b> Rating: </b> ${s.rating.average}<br>
                <b> Status: </b> ${s.status}
              </p>
              `
      });

      console.log(text);
      document.getElementById("results").innerHTML = html;
  });
