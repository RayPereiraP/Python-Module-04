def ft_value_security() -> None:
	print("cyber archives - vault security system")
	try:
		print("initiatint secure access\n")
		print("secure extraction: ")
		file_name = "classified_data.txt"
		with open(file_name) as file:
			print(file.read())
		print("\nsecure preservation: ")
		new_text = "\n[classified] new security protocols"
		with open(file_name, "a") as file:
			file.write(new_text)
		last_line = ""
		with open(file_name, "r") as file:
			for line in file:
				last_line = line
			print(last_line)
			print("vault automatically sealed upon completion\n")
	except Exception:
		print("error: there was an unexpected anomaly")

if __name__ == "__main__":
	ft_vault_security()
