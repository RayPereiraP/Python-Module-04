def ft_ancient_text() -> None:
	try:
		print("Cyber archives - data recovery sys\n")
		file_name = "ancient_fragmant.txt"
		print(f"accessing: {file_name}\n")
		with open(file_name) as file:
			print(file.read())
		print("\ndata recovery complete")
	except FileNotFoundError:
		print("Error: that file was not found")
	except Exception:
		print("Error: there was an unexpected anomaly")

if __name__ == "__main__":
	ft_ancient_text()