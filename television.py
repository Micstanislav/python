class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Initializes the Television object with default settings.
        - TV is initially powered off.
        - Volume is set to the minimum volume (0).
        - Channel is set to the minimum channel (0).
        - Mute status is set to False.
        """
        self.__status = False  # TV is off by default
        self.__muted = False   # TV is not muted by default
        self.__volume = Television.MIN_VOLUME  # Volume is at the minimum level
        self.__channel = Television.MIN_CHANNEL  # Channel is set to the minimum

    def power(self) -> None:
        """
        Toggles the power status of the television.
        - If the TV is off, it turns on.
        - If the TV is on, it turns off.

        Returns:
            None
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Toggles the mute status of the television if the TV is on.
        - If the TV is on and not muted, it mutes the TV.
        - If the TV is on and already muted, it unmutes the TV.

        Returns:
            None
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Increases the channel number if the TV is on.
        - If the channel exceeds the maximum, it wraps around to the minimum channel.

        Returns:
            None
        """
        if self.__status:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Decreases the channel number if the TV is on.
        - If the channel goes below the minimum, it wraps around to the maximum channel.

        Returns:
            None
        """
        if self.__status:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Increases the volume if the TV is on.
        - If the TV is muted, it unmutes it.
        - Volume is capped at the maximum level.

        Returns:
            None
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decreases the volume if the TV is on.
        - If the TV is muted, it unmutes it.
        - Volume is capped at the minimum level.

        Returns:
            None
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Returns the current state of the television as a string.
        The format is:
        'Power == <status>, Channel == <current_channel>, Volume == <current_volume_or_0_if_muted>'

        Returns:
            str: The state of the television, including power status, channel, and volume.
        """
        display_volume = 0 if self.__muted else self.__volume
        return f"Power == {self.__status}, Channel == {self.__channel}, Volume == {display_volume}"