import pytest
from television import Television


def test_init():
    tv = Television()
    assert str(tv) == "Power == False, Channel == 0, Volume == 0"


def test_power():
    tv = Television()
    tv.power()
    assert str(tv) == "Power == True, Channel == 0, Volume == 0"
    tv.power()
    assert str(tv) == "Power == False, Channel == 0, Volume == 0"


def test_mute():
    tv = Television()
    tv.power()
    tv.volume_up()  # Volume should increase to 1
    tv.mute()       # Mute sets volume to 0
    assert str(tv) == "Power == True, Channel == 0, Volume == 0"
    tv.mute()       # Unmute restores previous volume
    assert str(tv) == "Power == True, Channel == 0, Volume == 1"


def test_channel_up():
    tv = Television()
    tv.channel_up()
    assert str(tv) == "Power == False, Channel == 0, Volume == 0"  # No change when off
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power == True, Channel == 1, Volume == 0"  # Channel should increase
    for _ in range(3):
        tv.channel_up()
    assert str(tv) == "Power == True, Channel == 0, Volume == 0"  # Wrap-around


def test_channel_down():
    tv = Television()
    tv.channel_down()
    assert str(tv) == "Power == False, Channel == 0, Volume == 0"  # No change when off
    tv.power()
    tv.channel_down()
    assert str(tv) == "Power == True, Channel == 3, Volume == 0"  # Wrap-around
    tv.channel_down()
    assert str(tv) == "Power == True, Channel == 2, Volume == 0"  # Decrease channel


def test_volume_up():
    tv = Television()
    tv.volume_up()
    assert str(tv) == "Power == False, Channel == 0, Volume == 0"  # No change when off
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power == True, Channel == 0, Volume == 1"  # Volume should increase
    tv.volume_up()
    assert str(tv) == "Power == True, Channel == 0, Volume == 2"  # Max volume reached
    tv.volume_up()
    assert str(tv) == "Power == True, Channel == 0, Volume == 2"  # Stays at max volume


def test_volume_down():
    tv = Television()
    tv.volume_down()
    assert str(tv) == "Power == False, Channel == 0, Volume == 0"  # No change when off
    tv.power()
    tv.volume_down()
    assert str(tv) == "Power == True, Channel == 0, Volume == 0"  # Stays at min volume
    tv.volume_up()
    tv.volume_up()  # Volume increases to 2
    tv.volume_down()
    assert str(tv) == "Power == True, Channel == 0, Volume == 1"  # Volume decreases
    tv.mute()
    assert str(tv) == "Power == True, Channel == 0, Volume == 0"  # Mute sets to 0
    tv.volume_down()
    assert str(tv) == "Power == True, Channel == 0, Volume == 0"  # Stays muted