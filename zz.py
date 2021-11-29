import os
import rich
# zz


class Container:
	def __init__(self, cols=6, rows=3, data=None, custom_text=""):
		if data is None:
			data = []
		self.cols = cols
		self.rows = rows

		self.text = custom_text
		self.data = data
		self.update_size()

		self.style = {
			'top_left': "┏",
			'top_right': "┓",
			'bot_left': "┗",
			'bot_right': "┛",
			'vertical_wall': "┃",
			'horizontal_wall': "━"
		}
		self.display_cache = self.build_display_cache()

	def __str__(self):
		text = self.build_display_cache()
		return self.display_cache

	def update_size(self):
		self.rows = len(self.data)
		self.cols = len(self.data[0])

	def build_display_cache(self) -> str:
		tl_corner = self.style["top_left"]
		tr_corner = self.style["top_right"]
		bl_corner = self.style["bot_left"]
		br_corner = self.style["bot_right"]
		vert_wall = self.style["vertical_wall"]
		horiz_wall = self.style["horizontal_wall"]

		top_row = f"{tl_corner}{self.cols*horiz_wall}{tr_corner}\n"
		middle = ""
		if len(self.data) == 0:
			self.data = [[" " for x in range(self.cols)] for y in range(self.rows)]

		for i in range(self.rows):
			middle += f"{vert_wall}"
			for j in range(self.cols):
				current_cell = self.data[i][j]
				middle += f"{current_cell}"
			middle += f"{vert_wall}\n"

		bot_row = f"{bl_corner}{horiz_wall*self.cols}{br_corner}"

		return f"{top_row}{middle}{bot_row}"


if __name__ == "__main__":
	sample_data = [
		["#", " ", " "],
		["#", " ", " "],
		["#", " ", " "]
	]

	my_container = Container(24, 3)
	print(my_container)

