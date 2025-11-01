async function analyze() {
  const text = document.getElementById("review").value;
  if (!text.trim()) {
    document.getElementById("result").innerText = "Please enter text!";
    return;
  }
  const response = await fetch("/api/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text }),
  });
  const data = await response.json();
  if (data.error) {
    document.getElementById("result").innerText = data.error;
  } else {
    document.getElementById("result").innerText = `Sentiment: ${data.label} (${(data.score * 100).toFixed(1)}%)`;
  }
}
