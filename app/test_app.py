from app.app import analyze_logs

def test_analyze_logs():
    sample_logs = [
        "2026-10-14 10:00:00 INFO Server started",
        "2026-10-14 10:01:00 WARNING High memory usage",
        "2026-10-14 10:02:00 ERROR Database connection failed",
        "2026-10-14 10:03:00 INFO User logged in"
    ]
    result = analyze_logs(sample_logs)
    assert result["INFO"] == 2
    assert result["WARNING"] == 1
    assert result["ERROR"] == 1
