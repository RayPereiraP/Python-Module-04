def ft_archive_creation() -> None:
	print("cyber archive\n")
	file_name: "new_discovery.txt"
	entry1 = "[entry --1] new quantum algorithm discovered\n"
	entry2 = "[entry --2] efficienty increased by 347%\n"
	entry3 = "[entry --3] archived by data archivist trainee"
	try: 
		print(f"initializing new storage unit: {file_name}")
		print("storage unit created sucess\n")
		print("inscribing preservation data...")
		with open(file_name, "w") as file:
			file.write(entry1)
			file.write(entry2)
			file.write(entry3)
		with open(file_name) as file:
			print(file.read())
		print("\ndata inscription complete. storage unit sealed")
		print(f"archive \'{file_name}\' ready for long-term preservation")
	except Exception:
		print("error: there was an unexpected anomaly")

if __name__ == "__main__":
	ft_archive_creation()