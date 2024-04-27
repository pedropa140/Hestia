document.addEventListener('DOMContentLoaded', function () {
  var frame3 = document.querySelector('.frame-3');
  var frame6 = document.querySelector('.frame-6');
  var frame7 = document.querySelector('.frame-7');

  // Add click event listener for frame-3
  frame3.addEventListener('click', function () {
    // Navigate to the next page when frame-3 is clicked
    window.location.href = '/';
  });

  // Add click event listener for frame-6
  frame6.addEventListener('click', function () {
    // Navigate to the next page when frame-6 is clicked
    window.location.href = 'about';
  });

  frame7.addEventListener('click', function () {
    // Navigate to the next page when frame-7 is clicked
    window.location.href = 'help';
  });
});