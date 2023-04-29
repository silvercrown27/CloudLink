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
