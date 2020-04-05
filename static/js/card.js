function toggle(elem) {
    elem.classList.toggle("selected");
}

function goToLeaderboard() {
    hostAddress= top.location.host.toString();
    url = "http://" + hostAddress + "/leaderboard";
    window.location.href = url;
}