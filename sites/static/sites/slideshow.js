let current = 0;
showSlides();

function showSlides() {
    let slides = document.querySelectorAll("#slides > img");
    for(let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    current++;
    if(current > slides.length)
        current = 1;
    slides[current - 1 ].style.display = "block";
    setTimeout(showSlides, 5000);
}