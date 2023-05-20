from math import tan, radians
import svgwrite


k_width = 220
k_depth = (290, 340)
l_side_thickness = r_side_thickness = (16, 18, 19, 22, 25)
open_degree = (30, 45)
bt_offset = 15
bt_thickness = 4
inner_safe_dist = 70
offsets = [0, bt_offset, bt_thickness, inner_safe_dist]

# -=-=-=-=-=-=-=-=-=-=-=-=-
k_depth = k_depth[1]  # [0] = 300, [1] = 350
l_side_thickness = l_side_thickness[0]
r_side_thickness = r_side_thickness[0]
open_degree = open_degree[1]  # [0] = 30°, [1] = 45°
# -=-=-=-=-=-=-=-=-=-=-=-=-


def start_point(x, y):
    origin_x = origin_y = 50
    return origin_x + x, origin_y + y


def katet():
    inner_width = k_width - l_side_thickness - r_side_thickness
    return tan(radians(open_degree)) * inner_width


def width_validation():
    return max(k_width, 150)  # width couldn't be less then 150


def r_side_validation():
    depth = k_depth - katet()
    return sum(offsets) if depth - sum(offsets) <= 0 else depth


def depth_validation():
    return max(k_depth, 150)


def generate_svg_html():
    dwg = svgwrite.Drawing(filename='index.html',
                           size=('400mm', '400mm'),
                           profile='full', debug=True)
    left_side = dwg.rect(insert=(start_point(0, 0)),
                         size=(l_side_thickness,
                               depth_validation()),
                         id='leftSide')
    right_side = dwg.rect(insert=start_point(width_validation()
                                             - l_side_thickness, 0),
                          size=(r_side_thickness,
                                r_side_validation()),
                          id='rightSide')
    diagonal = dwg.line(start=start_point(l_side_thickness,
                                          depth_validation()),
                        end=start_point(width_validation() - l_side_thickness,
                                        r_side_validation()))

    hlines = dwg.add(dwg.g(id='hlines'))
    start_y = 0
    for y in offsets:
        start_y += y
        hlines.add(dwg.line(start=start_point(l_side_thickness, start_y),
                            end=start_point(width_validation()
                                            - l_side_thickness, start_y)))

    shapes = dwg.add(dwg.g(id='shapes'))
    shapes.add(left_side)
    shapes.add(right_side)
    shapes.add(diagonal)
    shapes.add(hlines)
    shapes.fill('blue', opacity=0.1).stroke('black', width=1).dasharray([5, 5])

    paragraph = dwg.add(dwg.g(font_size=20, fill='black'))
    paragraph.add(dwg.text(width_validation(), start_point(width_validation()/2-10, -5)))
    paragraph.add(dwg.text(round(depth_validation(), None), start_point(-35, depth_validation()/2)))
    paragraph.add(dwg.text(round(r_side_validation(), None), start_point(width_validation()+5, r_side_validation()/2 + 5)))
    paragraph.add(dwg.text(f'{open_degree}°', start_point(width_validation() - r_side_thickness - 40, r_side_validation() - 5)))

    # Add JavaScript code to update SVG attributes based on slider values
    js_code = '''
    <script>
        function updateRectSize() {
            var rect = document.getElementById('myRectangle');
            rect.setAttribute('width', document.getElementById('slider1').value);
            rect.setAttribute('height', document.getElementById('slider2').value);

            // Update current value labels
            var currentValue1 = document.getElementById('currentValue1');
            var currentValue2 = document.getElementById('currentValue2');
            var slider1 = document.getElementById('slider1');
            var slider2 = document.getElementById('slider2');
            var rectWidth = parseFloat(slider1.max) - parseFloat(slider1.min);
            var rectHeight = parseFloat(slider2.max) - parseFloat(slider2.min);
            currentValue1.style.marginLeft = 200/2 + 'px';
            currentValue2.style.marginLeft = 200/2 + 'px';
            currentValue1.textContent = slider1.value;
            currentValue2.textContent = slider2.value;
        }
    </script>
    '''

    # Add HTML code with sliders and SVG container
    html_code = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Corner kitchen cabinet calculation</title>
        <style>
            #slider1, #slider2 {
                width: 200px;
            }

            .slider-container {
                display: flex;
                flex-direction: column;
                align-items: left;
                text-align: center;
            }

            .slider-label {
                margin-top: 10px;
            }

            .slider-value {
                display: flex;
                justify-content: space-between;
                width: 200px;
            }

            .slider-current-value {
                position: relative;
                width: fit-content;
                margin-top: -20px;
            }
        </style>
    </head>
    <body>
        <h1>Corner kitchen cabinet calculation</h1>
        <div class="slider-container">
            <div class="slider-value">
                <span id="startValue1">16</span>
                <span id="endValue1">25</span>
            </div>
            <input type="range" id="slider1" min="16" max="25" value="16" oninput="updateRectSize()">
            <div class="slider-value">
                <span id="currentValue1" class="slider-current-value">16</span>
            </div>
        </div>
        <div class="slider-container">
            <div class="slider-value">
                <span id="startValue2">200</span>
                <span id="endValue2">1000</span>
            </div>
            <input type="range" id="slider2" min="200" max="1000" value="300" oninput="updateRectSize()">
            <div class="slider-value">
                <span id="currentValue2" class="slider-current-value">300</span>
            </div>
        </div>
        <select name="degree" method="GET" action="/">
            <option value="{{open_degree[0]}}" selected>{{open_degree[0]}}</option>
            {% for degree in open_degree[1:] %}
                <option value="{{degree}}">{{degree}}</option>
            {% endfor %}
        </select>
        <div id="svgContainer">
            ''' + dwg.tostring() + '''
        </div>
    </body>
    </html>
    '''

    with open('index.html', 'w') as file:
        file.write(js_code + html_code)


if __name__ == "__main__":
    generate_svg_html()
