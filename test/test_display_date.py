from datetime import datetime

from logger.Logger import Logger

logger = Logger(colors=False, display_levels=False, display_date=True)


def test_display_date(capsys):
    date_time_obj = datetime.now()
    date_str = date_time_obj.strftime("%F")
    logger.info("info")
    captured = capsys.readouterr()
    assert captured.out == f"[{date_str}] info\n"
    date_str = "18/09/19"

    # Test manually setting date
    date_time_obj = datetime.strptime(date_str, "%d/%m/%y")
    logger2 = Logger(
        colors=False, display_levels=False, display_date=True, date=date_time_obj
    )
    date_str = date_time_obj.strftime("%F")
    logger2.info("info")
    captured = capsys.readouterr()
    assert captured.out == f"[{date_str}] info\n"
