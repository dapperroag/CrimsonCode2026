// global variable to store the string
let myString = "";
const colors = ['#4CAF50', '#FF5722', '#2196F3', '#FFC107', '#9C27B0']; 
function cycleColor(btn) {
  // store current color index in a data attribute
  let currentIndex = btn.dataset.colorIndex ? parseInt(btn.dataset.colorIndex) : -1;

  // move to next color
  currentIndex = (currentIndex + 1) % colors.length;

  // apply the new color
  btn.style.backgroundColor = colors[currentIndex];

  // optional: change text color if needed
  btn.style.color = 'white';

  // save the index back to the button
  btn.dataset.colorIndex = currentIndex;
}
// Add a symbol to the string
function addSymbol(symbol) {
  myString += symbol;
  document.getElementById("result").innerText = myString;
}

// Reset the string
function resetString() {
  myString = "";
  document.getElementById("result").innerText = "";
  document.getElementById("backend-result").innerText = "";
}

// Send string to backend and display result
async function submitString() {
  try {
    const response = await fetch("http://127.0.0.1:8000/process_string", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ string: myString })
    })

    // Parse JSON response from backend
    const data = await response.json();

    console.log("Backend response:", data); // for debugging

    // Update HTML with backend result
    document.getElementById("backend-result").innerText = data.result;

  } catch (err) {
    console.error("Error sending to backend:", err);
    document.getElementById("backend-result").innerText = "Error connecting to backend";
  }
}