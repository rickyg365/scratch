import os
from time import sleep
import numpy as np

from typing import List
from dataclasses import dataclass

from rich import inspect
from rich.table import Table
from rich.progress import track
from rich.console import Console

from faker import Faker

# process_dataclass
fake = Faker()


@dataclass
class User:
	username: str
	password: str
	email: str
	handle: str


def create_raw_user_data(amount: int) -> list[dict]:
	user_list = []

	for i in track(np.arange(amount), description="[ Creating users ]", transient=True):
		# user_dict = {
		# 	"name": f"name{i + 1}",
		# 	"password": f"password{i + 1}",
		# 	"email": f"email{i + 1}@email.com",
		# 	"handle": f"rando{i + 1}"
		# }
		# fal = fake.profile()
		# print(fal)
		full_name = fake.name()
		first, last = full_name.split(' ')

		user_dict = {
			"name": full_name,
			"password": fake.ssn(),
			"email": fake.email(),
			"handle": f"@{first[0].lower()}{last.lower()}"
		}

		user_list.append(user_dict)
		sleep(1)

	return user_list


def process_raw_data(raw_data: list, console: Console) -> list[User]:
	""" list[dict] = keys("name", "password", "email", "handle") """
	processed_users = []
	with console.status("[bold green]Adding users...") as status:
		for _, raw_user in enumerate(raw_data):
			username = raw_user['name']
			password = raw_user['password']
			email = raw_user['email']
			handle = raw_user['handle']

			new_user = User(
				username=username,
				password=password,
				email=email,
				handle=handle
			)

			processed_users.append(new_user)
			sleep(.15)
			console.log(f"User #{_+1}: {username} added")

	return processed_users


def add_to_table(my_table: Table, data):
	...


if __name__ == "__main__":
	# sample_raw_data = [
	# 	{
	# 		"name": "rand_name1",
	# 		"password": "password1",
	# 		"email": "email1@email.com",
	# 		"handle": "rando1"
	# 	},
	# 	{
	# 		"name": "rand_name2",
	# 		"password": "password2",
	# 		"email": "email2@email.com",
	# 		"handle": "rando2"
	# 	},
	# 	{
	# 		"name": "rand_name3",
	# 		"password": "password3",
	# 		"email": "email3@email.com",
	# 		"handle": "rando3"
	# 	},
	# 	{
	# 		"name": "rand_name4",
	# 		"password": "password4",
	# 		"email": "email4@email.com",
	# 		"handle": "rando4"
	# 	},
	# 	{
	# 		"name": "rand_name5",
	# 		"password": "password5",
	# 		"email": "email5@email.com",
	# 		"handle": "rando5"
	# 	}
	# ]
	sample_raw_data = create_raw_user_data(10)

	my_console = Console()

	python_obj_list = process_raw_data(sample_raw_data, my_console)

	print("")
	# my_console.print(python_obj_list)
	inspect(python_obj_list[0])

	table = Table(title="Random Users")

	# Create Columns
	table.add_column("Username", justify="center", style="cyan", no_wrap=True)
	table.add_column("Handle", justify="center", style="green")
	table.add_column("Email", justify="center", style="yellow")

	for user in python_obj_list:
		table.add_row(user.username, user.handle, user.email)

	my_console.print(table)
