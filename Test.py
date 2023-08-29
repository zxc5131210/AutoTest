import subprocess


def clear_package(package_name):
    command = ['adb', 'shell', 'pm', 'clear', package_name]
    try:
        result = subprocess.run(
            command, capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print(e.stderr)


if __name__ == "__main__":
    package_name = "com.viewsonic.wallpaperpicker"
    clear_package(package_name)
