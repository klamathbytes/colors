// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// All of the Node.js APIs are available in this process.

module.exports.drawCircle = function drawCircle(ctx) {
    let radius = 100;
    let image = ctx.createImageData(2*radius, 2*radius);
    let data = image.data;

    for (let x = -radius; x < radius; x++) {
        for (let y = -radius; y < radius; y++) {
        
        let [r, phi] = xy2polar(x, y);
        
        if (r > radius) {
            // skip all (x,y) coordinates that are outside of the circle
            continue;
        }
        
        let deg = rad2deg(phi);
        
        // Figure out the starting index of this pixel in the image data array.
        let rowLength = 2*radius;
        let adjustedX = x + radius; // convert x from [-50, 50] to [0, 100] (the coordinates of the image data array)
        let adjustedY = y + radius; // convert y from [-50, 50] to [0, 100] (the coordinates of the image data array)
        let pixelWidth = 4; // each pixel requires 4 slots in the data array
        let index = (adjustedX + (adjustedY * rowLength)) * pixelWidth;
        
        let hue = deg;
        let saturation = r / radius;
        let value = 1.0;
        
        let [red, green, blue] = hsv2rgb(hue, saturation, value);
        let alpha = 255;
        
        data[index] = red;
        data[index+1] = green;
        data[index+2] = blue;
        data[index+3] = alpha;
        }
    }

    ctx.putImageData(image, 0, 0);
}

function xy2polar(x, y) {
    let r = Math.sqrt(x*x + y*y);
    let phi = Math.atan2(y, x);
    return [r, phi];
}

// rad in [-π, π] range
// return degree in [0, 360] range
function rad2deg(rad) {
    return ((rad + Math.PI) / (2 * Math.PI)) * 360;
}

// hue in range [0, 360]
// saturation, value in range [0,1]
// return [r,g,b] each in range [0,255]
// See: https://en.wikipedia.org/wiki/HSL_and_HSV#From_HSV
function hsv2rgb(hue, saturation, value) {
    let chroma = value * saturation;
    let hue1 = hue / 60;
    let x = chroma * (1- Math.abs((hue1 % 2) - 1));
    let r1, g1, b1;
    if (hue1 >= 0 && hue1 <= 1) {
        ([r1, g1, b1] = [chroma, x, 0]);
    } else if (hue1 >= 1 && hue1 <= 2) {
        ([r1, g1, b1] = [x, chroma, 0]);
    } else if (hue1 >= 2 && hue1 <= 3) {
        ([r1, g1, b1] = [0, chroma, x]);
    } else if (hue1 >= 3 && hue1 <= 4) {
        ([r1, g1, b1] = [0, x, chroma]);
    } else if (hue1 >= 4 && hue1 <= 5) {
        ([r1, g1, b1] = [x, 0, chroma]);
    } else if (hue1 >= 5 && hue1 <= 6) {
        ([r1, g1, b1] = [chroma, 0, x]);
    }

    let m = value - chroma;
    let [r,g,b] = [r1+m, g1+m, b1+m];

    // Change r,g,b values from [0,1] to [0,255]
    return [255*r,255*g,255*b];
}