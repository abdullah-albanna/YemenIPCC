import platform


bsystem = platform.system()

# Used to change the "Darwin" to "Mac" because it is known better with Mac not Darwin
if bsystem == "Darwin":
    system: str = "Mac"
else:
    system = bsystem
