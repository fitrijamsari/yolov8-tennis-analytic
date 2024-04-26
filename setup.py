from setuptools import find_packages, setup

setup(
    name="yolov8-tennis-match-tracking",
    version="0.1",
    description="Yolov8 Object Detection - Tennis Match Tracking",
    license="MIT",
    packages=find_packages(include=["src", "src.*"]),
    zip_safe=False,
)
