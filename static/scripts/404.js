function dance(){
    const pepe = document.getElementById("pepe");
    pepe.onclick = "";

    const music = new Audio("/static/audio/music.mp3");

    pepe.style.transform = "translate(0%, 75%) scale(3)";

    const link = document.getElementById("link");
    link.style.transition = "1.5s";
    link.style.opacity = "0";
    music.play();
}