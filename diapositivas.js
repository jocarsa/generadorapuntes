// Variables
const scrollDuration = 800; // Duration of smooth scrolling animation in milliseconds
const scrollOffset = 0; // Offset for scrolling position

let scrollElements = document.querySelectorAll('.diapositiva'); // Replace '.your-selector' with your desired selector

let currentIndex = 0;
let isScrolling = false;

// Function to smoothly scroll to the specified element
function scrollToElement(element) {
  isScrolling = true;

  const elementPosition = element.offsetTop - scrollOffset;
  const startPosition = window.pageYOffset;
  const distance = elementPosition - startPosition;
  const startTime = performance.now();

  function scrollStep(timestamp) {
    const currentTime = timestamp - startTime;
    const scrollProgress = Math.min(currentTime / scrollDuration, 1);
    const ease = easeInOutQuad(scrollProgress);
    window.scrollTo(0, startPosition + distance * ease);

    if (currentTime < scrollDuration) {
      window.requestAnimationFrame(scrollStep);
    } else {
      isScrolling = false;
    }
  }

  window.requestAnimationFrame(scrollStep);
}

// Function to handle mouse click events
function handleClick(event) {
  event.preventDefault(); // Prevent default right-click context menu

  if (isScrolling) {
    return;
  }

  if (event.button === 0) {
    // Left click - Go back one element
    if (currentIndex > 0) {
      currentIndex--;
      scrollToElement(scrollElements[currentIndex]);
    }
  } else if (event.button === 2) {
    // Right click - Go forward one element
    if (currentIndex < scrollElements.length - 1) {
      currentIndex++;
      scrollToElement(scrollElements[currentIndex]);
    }
  }
}

// Attach event listener to the document for mouse click events
document.addEventListener('mousedown', handleClick);

// Easing function
function easeInOutQuad(t) {
  return t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t;
}

// Function to handle right mouse button click and prevent context menu
function handleContextMenu(event) {
  event.preventDefault(); // Prevent default context menu
}

// Attach event listener to the document for contextmenu event
document.addEventListener('contextmenu', handleContextMenu);