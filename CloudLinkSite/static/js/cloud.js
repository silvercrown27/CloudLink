function validatePage1() {
    // Validation logic for page 1
    return true; // Return true if validation is successful, false otherwise
}

function validatePage2() {
    // Validation logic for page 2
    return true; // Return true if validation is successful, false otherwise
}

function validatePage3() {
    // Validation logic for page 3
    return true; // Return true if validation is successful, false otherwise
}

function validatePage4() {
    // Validation logic for page 4
    return true; // Return true if validation is successful, false otherwise
}

function submitForm() {
    // Final form submission logic
    alert("Form submitted successfully!");
}

function nextPage(currentPage) {
    let nextTab = currentPage + 1;
    let currentTab = document.getElementById("selection_tab" + currentPage);
    let nextTabContent = document.getElementById("selection_tab" + nextTab);

    if (currentPage < 4 && validatePage(currentPage)) {
        currentTab.classList.remove("active");
        nextTabContent.style.display = "block";
        document.getElementById("selection_tab" + nextTab).classList.add("active");
        document.getElementById("selection_tab" + currentPage).style.display = "none";
    }
}

function previousPage(currentPage) {
    let prevTab = currentPage - 1;
    let currentTab = document.getElementById("selection_tab" + currentPage);
    let prevTabContent = document.getElementById("selection_tab" + prevTab);

    if (currentPage > 1 && validatePage(currentPage - 1)) {
        currentTab.classList.remove("active");
        prevTabContent.style.display = "block";
        document.getElementById("selection_tab" + prevTab).classList.add("active");
        document.getElementById("selection_tab" + currentPage).style.display = "none";
    }
}

function validatePage(currentPage) {
    switch (currentPage) {
        case 1:
            return validatePage1();
        case 2:
            return validatePage2();
        case 3:
            return validatePage3();
        case 4:
            return validatePage4();
        default:
            return true;
    }
}

function checkPassword() {
  var password = document.getElementById("password");
  var confirm_password = document.getElementById("confirm_password");
  var password_warning = document.getElementById("password_warning");

  if (password.value != confirm_password.value) {
    password_warning.style.display = "inline";
  } else {
    password_warning.style.display = "none";
  }
}

// Function to check if an element is in the viewport
function isElementInViewport(el) {
    var rect = el.getBoundingClientRect();
    return (
      rect.top >= 0 &&
      rect.left >= 0 &&
      rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
      rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

// Function to load more items when user scrolls
function lazyLoad() {
    var mediaItems = document.getElementsByClassName("media-item");

    for (var i = 0; i < mediaItems.length; i++) {
      if (isElementInViewport(mediaItems[i])) {
        mediaItems[i].classList.add("loaded");
      }
    }
}

// Attach lazyLoad function to scroll event
window.addEventListener("scroll", lazyLoad);

// Load initial items
lazyLoad();