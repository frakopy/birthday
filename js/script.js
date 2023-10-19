const videoContainer = document.getElementById("videoCont");
const finalVideo = document.getElementById("finalVideo");
const p = document.getElementsByTagName("p")[0];
const BoxVideo = document.getElementById("boxVideo");
let backgroundMusic = document.getElementById("mananitas");

videoContainer.addEventListener("click", (e) => {

    setTimeout(() => {
        videoContainer.classList.add("enlarged");
        setTimeout(() => {
            BoxVideo.classList.add("hide");
            finalVideo.classList.remove("hide");
            finalVideo.classList.add("fade-in-element");
            videoContainer.classList.remove("enlarged");
            finalVideo.play();
        }, 2000);
    }, 7500);

    // hide text below box video
    p.classList.add("hide");

    // Play video (box effect)
    BoxVideo.play();

    // Play the background music
    backgroundMusic.play();
    // Set the volume of the background music
    backgroundMusic.volume = 0.1;
});
