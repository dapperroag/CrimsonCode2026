// global variable to store the string
let myString = "";

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
    });

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