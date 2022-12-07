from logger.Logger import Logger

logger = Logger(colors=True, display_levels=True)


def test_display_colors_and_levels(capsys):
    logger.level = "info"
    logger.info("info")
    captured = capsys.readouterr()
    assert captured.out == "INFO: info\x1b[0m\n"
    logger.debug("debug")
    captured = capsys.readouterr()
    assert captured.out == "\x1b[95mDEBUG: debug\x1b[0m\n"
    logger.warning("warning")
    captured = capsys.readouterr()
    assert captured.out == "\x1b[93mWARNING: warning\x1b[0m\n"
    logger.critical("critical")
    captured = capsys.readouterr()
    assert captured.out == "\x1b[91mCRITICAL: critical\x1b[0m\n"
    logger.error("error")
    captured = capsys.readouterr()
    assert captured.out == "\x1b[91mERROR: error\x1b[0m\n"
