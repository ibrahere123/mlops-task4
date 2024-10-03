async function fetchMessages() {
    const response = await fetch('http://localhost:5000/messages'); // Keep this as localhost
    const data = await response.json();
    const contentDiv = document.getElementById('content');
    contentDiv.innerHTML = data.map(msg => `<p><strong>${msg.name}</strong> (${msg.email}): ${msg.message}</p>`).join('');
}

async function addMessage() {
    const nameInput = document.getElementById('nameInput');
    const emailInput = document.getElementById('emailInput');
    const messageInput = document.getElementById('messageInput');

    const name = nameInput.value;
    const email = emailInput.value;
    const message = messageInput.value;

    if (!name || !email || !message) return;

    await fetch('http://localhost:5000/messages', { // Keep this as localhost
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, email, message }),
    });

    nameInput.value = '';
    emailInput.value = '';
    messageInput.value = '';
    fetchMessages();
}

fetchMessages();
