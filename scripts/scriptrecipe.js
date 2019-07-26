console.log("It works!");

function onsubmitClick(i) {
  console.log("it hit");
  var title = document.getElementById("card-title" + i).textContent;
  var content = document.getElementById("card-text" + i).textContent;
  var ingredients = document.getElementById("hidden" + i).textContent;
  var image = document.getElementById("hiddenImage" + i).textContent;

  var url ="/choosenrecipe?title=" + title + "&content=" + content + "&ingredients=" + ingredients +"&image=" + image;
  window.location.href = url;

}

function init() {
}

$(document).ready(init);
