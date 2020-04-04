function goToCard() {
    hostAddress= top.location.host.toString();
    name = document.getElementById("username").value;
    url = "http://" + hostAddress + "/" + name;
    window.location.href = url;
}
