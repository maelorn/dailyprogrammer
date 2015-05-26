
output = {}

def init(width, height):
	output[0] = 0
	return [[0 for x in range(width)] for x in range(height)]


def add_color(canvas, input):
	color, top, left, width, height = input
	output[color] = 0
	for x in range(left, left + width):
		for y in range(top, top + height):
			canvas[y][x] = color
	return canvas


def count(canvas):
	keys = output.keys()
	flat_canvas = [item for sublist in canvas for item in sublist]
	print(flat_canvas)
	for key in keys:
		output[key] =  flat_canvas.count(key)
	print(output)
    
if __name__ == '__main__':
	canvas = init(20, 10)
	print(canvas)
	canvas = add_color(canvas, (1, 5, 5, 10, 3))
	print(canvas)
	canvas = add_color(canvas, (2, 0, 0, 7, 7))
	print(canvas)
	count(canvas)

	