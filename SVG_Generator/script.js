document.addEventListener("DOMContentLoaded", function () {
    const kWidthInput = document.getElementById("k-width-input");
    const kDepthSelect = document.getElementById("k-depth-select");
    const lSideSelect = document.getElementById("l-side-select");
    const rSideSelect = document.getElementById("r-side-select");
    const facadeSelect = document.getElementById("facade-select");
    const openDegreeSelect = document.getElementById("open-degree-select");
    const svgContainer = document.getElementById("svg-container");

    function updateSVGGraphics() {
        const kWidth = parseInt(kWidthInput.value);
        const kDepth = parseInt(kDepthSelect.value);
        const lSideThickness = parseInt(lSideSelect.value);
        const rSideThickness = parseInt(rSideSelect.value);
        const facadeThickness = parseInt(facadeSelect.value);
        const openDegree = parseInt(openDegreeSelect.value);

        const svgCode = generateSVGCode(
            kWidth,
            kDepth,
            lSideThickness,
            rSideThickness,
            facadeThickness,
            openDegree
        );

        svgContainer.innerHTML = svgCode;
    }

    kWidthInput.addEventListener("input", updateSVGGraphics);
    kDepthSelect.addEventListener("input", updateSVGGraphics);
    lSideSelect.addEventListener("change", updateSVGGraphics);
    rSideSelect.addEventListener("change", updateSVGGraphics);
    facadeSelect.addEventListener("change", updateSVGGraphics);
    openDegreeSelect.addEventListener("change", updateSVGGraphics);

    // Initial SVG graphics generation
    updateSVGGraphics();
});

function generateSVGCode(kWidth, kDepth, lSideThickness, rSideThickness, facadeThickness, openDegree) {
    const bt_offset = 15;
    const bt_thickness = 4;
    const inner_safe_dist = 70;
    const offsets = [0, bt_offset, bt_thickness, inner_safe_dist];
    const sum_offsets = offsets.reduce((a, b) => a + b, 0)

    const start_point = (x, y) => [50 + x, 50 + y];

    const katet = () => {
        const inner_width = width_validation() - lSideThickness - rSideThickness;
        return Math.tan((openDegree * Math.PI) / 180) * inner_width;
    };

    function max_width() {
        let inner_depth = depth_validation() - sum_offsets;
        return (inner_depth / Math.tan(openDegree * (Math.PI / 180))) + lSideThickness + rSideThickness;
    }

    function width_validation() {
        return (kWidth > max_width()) ? max_width() : Math.max(kWidth, 150);
    }

    function depth_validation() {
        return Math.max(kDepth, 150);
    }

    function r_side_validation() {
        let depth = depth_validation() - katet();
        return (depth - sum_offsets <= 0) ? sum_offsets : depth;
    }

    function roundUp(num, precision) {
        precision = Math.pow(10, precision)
        return Math.ceil(num * precision) / precision
    }

    const facadeWidth = () => {
        const inner_width = width_validation() - 2 - rSideThickness;
        return inner_width / Math.cos((openDegree * Math.PI) / 180);
    };

    const offsets_addition = []
    let startY = 0;
    for (const y of offsets) { startY += y; offsets_addition.push(startY) }

    return `<svg xmlns="http://www.w3.org/2000/svg" width="600" height="1000">
          <rect x="${start_point(0, 0)[0]}" y="${start_point(0, 0)[1]}" width="${lSideThickness}" height="${depth_validation()}" id="leftSide" style="fill:blue;fill-opacity:0.1;stroke:black;stroke-width:1;stroke-dasharray:5,5;opacity:1" />
          <rect x="${start_point(width_validation() - rSideThickness, 0)[0]}" y="${start_point(width_validation() - rSideThickness, 0)[1]}" width="${rSideThickness}" height="${r_side_validation()}" id="rightSide" style="fill:blue;fill-opacity:0.1;stroke:black;stroke-width:1;stroke-dasharray:5,5;opacity:1" />
          <line x1="${start_point(lSideThickness, 0)[0]}" y1="${start_point(0, depth_validation())[1]}" x2="${start_point(width_validation() - rSideThickness, 0)[0]}" y2="${start_point(0, r_side_validation())[1]}" style="stroke:black;stroke-width:1;stroke-dasharray:5,5" />
          <rect x="${start_point(width_validation() - rSideThickness, 0)[0]}" y="${start_point(0, r_side_validation())[1]}" width="${facadeThickness}" height="${facadeWidth()}" transform="rotate(${90 - openDegree}, ${start_point(width_validation() - rSideThickness, 0)[0]}, ${start_point(0, r_side_validation())[1]})" id="facade" style="fill:red;fill-opacity:0.1;stroke:black;stroke-width:1;stroke-dasharray:5,5;opacity:1" />
          ${offsets_addition
            .map(
                (offset) =>
                    `<line x1="${start_point(lSideThickness, offset)[0]}" y1="${start_point(lSideThickness, offset)[1]}" x2="${start_point(width_validation() - rSideThickness, offset)[0]}" y2="${start_point(width_validation() - rSideThickness, offset)[1]}" style="stroke:black;stroke-width:1;stroke-dasharray:5,5" />`
            )
            .join("\n")
        }
          <text x="${start_point(width_validation() / 2, -5)[0]}" y="${start_point(width_validation() / 2, -5)[1]}" text-anchor="middle">${roundUp(width_validation(), 0)} (max.${roundUp(max_width(), 0)})</text>
          <text x="${start_point(-5, depth_validation() / 2)[0]}" y="${start_point(-5, depth_validation() / 2)[1]}" text-anchor="end">${roundUp(depth_validation(), 0)}</text>
          <text x="${start_point(width_validation() + 5, r_side_validation() / 2 + 5)[0]}, " y="${start_point(width_validation() + 5, r_side_validation() / 2 + 5)[1]}" text-anchor="start">${roundUp(r_side_validation(), 0)}</text>
          <text x="${start_point(width_validation() - rSideThickness - 40, r_side_validation() - 5)[0]}" y="${start_point(width_validation() - rSideThickness - 40, r_side_validation() - 5)[1]}">${openDegree}°</text>
          <text x="${start_point(width_validation() / 2, 0)[0]}" y="${start_point(0, (depth_validation() - r_side_validation()) / 2 + r_side_validation())[1] - 5}" text-anchor="middle" transform="rotate(${-openDegree}, ${start_point(width_validation() / 2, 0)[0]}, ${start_point(0, (depth_validation() - r_side_validation()) / 2 + r_side_validation())[1] - 5}) ">${roundUp(facadeWidth(), 0)}</text>
          </svg > `;
}
//

