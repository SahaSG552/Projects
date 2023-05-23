from math import tan, radians
import svgwrite


k_depth = (290, 340)
l_side_thickness = r_side_thickness = (16, 18, 19, 22, 25)
open_degree = (30, 45)
bt_offset = 15
bt_thickness = 4
inner_safe_dist = 70
offsets = [0, bt_offset, bt_thickness, inner_safe_dist]

# -=-=-=-=-=-=-=-=-=-=-=-=-
k_width = 100
k_depth = k_depth[1]
l_side_thickness = l_side_thickness[0]
r_side_thickness = r_side_thickness[0]
open_degree = open_degree[1]
# -=-=-=-=-=-=-=-=-=-=-=-=-


def start_point(x, y):
    origin_x = origin_y = 50
    return origin_x + x, origin_y + y


def katet():
    inner_width = width_validation() - l_side_thickness - r_side_thickness
    return tan(radians(open_degree)) * inner_width


def max_width():
    inner_depth = k_depth - sum(offsets)
    return inner_depth / tan(radians(open_degree)) + l_side_thickness + r_side_thickness


def width_validation():
    return max_width() if k_width > max_width() else max(k_width, 150)


def r_side_validation():
    depth = depth_validation() - katet()
    return sum(offsets) if depth - sum(offsets) <= 0 else depth


def depth_validation():
    return max(k_depth, 150)


def generate_svg(name):
    dwg = svgwrite.Drawing(filename=name,
                           size=('600', '600'),
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

    annotations = dwg.add(dwg.g(font_size=20, fill='black', id='annotations'))
    annotations.add(dwg.text(f'{round(width_validation(), None)} (max.{round(max_width(), None)})',
                             start_point(width_validation()/2-55, -5)))
    annotations.add(dwg.text(round(depth_validation(), None),
                             start_point(-35, depth_validation()/2)))
    annotations.add(dwg.text(round(r_side_validation(), None),
                             start_point(width_validation()+5,
                                         r_side_validation()/2 + 5)))
    annotations.add(dwg.text(f'{open_degree}°',
                             start_point(width_validation() - r_side_thickness - 40,
                                         r_side_validation() - 5)))

    dwg.save()


if __name__ == "__main__":
    generate_svg('kitchen_cabinet.svg')
