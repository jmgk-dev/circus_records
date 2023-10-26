/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function dropDown() {
    document.getElementById("colour_burger_menu").classList.toggle("show");
    document.getElementById("burger_logo").classList.toggle("show");
    document.getElementById("sticky_bg").classList.toggle("hide_bg");
    document.body.classList.toggle("hideoverflow");

    const hideableDivs = document.getElementsByClassName("tohide");
    // Loop through the collection and toggle the visibility of each div
    for (let i = 0; i < hideableDivs.length; i++) {
      if (hideableDivs[i].style.display === "block" || hideableDivs[i].style.display === "") {
        hideableDivs[i].style.display = "none"; // hide the div
      } else {
        hideableDivs[i].style.display = "block"; // show the div
      }
    }
    

  };
  
function menuAni(x) {
    x.classList.toggle("change");
}


