from logger.Logger import Logger

logger = Logger(colors=False, display_levels=False, display_date=False)


def test_error_level(capsys):
    logger.level = "error"
    logger.info("info")
    captured = capsys.readouterr()
    assert captured.out == ""
    logger.debug("debug")
    captured = capsys.readouterr()
    assert captured.out == ""
    logger.warning("warning")
    captured = capsys.readouterr()
    assert captured.out == ""
    logger.critical("critical")
    captured = capsys.readouterr()
    assert captured.out == ""
    logger.error("error")
    captured = capsys.readouterr()
    assert captured.out == "error\n"


def test_critical_level(capsys):
    logger.level = "critical"
    logger.info("info")
    captured = capsys.readouterr()
    assert captured.out == ""
    logger.debug("debug")
    captured = capsys.readouterr()
    assert captured.out == ""
    logger.warning("warning")
    captured = capsys.readouterr()
    assert captured.out == ""
    logger.critical("critical")
    captured = capsys.readouterr()
    assert captured.out == "critical\n"
    logger.error("error")
    captured = capsys.readouterr()
    assert captured.out == "error\n"


def test_warning_level(capsys):
    logger.level = "warning"
    logger.info("info")
    captured = capsys.readouterr()
    assert captured.out == ""
    logger.debug("debug")
    captured = capsys.readouterr()
    assert captured.out == ""
    logger.warning("warning")
    captured = capsys.readouterr()
    assert captured.out == "warning\n"
    logger.critical("critical")
    captured = capsys.readouterr()
    assert captured.out == "critical\n"
    logger.error("error")
    captured = capsys.readouterr()
    assert captured.out == "error\n"


def test_debug_level(capsys):
    logger.level = "debug"
    logger.info("info")
    captured = capsys.readouterr()
    assert captured.out == ""
    logger.debug("debug")
    captured = capsys.readouterr()
    assert captured.out == "debug\n"
    logger.warning("warning")
    captured = capsys.readouterr()
    assert captured.out == "warning\n"
    logger.critical("critical")
    captured = capsys.readouterr()
    assert captured.out == "critical\n"
    logger.error("error")
    captured = capsys.readouterr()
    assert captured.out == "error\n"


def test_info_level(capsys):
    logger.level = "info"
    logger.info("info")
    captured = capsys.readouterr()
    assert captured.out == "info\n"
    logger.debug("debug")
    captured = capsys.readouterr()
    assert captured.out == "debug\n"
    logger.warning("warning")
    captured = capsys.readouterr()
    assert captured.out == "warning\n"
    logger.critical("critical")
    captured = capsys.readouterr()
    assert captured.out == "critical\n"
    logger.error("error")
    captured = capsys.readouterr()
    assert captured.out == "error\n"
