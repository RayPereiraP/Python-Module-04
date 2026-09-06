import sys

def ft_stream_management() -> None:
	print("cyber archives - communication system")
	arch_id = input("input stream active, enter archivist id: ")
	status = input("input stream active, enter status report: ")
	sys.stdout.write(f"\n[STANDARD] Archive status from {arch_id}: {status}")
	sys.stderr.write("\n[ALERT] System diagnostic: ")
	sys.stdout.write("\n[STANDARD] Data transmission complete\n")
	sys.stdout.write("\nThree-channel communication test successful.")

if __name__ == "__main__":
	ft_stream_management()