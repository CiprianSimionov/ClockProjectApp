from django.shortcuts import render
from datetime import datetime

# Create views here.
def digital_clock(request):
    current_hour = datetime.now()
    format_current_hour = current_hour.strftime("%H:%M:%S")
    format_current_hour = format_current_hour.replace(":", "o").replace(" ", "o")
    dict_hour = {

            '0': [
                " _ ",
                "| |",
                "|_|"
            ],
            '1': [
                "   ",
                "  |",
                "  |"
            ],
            '2': [
                " _ ",
                " _|",
                "|_ "
            ],
            '3': [
                " _ ",
                " _|",
                " _|"
            ],
            '4': [
                "   ",
                "|_|",
                "  |"
            ],
            '5': [
                " _ ",
                "|_ ",
                " _|"
            ],
            '6': [
                " _ ",
                "|_ ",
                "|_|"
            ],
            '7': [
                " _ ",
                "  |",
                "  |"
            ],
            '8': [
                " _ ",
                "|_|",
                "|_|"
            ],
            '9': [
                " _ ",
                "|_|",
                " _|"
            ],
            'o': [
                "   ",
                " o ",
                " o "
            ]
        }

    display_lines = ["", "", ""]
    for char in format_current_hour:
        if char in dict_hour:
            number = dict_hour[char]
            for i in range(3):
                display_lines[i] += number[i] + "   "
    return render(request, "ClockApp/clock.html", {"display_lines": display_lines})