// Function to update the graphics based on the selected values
function updateGraphics() {
    // Get the selected values from the controls
    var kWidth = document.getElementById("k-width").value;
    var kDepth = document.getElementById("k-depth").value;
    var lSideThickness = document.getElementById("l-side-thickness").value;
    var rSideThickness = document.getElementById("r-side-thickness").value;
    var openDegree = document.getElementById("open-degree").value;

    // Make an AJAX request to the Python server to generate the graphics
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/generate_graphics", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            // On successful response, update the SVG graphics
            var svgData = xhr.responseText;
            document.getElementById("vector-graphics").innerHTML = svgData;
        }
    };
    xhr.send(JSON.stringify({
        kWidth: kWidth,
        kDepth: kDepth,
        lSideThickness: lSideThickness,
        rSideThickness: rSideThickness,
        openDegree: openDegree
    }));
}

// Attach event listeners to the controls
document.getElementById("k-width").addEventListener("input", updateGraphics);
document.getElementById("k-depth").addEventListener("change", updateGraphics);
document.getElementById("l-side-thickness").addEventListener("change", updateGraphics);
document.getElementById("r-side-thickness").addEventListener("change", updateGraphics);
document.getElementById("open-degree").addEventListener("change", updateGraphics);

// Initial update of the graphics
updateGraphics();
