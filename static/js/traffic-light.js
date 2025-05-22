document.getElementById('stopButton').onclick = () => updateLight('stop');
document.getElementById('slowButton').onclick = () => updateLight('slow');
document.getElementById('goButton').onclick = () => updateLight('go');

function illuminateRed() {
    clearLights();
    document.getElementById('stopLight').style.backgroundColor = "red";
    updateLight("stop");
}

function illuminateYellow() {
    clearLights();
    document.getElementById('slowLight').style.backgroundColor = "yellow";
    updateLight("slow");
}

function illuminateGreen() {
    clearLights();
    document.getElementById('goLight').style.backgroundColor = "green";
    updateLight("go");
}

function clearLights() {
    document.getElementById('stopLight').style.backgroundColor = "black";
    document.getElementById('slowLight').style.backgroundColor = "black";
    document.getElementById('goLight').style.backgroundColor = "black";
}

function updateLight(color) {
    // Illuminate logic
    clearLights();
    const colorMap = {
        stop: 'red',
        slow: 'yellow',
        go: 'green'
    };
    document.getElementById(`${color}Light`).style.backgroundColor = colorMap[color];

    // Notify backend to update count
    fetch('/update-light', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ color: color })
    })
    .then(response => response.json())
    .then(data => {
        // Update counts on screen
        document.getElementById('stopCount').textContent = data.stop;
        document.getElementById('slowCount').textContent = data.slow;
        document.getElementById('goCount').textContent = data.go;
    });
}
