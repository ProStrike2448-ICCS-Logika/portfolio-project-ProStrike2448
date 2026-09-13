function showMore() {
  let pageCur = Number(document.getElementById("page-cur").value);
  let pageNum = Number(document.getElementById("page-num").value);

  pageCur += 1;
  fetch("?page=" + pageCur, { headers: { "X-Requested-With": "XMLHttpRequest" } })
    .then((response) => {
      console.log(response);
      if (!response.ok) {
        throw new Error("Network response was not ok" + response.statusText);
      }
      return response.text();
    })
    .then((data) => {
      document.getElementsByClassName("article-container")[0].innerHTML += data;
      document.getElementById("page-cur").value = pageCur;
      if (pageCur == pageNum) {
        document.getElementById("show-more").classList.add("disabled");
        document.getElementById("next-page").classList.add("disabled");
      }
      let numPages = document.getElementsByClassName("pagination")[0];
      let i = 0;
      for (let nP of numPages.children) {
        nP.classList.remove("active");
        nP.classList.remove("disabled");

        if (pageCur >= i) {
          nP.classList.add("disabled");
        }
        i++;
      }
    })
    .catch((error) => console.log("Error: ", error));
}
