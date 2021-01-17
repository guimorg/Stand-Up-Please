from setuptools import setup


APP = ["stand_up_please.py"]
OPTIONS = {
    "iconfile": "stand_up_please.icns"
}


setup(
    app=APP,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"]
)
