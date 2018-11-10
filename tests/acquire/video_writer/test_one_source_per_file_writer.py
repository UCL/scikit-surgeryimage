import pytest
import numpy as np
import os
from sksurgeryimage.acquire import video_writer as vw


def test_generate_single_filename(video_writer_single_source):

    video_writer = video_writer_single_source

    sequential_filenames = video_writer.generate_sequential_filenames()
    expected_single_filenames = ['tests/output/output_0.avi']
    assert sequential_filenames == expected_single_filenames


def test_generate_multiple_filenames(video_writer_five_sources):
    video_writer = video_writer_five_sources
    sequential_filenames = video_writer.generate_sequential_filenames()

    expected_single_filenames = [
        'tests/output/output_0.avi',
        'tests/output/output_1.avi',
        'tests/output/output_2.avi',
        'tests/output/output_3.avi',
        'tests/output/output_4.avi']
    assert sequential_filenames == expected_single_filenames


def test_generate_single_video_writer(video_writer_single_source):
    video_writer = video_writer_single_source

    video_writer.create_video_writers()
    assert len(video_writer.video_writers) == 1

    # Check video_writer has created files
    for filename in video_writer.generate_sequential_filenames():
        assert os.path.isfile(filename)

    video_writer.release_video_writers()
    assert not video_writer.video_writers[0].isOpened()


def test_generate_multiple_video_writers(video_writer_five_sources):
    video_writer = video_writer_five_sources

    video_writer.create_video_writers()
    assert len(video_writer.video_writers) == 5

    # Check video_writer has created files
    for filename in video_writer.generate_sequential_filenames():
        assert os.path.isfile(filename)

    video_writer.release_video_writers()
    for video_writer in video_writer.video_writers:
        assert not video_writer.isOpened()
