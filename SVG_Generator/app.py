from flask import Flask, request, jsonify, render_template
import svgwrite
from math import tan, radians

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_graphics', methods=['POST'])
def generate_graphics():
    # Get the selected values from the request
    data = request.get_json()
    k_width = int(data['kWidth'])
    k_depth = int(data['kDepth'])
    l_side_thickness = int(data['lSideThickness'])
    r_side_thickness = int(data['rSideThickness'])
    open_degree = int(data['openDegree'])

    bt_offset = 15
    bt_thickness = 4
    inner_safe_dist = 70
    offsets = [0, bt_offset, bt_thickness, inner_safe_dist]

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


    # Generate the graphics using svgwrite
    dwg = svgwrite.Drawing('vector_graphics.svg', profile='tiny')
    # Your logic to generate the graphics here using the selected values
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

    annotations = dwg.add(dwg.g(font_size=20, fill='black', id='annotations'))
    annotations.add(dwg.text(width_validation(), start_point(width_validation()/2-10, -5)))
    annotations.add(dwg.text(round(depth_validation(), None), start_point(-35, depth_validation()/2)))
    annotations.add(dwg.text(round(r_side_validation(), None), start_point(width_validation()+5, r_side_validation()/2 + 5)))
    annotations.add(dwg.text(f'{open_degree}°', start_point(width_validation() - r_side_thickness - 40, r_side_validation() - 5)))

    # Save the SVG graphics to a file
    dwg.save()
    return jsonify({'svgPath': 'static/graphics.svg'})
    ## svg_content = dwg.tostring()
    # return jsonify({'svgContent': svg_content})

if __name__ == '__main__':
    app.run(debug=True)
