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

var storageChart = new Chart(document.getElementById('storage-chart'), {
    type: 'doughnut',
    data: {
    labels: ['Used', 'Free'],
    datasets: [{
      data: [60, 40],
      backgroundColor: ['#007bff', '#e2e3e5'],
      borderWidth: 0
    }]
    },
    options: {
    maintainAspectRatio: false,
    cutoutPercentage: 80,
    legend: {
      display: false
    }
    }
    });

// Media Chart
var mediaChart = new Chart(document.getElementById('media-chart'), {
    type: 'line',
    data: {
    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
    datasets: [{
      data: [20, 50, 80, 60, 70, 90, 100],
      label: 'Files',
      borderColor: '#007bff',
      fill: false
    }]
    },
    options: {
    maintainAspectRatio: false,
    legend: {
      display: false
    },
    scales: {
      xAxes: [{
        gridLines: {
          display: false
        }
      }],
      yAxes: [{
        gridLines: {
          display: false
        }
      }]
    }
    }
    });