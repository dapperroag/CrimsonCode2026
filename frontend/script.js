let myString = "";

function addSymbol(symbol) {
  myString += symbol;
  document.getElementById("result").innerText = myString;
}

function resetString() {
  myString = "";
  document.getElementById("result").innerText = myString;
}

async function submitString() {
  // Example: send to backend (FastAPI)
  try {
    const response = await fetch("http://127.0.0.1:8000/process_string", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ string: myString }),
    });
    const data = await response.json();
    console.log("Backend response:", data);
  } catch (err) {
    console.error("Error sending to backend:", err);
  }
}