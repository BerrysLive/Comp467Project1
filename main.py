import csv
import os

xytech_dir = "Xytech.txt"
baselight_dir = "Baselight_export.txt"

filename = "export.csv"
header = ["Producer", "Operator", "Job", "Notes"]

baselight_fixed_lines = []

#how i discussed to parse baselight
#split the file into a list called lines, .split("\n")
with open(baselight_dir, "r") as baselight_file:
    for baselight_line in baselight_file:
        # Skip lines containing "<null>" or "<err>" aka removing them
        if "<null>" in baselight_line or "<err>" in baselight_line:
            continue
        # Split the line into items in a list
        baselight_fixed_lines.append(baselight_line.split(" "))
#Now you have a list of every row of information

print("Baselight Frames")
for line in baselight_fixed_lines:
    print(line[1:])

def FrameCheck(frame_lists):
    list_of_frame_ranges = []
    #Go Thru List of lists that contains raw frame numbers
    for frame_list in frame_lists:
        frame_ranges = []
        # Remove Spaces, Check if it's a Number and if it is convert the str to an int
        frame_list = [int(frame.strip()) for frame in frame_list if frame.strip().isdigit()]
        if not frame_list:
            list_of_frame_ranges.append([])
            continue
        start = frame_list[0]
        end = start
        for i in range(1, len(frame_list)):
            if frame_list[i] != end + 1:
                # Add the frame range or single frame number
                frame_ranges.append(f"{start}" if start == end else f"{start}-{end}")
                start = frame_list[i]
            end = frame_list[i]
        # Add the last frame range or single frame number
        frame_ranges.append(f"{start}" if start == end else f"{start}-{end}")
        list_of_frame_ranges.append(frame_ranges)
    return list_of_frame_ranges

print("\nFrameCheck Test")
print(FrameCheck(baselight_fixed_lines))
