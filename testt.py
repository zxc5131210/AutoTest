from HTMLReport import TestReport

if __name__ == "__main__":
    report = TestReport()

report.add_entry(
    "vlauncher",
    "UI",
    "Test_Login",
    "Login screen should appear correctly",
    {"Step 1": "Open App", "Step 2": "Check login screen"},
    "Pass",
)
report.add_entry(
    "vlauncher",
    "UI",
    "Test_Logo",
    "Logo should be visible",
    {"Step 1": "Open App", "Step 2": "Check logo visibility"},
    "Fail",
)
report.add_entry(
    "vlauncher",
    "Functional",
    "Test_PlayVideo",
    "Video should play without lag",
    {"Step 1": "Open video", "Step 2": "Play video", "Step 3": "Check lag"},
    "Pass",
)

report.add_entry(
    "STB",
    "Connectivity",
    "Test_Wifi",
    "WiFi should connect automatically",
    {"Step 1": "Turn on STB", "Step 2": "Check WiFi connection"},
    "Fail",
)
report.add_entry(
    "STB",
    "UI",
    "Test_MainMenu",
    "Main menu should list all categories",
    {
        "qqq": "Fail",
        "Step 2": "Navigate to main menu",
        "Step 3": "Check categories",
    },
    "Fail",
)
# Saving to file
report.save_to_file("test_report.html")
