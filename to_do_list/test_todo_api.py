import os
from to_do_api import Task, ToDoList
# test_todo_api


# Build List
new_list = []
for i in range(10):
	new_task = Task(f"Task #{i+1}")
	if i in [0, 1, 2, 3]:
		new_task.complete = True
	new_list.append(new_task)

test_list = ToDoList(new_list, "Test To Do List", numbered=True)


def add_task_test():
	test_list.ap




# Add task
to_list.add_task(Task("Random task"))
to_list.add_task(Task("2nd Random task"))


# Change to Complete
to_list.flip_mark("11")
to_list.flip_mark("10")



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



if __name__ == "__main__":
	...
