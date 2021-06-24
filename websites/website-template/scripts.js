var menuState = "off"

function changeMenu(x) {
    x.classList.toggle("change");
}

function changeActive(x) {
    x.classList.toggle("active")
}

// menu panel
function showPanel(x) {
    var panel = x.firstElementChild;
    if (panel.style.display === "block") {
        panel.style.display = "none";
    } else {
        panel.style.display = "block";
    }
}

// open tab
function openTab(x, tabName) {
    // Declare all variables
    var i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(tabName).style.display = "block";
    x.classList.toggle("active");
}

function openMenu(x, tabName) {
    if (menuState === "off") {
        openTab(x, tabName);
        menuState = "on";
    } else {
        closeTab();
        menuState = "off";
        x.classList.toggle("active");
    }
}