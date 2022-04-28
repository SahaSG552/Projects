import rhinoscriptsyntax as rs

startPoint = [1.0, 2.0, 3.0]
endPoint = [4.0, 5.0, 6.0]
line1 = [startPoint, endPoint]

lineID = rs.AddLine(line1[0], line1[1])
