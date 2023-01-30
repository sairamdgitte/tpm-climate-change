function showPage(pageName) {
    // Get the container element where you want to display the content
    var container = document.getElementById("content-container");
    // Hide the other container elements
    var containers = document.getElementsByClassName("content-container");
    for (var i = 0; i < containers.length; i++) {
        containers[i].style.display = "none";
    }
    // Set the container to be visible
    document.getElementById(pageName+"-container").style.display = "block";
}
