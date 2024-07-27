from cx_Freeze import setup, Executable

setup(
    name="YourAppName",
    version="1.0",
    description="Description of your app",
    executables=[Executable("user_haxc.py")],
    install_requires=[
        'numpy>=1.21.0',
        'requests',
        'pandas==1.5.0',
        'opencv-python>=4.5.0',
        'telebot>=0.0.5'  
    ],
)