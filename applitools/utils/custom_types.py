from __future__ import absolute_import

import typing as tp

if tp.TYPE_CHECKING:
    from selenium.webdriver.remote.webdriver import WebDriver
    from selenium.webdriver.remote.webelement import WebElement

    from applitools.core.geometry import Region
    from applitools.selenium.webdriver import EyesWebDriver
    from applitools.selenium.webelement import EyesWebElement

    RunningSession = tp.Dict[tp.Text, tp.Any]
    ViewPort = tp.Dict[tp.Text, int]
    AppOutput = tp.Dict[tp.Text, tp.Any]
    MatchResult = tp.Dict[tp.Text, tp.Any]
    AppEnvironment = tp.Dict[tp.Text, tp.Any]
    SessionStartInfo = tp.Dict[tp.Text, tp.Any]
    Num = tp.Union[int, float]
    RectangleSize = tp.Dict[tp.Text, Num]

    AnyWebDriver = tp.Union[EyesWebDriver, WebDriver]
    AnyWebElement = tp.Union[EyesWebElement, WebElement]
    FrameReference = tp.Union[tp.Text, int, EyesWebElement, WebElement]

    # could contain MouseTrigger, TextTrigger
    UserInputs = tp.List
