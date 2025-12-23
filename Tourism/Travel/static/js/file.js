function sendMessage() {
    const msg = document.getElementById("userMessage").value;
    document.getElementById("chatbox").innerHTML += "<p>You: " + msg + "</p>";
    // Simulated reply
    document.getElementById("chatbox").innerHTML += "<p>Bot: This is a demo response.</p>";
}
