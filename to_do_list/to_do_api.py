import os

from dataclasses import dataclass

# to_do_api


def clear_screen():
	os.system("cls")


@dataclass
class Task:
	task: str = ""
	complete: bool = False

	def __str__(self):
		return self.task

	def is_complete(self):
		return self.complete

	def change_status(self, status: bool):
		self.complete = status

	def data_tuple(self):
		return self.task, self.complete


class ToDoList:
	def __init__(self, saved_tasks=None, title="To Do List", numbered=True, symbols=None):
		if saved_tasks is None:
			saved_tasks = []

		if symbols is None:
			symbols = {
				"complete": "x",
				"incomplete": " ",
				"shell": ["[", "]"]
			}
		# Data
		self.tasks = saved_tasks

		# Styling
		self.title = title
		self.numbered = numbered
		self.symbols = symbols

		# Map
		self.task_map = {}

		# Length
		self.length = self.check_length()
		self.update_map()

	def __str__(self):
		list_str = f"[ {self.title.capitalize()} ]:\n"

		count = 0
		style = ""
		for task in self.tasks:

			if self.numbered:
				count += 1
				style = f"{count}."

			fill = self.symbols["incomplete"]
			if task.is_complete():
				fill = self.symbols["complete"]

			# left, right = self.symbols["shell"]

			list_str += f"\n {self.symbols['shell'][0]}{fill}{self.symbols['shell'][1]} {style}{task}"

		list_str += "\n"
		return list_str

	def check_length(self):
		return len(self.tasks)

	def update_map(self):
		self.task_map = {}
		for _, item in enumerate(self.tasks):
			key = f"{_+1}"
			self.task_map[key] = item

	def add_task(self, task: Task) -> bool:
		self.tasks.append(task)
		self.length += 1
		self.update_map()
		return True

	def remove_task(self, index_num: str) -> bool:
		remove_item = self.task_map.get(index_num, False)

		if not remove_item:
			return False

		# int(index_num) - 1
		# Remove from list and dict
		self.tasks.remove(remove_item)
		del self.task_map[index_num]

		# Update Length
		self.length -= 1

		# Update Map
		self.update_map()

		return True

	def mark_complete(self):
		...

	def mark_incomplete(self):
		...

	def flip_mark(self, index_num: str) -> bool:
		flip_item = self.task_map.get(index_num, None)

		if not flip_item:
			return False

		match (flip_item.is_complete()):
			case True:
				flip_item.change_status(False)
				return True
			case False:
				flip_item.change_status(True)
				return True


if __name__ == "__main__":
	# Build List
	new_list = []
	for i in range(10):
		new_task = Task(f"Task #{i+1}")
		if i in [0, 1, 2, 3]:
			new_task.complete = True
		new_list.append(new_task)

	to_list = ToDoList(new_list, "Sample To Do List", numbered=True)

	# Display
	clear_screen()
	print(to_list)

	# Add task
	to_list.add_task(Task("Random task"))
	to_list.add_task(Task("2nd Random task"))


	# Change to Complete
	to_list.flip_mark("11")
	to_list.flip_mark("10")

	clear_screen()
	print(to_list)


	# # Remove item loop
	# while to_list.length != 0:
	# 	extra_text = ""
	# 	u_in = input("Select one to remove: ")
	# 	if u_in.lower() == 'q':
	# 		print("\n[ Program Quit ]\n")
	# 		quit()
	#
	# 	# should probably validate input first lol
	# 	is_removed = to_list.remove_task(u_in)
	#
	# 	clear_screen()
	# 	print(to_list)
	# 	if not is_removed:
	# 		extra_text = "| Invalid index: Nothing Removed!"
	#
	# 	print(f"Size: {to_list.length} {extra_text}")
	#
	# clear_screen()
	# print("[ EMPTY LIST ]\n\n")
