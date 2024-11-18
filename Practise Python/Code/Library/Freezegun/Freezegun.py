from freezegun import freeze_time
import datetime

# Run 'pytest' in shell
@freeze_time("2022-04-09")
def test_datetime():
    assert datetime.datetime.now() == datetime.datetime(2022, 4, 9)

def test_with():
    with freeze_time("Apr 9th, 2022"):
        assert datetime.datetime.now() == datetime.datetime(2022, 4, 9)

@freeze_time("Apr 9th, 2022", tick=True)
def test_time_ticking():
    assert datetime.datetime.now() > datetime.datetime(2022, 4, 9)

