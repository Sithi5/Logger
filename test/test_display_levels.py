from logger.Logger import Logger

logger = Logger(colors=False, display_levels=True, display_date=False)


def test_display_levels(capsys):
    logger.level = "info"
    logger.info("info")
    captured = capsys.readouterr()
    assert captured.out == "INFO: info\n"
    logger.debug("debug")
    captured = capsys.readouterr()
    assert captured.out == "DEBUG: debug\n"
    logger.warning("warning")
    captured = capsys.readouterr()
    assert captured.out == "WARNING: warning\n"
    logger.critical("critical")
    captured = capsys.readouterr()
    assert captured.out == "CRITICAL: critical\n"
    logger.error("error")
    captured = capsys.readouterr()
    assert captured.out == "ERROR: error\n"
