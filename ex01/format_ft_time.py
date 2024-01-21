import time
import datetime

def main():
	seconds = round(time.time(), 4)
	scientific_notation = "{:.2e}".format(seconds)
	strftime = time.strftime("%d %m %Y", time.localtime(seconds))
	print("Seconds since January 1st, 1970:", f"{seconds:,}")
	print("Scientific notation:", scientific_notation)
	print("Date:", strftime)

if __name__ == '__main__':
	main()