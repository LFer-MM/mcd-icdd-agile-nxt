function check_connectivity() {
    const cs = document.querySelector(".connection-status");
    fetch("/check_connectivity", {method: "GET"}).then(result => result.json())
    .then(data => {
        cs.textContent=data.connection_status.toString();
        if(data.connection_status===true){
            cs.style.backgroundColor="#20ab2c";
        }
        });
}

function move(direction) {
    fetch("/move", {method: "POST", headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({"direction": direction}, null, 4)})
    then(response => response.text);
}

function scan_color() {
    const scb = document.querySelector(".scanned-color-box");
    fetch("/scan_color", {method: "GET"}).then(result => result.json())
    .then(data => {scb.style.backgroundColor=data.detected_color;});
}

function shoot() {
    fetch("/shoot", {method: "GET"})
    then(response => response.text);
}