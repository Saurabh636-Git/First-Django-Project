console.log('Hello')

function see_charts() {
    var x = document.getElementById("reveal");
    if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
  }

  const bill = 259

  const tip = (50<bill<300) ? `0.15 * ${bill}` : `0.20 * ${bill}` 