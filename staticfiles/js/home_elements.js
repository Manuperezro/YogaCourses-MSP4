  // Carousel following the youtube tutorial Users Stories Jasvascrpt carousel By Codelab

function modulo(number, mod) {
  let result = number % mod;
  if (result < 0) {
    result += mod;
  }
  return result;
}

function setUpCarousel(carousel) {
  function handleNext() {
    currentSlide = modulo(currentSlide + 1, numSlides);
    changeSlide(currentSlide);
  }

  function handlePrevious() {
    currentSlide = modulo(currentSlide - 1, numSlides);
    changeSlide(currentSlide);
  }

  function changeSlide(slideNumber) {
    carousel.style.setProperty('--current-slide', slideNumber);
  }

  // get elements
  const buttonPrevious = carousel.querySelector('[data-carousel-button-previous]');
  const buttonNext = carousel.querySelector('[data-carousel-button-next]');
  const slidesContainer = carousel.querySelector('[data-carousel-slides-container]');

  // carousel state we need to remember
  let currentSlide = 0;
  const numSlides = slidesContainer.children.length;

  // set up events
  buttonPrevious.addEventListener('click', handlePrevious);
  buttonNext.addEventListener('click', handleNext);
}

const carousels = document.querySelectorAll('[data-carousel]');
carousels.forEach(setUpCarousel);


// effects 

$(document).hover(function(){
    $(".overlay-story").hover(function(){
      $(this).css("background-color", "#d39e00");
      }, function(){
      $(this).css("background-color", "aliceblue");
    });
  });

// Modal Footer

$(document).ready(function(){
	$('#joinmodal').click(function(){
		$('#joinmodal').modal('show')
	});
});
