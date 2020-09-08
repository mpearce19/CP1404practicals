NAME_TO_CODE = {"aliceblue": "#f0f8ff", "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6", "aquamarine4": "#458b74",
                "blue1": "#0000ff",  "blue2": "#0000ee", "blue4": "#00008b", "blueviolet": "#8a2be2",
                "cadetblue1": "#98f5ff", "cadetblue2": "#8ee5ee"}

print(NAME_TO_CODE)

colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    if colour_name in NAME_TO_CODE:
        print(NAME_TO_CODE[colour_name])
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ")
