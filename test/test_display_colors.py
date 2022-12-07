from logger.Logger import Logger

logger = Logger(colors=True, display_levels=False)


def test_display_colors(capsys):
    logger.level = "info"
    logger.info("info")
    captured = capsys.readouterr()
    assert captured.out == "info\x1b[0m\n"
    logger.debug("debug")
    captured = capsys.readouterr()
    assert captured.out == "\x1b[95mdebug\x1b[0m\n"
    logger.warning("warning")
    captured = capsys.readouterr()
    assert captured.out == "\x1b[93mwarning\x1b[0m\n"
    logger.critical("critical")
    captured = capsys.readouterr()
    assert captured.out == "\x1b[91mcritical\x1b[0m\n"
    logger.error("error")
    captured = capsys.readouterr()
    assert captured.out == "\x1b[91merror\x1b[0m\n"
