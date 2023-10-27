// Get all images on the page

const images = document.querySelectorAll('img');

// Create a counter to track the number of images that have loaded

let loadedImages = 0;

// Add a load event listener to each image
images.forEach(image => {
  image.addEventListener('load', () => {
    // Increment the loaded images counter
    loadedImages++;

    // If all images have loaded, hide the loading screen

    
if (loadedImages === images.length) {
      document.getElementById('loading-screen').style.display = 'none';
    }
  });
});