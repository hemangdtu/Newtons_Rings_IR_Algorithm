# Investigating Interference Patterns in Newton’s Rings with Image Recognition Algorithm
A project aimed at investigating the interference phenomenon of Newton's Rings through the use of automated data collection via implementation of Image Recognition Algorithm.

## Prerequisites
<ul>
<li>Newton's Rings is a phenomenon in which an interference pattern is created by the reflection of a monochromatic light source between a spherical surface and an adjacent touching flat surface, having a layer of air exists between them.</li>
<li>We obtain concentric circles consisting of Dark and Bright fringes.</li>
<li>In order to calculate the radius of nth dark fringe we use the relation, r<sub>n</sub><sup>2</sup> = n𝛌R</li>
</ul>

## Flow of Control of Program
<ol>
<li>The image was then fed to the image recognition algorithm.</li>
<li>Gaussian blur was then applied by convolving the pixel values of the image.</li>
<li>Hough transform is applied to the image available in OpenCV Library.</li>
<li>The detected circles were then filtered by distance to the center of the image, and the center of one of the detected circles was chosen to be the center of the concentric rings in the interference pattern.</li>
<li>The data collected is then used to calculate the radius of curvature of convex lens.</li>
</ol>

## Description of Program Files
<table>
<thead>
  <tr>
    <th>S. No.</th>
    <th>Program File</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>1.</td>
    <td><a href="https://github.com/hemangdtu/Newtons_Rings_IR_Algorithm/blob/master/edge_detect.py" target="_blank" rel="noopener noreferrer">edge_detect.py</a></td>
    <td>Image recognition algorithm is implemented to detect the circular edges of the Newton's Ring pattern</td>
  </tr>
  <tr>
    <td>2.</td>
    <td><a href="https://github.com/hemangdtu/Newtons_Rings_IR_Algorithm/blob/master/pixel_conversion_2.py" target="_blank" rel="noopener noreferrer">pixel_conversion_2.py</a></td>
    <td>Used for unit conversion from Pixel to Millimeter to implement mathematical calculations involved in Newton's Ring experiment</td>
  </tr>
  <tr>
    <td>3.</td>
    <td><a href="https://github.com/hemangdtu/Newtons_Rings_IR_Algorithm/blob/master/plot.py" target="_blank" rel="noopener noreferrer">plot.py</a></td>
    <td>Plotting the results obtained from edge_detect.py and pixel_conversion_2.py</td>
  </tr>
</tbody>
</table>
